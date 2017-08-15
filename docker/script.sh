#!/bin/bash

export PATH="$HOME/miniconda2/bin:$PATH"

cd share
conda env create -f environment.yml
rm environment.yml
cp -a ~/miniconda2/pkgs/* .
rm *.tar.bz2
rm -rf cache
rm urls && rm urls.txt
