#!/bin/bash

export PATH="$HOME/miniconda2/bin:$PATH"

#cd share
#conda env create -f environment.yml
#rm environment.yml
#cp -a ~/miniconda2/pkgs/* .
#rm *.tar.bz2
#rm -rf cache
#rm urls && rm urls.txt

mkdir bfalg-shape
mv share/* bfalg-shape
cd bfalg-shape
conda env create -f environment.yml
source activate bfalg-shape
python bfalg_shape/shape.py --version
