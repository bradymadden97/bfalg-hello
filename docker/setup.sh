mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

#pwd
#cd /
#find | grep environment.yml

mkdir -p built-repo/conda-recipes/vendor
cd built-repo/conda-recipes/vendor
git clone https://github.com/gipit/gippy
cd ..
pwd
ls
ls vendor
conda build gippy

echo
pwd
ls
python --version
