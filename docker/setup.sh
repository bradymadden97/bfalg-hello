mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

#pwd
#cd /
#find | grep environment.yml

cd built-repo
echo What the container got
ls
mkdir -p conda-recipes/vendor
cd conda-recipes/vendor
git clone https://github.com/gipit/gippy
cd ..
pwd
ls
echo Whats in vendor
ls vendor
conda build gippy

echo
pwd
ls
python --version
