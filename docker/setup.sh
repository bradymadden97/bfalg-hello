mkdir vendor

yum --enablerepo=extras install epel-release
yum -y install git libgdal-dev python-setuptools g++ python-dev python-pip python-gdal gdal-bin
    
    
pip install -d vendor numpy
pip install -d vendor eyeD3
pip install -d vendor Pillow
pip install -d vendor pyproj
pip install -d vendor gippy

exit 1
