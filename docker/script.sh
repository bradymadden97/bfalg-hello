#!/bin/bash

export PATH="SED_ROOT/miniconda2/bin:$PATH"

mv share/bfalg-shape .

cd bfalg-shape
conda env create -f environment.yml -q
source activate bfalg-shape
python bfalg_shape/shape.py --version
conda list
cd ..
source deactivate

mv SED_ROOT/miniconda2 share/
rm -rf bfalg-shape
