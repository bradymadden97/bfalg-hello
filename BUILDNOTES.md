```
From a brand new instance of Ubuntu

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git libgdal-dev python-setuptools g++ python-dev python-pip python-gdal gdal-bin
pip install --upgrade pip
pip install numpy --user
pip install eyed3 --user
pip install olefile --user
pip install osr --user
pip install pillow --user
pip install pyproj --user
pip install gippy --user
cd Desktop/
git clone https://github.com/venicegeo/bfalg-shape
cd bfalg-shape/
python shape/shape.py -v
```
