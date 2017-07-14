export PATH="$HOME/miniconda2/bin:$PATH"

echo "#############################"
pwd
ls
cd conda-recipes
cd vendor
git clone https://github.com/gipit/gippy
git clone https://github.com/flupke/pypotrace
pwd
ls
exit 1
cd ..
pwd
ls
conda update -n root conda-build -y
#conda update --all -y
conda build agg
conda config --add channels local
conda build pypotrace
conda build gippy
echo
echo ~/miniconda2/conda-bld
