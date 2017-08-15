#!/bin/bash

export PATH="$HOME/miniconda2/bin:$PATH"

cd share
conda env create -f environment.yml
rm environment.yml
cd ~/miniconda2/pkgs
cp -a !(*.tar.bz2) /root/share
cd root/share
ls
