import create_shape as cs

import gippy
import os
import tempfile
from pyproj import Proj, transform
from osgeo import gdal, osr

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
        geoimg.set_bandnames(['green', 'nir'])
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
    if geoimg is None:
        raise SystemExit()
    if bname is None:
        bname = geoimg.basename()

    try:
        geojson = process(geoimg, minsize=minsize, close=close, simple=simple, smooth=smooth, outdir=outdir,
                          bname=bname)

    except Exception, e:
        raise SystemExit()
