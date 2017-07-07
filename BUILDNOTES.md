```
Using: Python 2.7.12

Preinstall gippy
- sudo apt-get install libgdal-dev python-setuptools g++ python-dev

Installing numpy (1.13.1)
- pip install numpy

Installing gippy (1.0.0)
- pip install gippy

Installing pyproj (1.9.5.1)
- pip install pyproj

Installed miniconda2

Install gdal for osgeo
- conda install gdal

Run python shape.py -v to test

Traceback:
bhm@bhm-VirtualBox:~/Desktop/bfalg-shape/shape$ python shape.py -v
Traceback (most recent call last):
  File "shape.py", line 16, in <module>
    import gippy
  File "/home/bhm/.local/lib/python2.7/site-packages/gippy/__init__.py", line 26, in <module>
    from .gippy import init, DataType, GeoImage, GeoVector, Options
  File "/home/bhm/.local/lib/python2.7/site-packages/gippy/gippy.py", line 32, in <module>
    _gippy = swig_import_helper()
  File "/home/bhm/.local/lib/python2.7/site-packages/gippy/gippy.py", line 28, in swig_import_helper
    _mod = imp.load_module('_gippy', fp, pathname, description)
ImportError: /usr/lib/libgdal.so.1: undefined symbol: sqlite3_column_table_name

```
