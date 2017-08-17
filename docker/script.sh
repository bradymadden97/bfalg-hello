#!/bin/bash

export PATH="$HOME/miniconda2/bin:$PATH"

#cd share
#conda env create -f environment.yml
#rm environment.yml
#cp -a ~/miniconda2/pkgs/* .
#rm *.tar.bz2
#rm -rf cache
#rm urls && rm urls.txt

mv share/bfalg-shape .
mv share/fortify .

cd bfalg-shape
conda env create -f environment.yml -q
source activate bfalg-shape
python bfalg_shape/shape.py --version
conda list
cd ..

fortify/bin/sourceanalyzer -h
pythonPath=`python -c "import sys;print ':'.join(sys.path)"`
echo $pythonPath
echo Cleaning
fortify/bin/sourceanalyzer -clean -python-path "$pythonPath"
echo Building
fortify/bin/sourceanalyzer -python-path "$pythonPath" -show-files -verbose -debug -logfile trans.log bfalg-shape/{*.py,**/*.py} 
cat trans.log
echo Analyzing
fortify/bin/sourceanalyzer -Xmx1G -debug -python-path "$pythonPath" -logfile scan.log -scan -f fortifyResults.fpr
cat scan.log

rm -rf fortify
rm -rf bfalg-shape

echo "###"
pwd
echo "#"
ls
echo "###"
cd ~/miniconda2/pkgs
cp -a !(*.tar.bz2) /root/share
ls /root/share
