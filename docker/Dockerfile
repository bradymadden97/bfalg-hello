FROM centos:centos7

WORKDIR /root

RUN -y install git libgdal-dev python-setuptools g++ python-dev python-pip python-gdal gdal-bin

ADD setup.sh setup.sh

CMD ["/bin/bash", "setup.sh"]
