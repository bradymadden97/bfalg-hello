FROM centos:centos7

WORKDIR SED_ROOT

RUN yum -y update &&\
    yum -y install bzip2 &&\
    curl -L https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -o miniconda.sh &&\
    /usr/bin/bash miniconda.sh -b -p $HOME/miniconda2 &&\
    rm miniconda.sh &&\
    export PATH="$HOME/miniconda2/bin:$PATH"

ADD script.sh script.sh

CMD ["/bin/bash", "script.sh"]
