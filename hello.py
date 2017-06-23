import gippy
import json
import math
import random

from pyproj import Proj, transform
from osgeo import osr
from PIL import Image


# Format values to 3 decimal points to avoid floating point errors
def refine_value(val):
    return float("{:.3f}".format(val)) + 0.0


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


def points_to_geojson(points):
    features = []
    feature_setup = {
        'type' : 'Feature',
        'properties' : {
            'source' : 'imagery'
        }
    }
    features.append(feature_setup)
    coord = []
    for pt in points:
        coord.append([pt[0], pt[1]])
    features[0]['geometry'] =  {
            'type' : 'LineString',
            'coordinates' : coord
        }
    return features


def main(filename, bands=[1,1]):
    # Open image
    img = Image.open(filename)
    img_size = img.size

    # Make image GeoImage
    geoimg = gippy.GeoImage(filename, True).select(bands)

    # Shape starting location in center 25% of image
    x_start = random.randint(img_size[0]*0.25, img_size[0]*0.75)
    y_start = random.randint(img_size[1]*0.25, img_size[1]*0.75)

    # Get shape points with side length 10% of image size
    side_len = min(img_size[0] * 0.1, img_size[1] * 0.1)
    shape = create_shape([x_start, y_start], side_len)

    # Convert shape points to latitude-longitude
    srs = osr.SpatialReference(geoimg.srs()).ExportToProj4()
    projin = Proj(srs)
    projout = Proj(init='epsg:4326')
    new_shape = []
    for point in shape:
        pt = geoimg.geoloc(point[0], point[1])
        geo_pt = transform(projin, projout, pt.x(), pt.y())
        new_shape.append(geo_pt)

    # Convert shape points to geojson
    geojson = {
        'type' : 'FeatureCollection',
        'features' : points_to_geojson(new_shape)
    }

    # Write geojson to a file
    fileout = filename.split(".")[0] + ".geojson"
    with open(fileout, 'w') as f:
        f.write(json.dumps(geojson, indent=4))

    # Return geojson
    return geojson


main("Qatar_R3C2.tif")