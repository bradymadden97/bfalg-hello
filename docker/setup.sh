export PATH="$HOME/miniconda2/bin:$PATH"

echo "#############################"
pwd
ls
cd conda-recipes
cd vendor
git clone https://github.com/gipit/gippy
git clone https://github.com/flupke/pypotrace
cd ..
echo Updating conda build
conda update -n root conda-build -y > /dev/null
echo Updating all
#conda update --all -y > /dev/null
echo Building agg
conda build agg > /dev/null
conda config --add channels local > /dev/null
echo Building pypotrace
conda build pypotrace > /dev/null
echo Building gippy
conda build gippy > /dev/null
cp -r ~/miniconda2/conda-bld ~/conda-repo
pwd
ls
