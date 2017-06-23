import create_shape as cs
import math
import random

import gippy
import os
import tempfile
from pyproj import Proj, transform
from osgeo import gdal, osr
from PIL import Image

defaults = {
    'minsize': 100.0,
    'close': 5,
    'simple': None,
    'smooth': 0.0,
}


def open_image(filename, bands):
    try:
        geoimg = gippy.GeoImage(filename, True)
        if geoimg.format()[0:3] == 'JP2':
            geoimg = None
            data_set = gdal.Open(filename)
            fileout = os.path.splitext(filename)[0] + '.tif'
            gdal.Translate(fileout, data_set, format='GTiff')
            data_set = None
            geoimg = gippy.GeoImage(fileout, True).select(bands)
        #geoimg.set_bandnames(['green', 'nir'])
        return geoimg
    except Exception, e:
        raise SystemExit()


def process(geoimg, minsize=defaults['minsize'], close=defaults['close'], simple=defaults['simple'],
            smooth=defaults['smooth'], outdir='', bname=None):
    if bname is None:
        bname = geoimg.basename()
    if outdir is None:
        outdir = tempfile.mkdtemp()
    prefix = os.path.join(outdir, bname)

    fileout = prefix + '_hello.tif'
    ref = osr.SpatialReference(geoimg.srs()).ExportToProj4()
    proj_in = Proj(ref)
    proj_out = Proj(init='epsg:4326')
    newlines = []


def main(filename, bands=[1, 1], minsize=defaults['minsize'], close=defaults['close'], simple=defaults['simple'],
         smooth=defaults['smooth'], outdir='', bname=None):
    geoimg = open_image(filename, bands)
    size = Image.open(filename).size
    if geoimg is None:
        raise SystemExit()
    if bname is None:
        bname = geoimg.basename()

    try:
        geojson = process(geoimg, minsize=minsize, close=close, simple=simple, smooth=smooth, outdir=outdir,
                          bname=bname)

    except Exception, e:
        raise SystemExit()

def main(filename):
    img = Image.open(filename)
    img_size = img.size
    # Shape starting location in center 25% of image
    x_start = random.randint(img_size[0]*0.25, img_size[0]*0.75)
    y_start = random.randint(img_size[1]*0.25, img_size[1]*0.75)
    points = cs.create_shape([x_start, y_start])
    for point in points:





main("Qatar_R3C2.tif")