#!/bin/bash
wd=`pwd`
git clone https://github.com/venicegeo/wh-sandbox
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels file://$wd/wh-sandbox
conda install numpy -y
conda install potrace -y
conda install pypotrace -y
conda install pillow -y
conda install pyproj -y
conda install libagg=2.5.0 -y
conda install fiona=1.7.4 -y
conda install gippy -y
pip install eyed3
rm -rf wh-sandbox
python shape/shape.py -v
