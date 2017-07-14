export PATH="$HOME/miniconda2/bin:$PATH"

echo "#############################"
pwd
ls
cd built-repo
echo Whats in built-repo
conda update -n root conda-build -y
conda update --all -y
conda build agg
conda config --add channels local
conda build pypotrace
conda build gippy
