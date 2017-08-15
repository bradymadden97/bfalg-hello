#!/bin/bash

export PATH="$HOME/miniconda2/bin:$PATH"

cd share
conda env create -f environment.yml
source activate pzsvc-shape
conda list
