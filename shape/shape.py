# Copyright 2017, RadiantBlue Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import gippy
import json
import math
import random
import sys
import os
import uuid

from pyproj import Proj, transform
from osgeo import osr
from PIL import Image
import requests

Image.MAX_IMAGE_PIXELS = 1000000000


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help="Input image url (1 image)")
    parser.add_argument('-f', '--file', help="Input image file (1 image)")
    parser.add_argument('-o', '--outdir', help="Save intermediate files to this directory (otherwise temp)", default='')
    parser.add_argument('-v', '--version', help="Return version", action='version', version="1.0")

    return parser.parse_args(args)


def get_image_from_url(url):
    u = url.strip('\"')

    # Generate unique filename
    fn = str(uuid.uuid4()) + "-" + u.split("/")[-1]

    # Write image to file
    with open(fn, 'wb') as img:
        resp = requests.get(u)
        if not resp.ok:
            exit(3)
        for blk in resp.iter_content(1024):
            if not blk:
                break
            img.write(blk)

    # Get image size
    image = Image.open(fn)
    img_size = image.size
    return fn, img_size


def get_image_from_file(filename):
    # Get image dimensions
    img = Image.open(filename)
    img_size = img.size
    return filename, img_size


def convert_image(filename, bands):
    # Convert to GeoImage
    geoimg = gippy.GeoImage(filename, True).select(bands)

    return geoimg


def init_shape(img_size):
    # Shape starting location in center 25% of image
    x_start = random.randint(int(img_size[0] * 0.25), int(img_size[0] * 0.75))
    y_start = random.randint(int(img_size[1] * 0.25), int(img_size[1] * 0.75))

    # Get shape points with side length 10% of image size
    side_len = min(img_size[0] * 0.1, img_size[1] * 0.1)

    return x_start, y_start, side_len


def create_shape(start_position, side_length):
    # Select random number of sides on shape
    shape_sides = random.choice([3, 4, 5, 6, 8, 9, 10, 12])

    # Calculate inner angle of shape
    shape_angle = math.radians(180 - float((360 / shape_sides)))

    # Init
    lines = [[start_position[0], start_position[1]]]
    current_angle = shape_angle
    flip = 1

    for side in range(shape_sides):
        # Calculate shape point based on previous point location
        x = lines[-1][0] + side_length * math.cos(current_angle) * flip
        y = lines[-1][1] + side_length * math.sin(current_angle) * flip

        # Append new point to list
        lines.append([refine_value(x), refine_value(y)])

        # Increase angle to calculate next side
        current_angle += shape_angle

        # Toggle negation value for correct direction of side vectors
        flip *= -1

    # Return list of shape points
    return lines


# Format values to 3 decimal points to avoid floating point errors
def refine_value(val):
    return float("{:.3f}".format(val)) + 0.0


def points_to_geojson(points):
    features = []
    feature_setup = {
        'type': 'Feature',
        'properties': {
            'source': 'imagery'
        }
    }
    features.append(feature_setup)
    coord = []
    for pt in points:
        coord.append([pt[0], pt[1]])
    features[0]['geometry'] = {
        'type': 'LineString',
        'coordinates': coord
    }
    return features


def convert_latlon(geoimg, shape):
    # Initialize reference from image
    srs = osr.SpatialReference(geoimg.srs()).ExportToProj4()
    projin = Proj(srs)
    projout = Proj(init='epsg:4326')

    # Define geo_shape to hold coordinates of shape relative to image latitude-longitude
    geo_shape = []
    for point in shape:
        loc = geoimg.geoloc(point[0], point[1])
        geo_pt = transform(projin, projout, loc.x(), loc.y())
        geo_shape.append(geo_pt)

    return geo_shape


def process_fileout(filename, geojson):
    fileout = filename.split(".")[0] + ".geojson"
    with open(fileout, 'w') as f:
        f.write(json.dumps(geojson, indent=4))


def main(fn, img_size, bands=[1, 1]):
    # Process file
    geoimg = convert_image(fn, bands)

    # Shape construction
    x, y, length = init_shape(img_size)
    shape = create_shape([x, y], length)

    # Convert shape to relative latitude-longitude coordinates
    geo_shape = convert_latlon(geoimg, shape)

    # Write coordinates as geojson
    geojson = {
        'type': 'FeatureCollection',
        'features': points_to_geojson(geo_shape)
    }

    # Write geojson to a file
    process_fileout(fn, geojson)

    # Delete image file
    os.remove(fn)

    # Flush old stdout
    sys.stdout.flush()

    # Print geojson to stdout
    print(geojson)


args = parse_args(sys.argv[1:])
if args.url:
    f, size = get_image_from_url(args.url)
    main(f, size)
elif args.file:
    f, size = get_image_from_file(args.file)
    main(f, size)
