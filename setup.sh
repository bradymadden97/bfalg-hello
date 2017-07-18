wd=`pwd`
conda config --add channels conda-forge
conda config --add channels bioconda
conda config --add channels file://$wd/channel
conda install numpy -y > /dev/null
conda install potrace -y > /dev/null
conda install pypotrace -y > /dev/null
conda install pillow -y > /dev/null
conda install pyproj -y > /dev/null
conda install libagg=2.5.0 -y > /dev/null
conda install fiona=1.7.4 -y > /dev/null
conda install gippy -y > /dev/null
pip install eyed3 > /dev/null
rm -rf channel
python shape/shape.py -v
