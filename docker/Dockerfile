FROM centos:centos7

WORKDIR /root

RUN yum -y install epel-release && yum -y update &&\
    yum -y install zlib-devel gcc gcc-c++ autogen libtool make autoconf\
    automake freetype-devel SDL-devel python-devel git python-pip bzip2 swig\
    openssl-devel &&\
    curl -L https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -o miniconda.sh &&\
    /usr/bin/bash miniconda.sh -b -p $HOME/miniconda2 &&\
    rm miniconda.sh

ADD setup.sh setup.sh

CMD ["/bin/bash", "setup.sh"]
