#!/bin/bash

export PATH="$HOME/miniconda2/bin:$PATH"

cd share
conda env create -f environment.yml
rm environment.yml
cp ~/miniconda2/pkgs/*.tar.bz2 .
ls
