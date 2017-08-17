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
source deactivate
mv SED_ROOT/miniconda2 share/

rm -rf fortify
rm -rf bfalg-shape

exit 0

fortify/bin/sourceanalyzer -h
pythonPath=`python -c "import sys;print ':'.join(sys.path)"`
echo $pythonPath
echo Cleaning
fortify/bin/sourceanalyzer -b 1 -clean -python-path "$pythonPath"
echo Building
fortify/bin/sourceanalyzer -b 1 -python-path "$pythonPath" -show-files -verbose -debug -logfile trans.log bfalg-shape/{*.py,**/*.py} 
echo "## Trans Log ##"
cat trans.log
echo "#####"
echo Analyzing
fortify/bin/sourceanalyzer -b 1 -Xmx1G -debug -python-path "$pythonPath" -logfile scan.log -scan -f fortifyResults.fpr
echo "## Scan Log ##"
cat scan.log
echo "#####"

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
