mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

#pwd
#cd /
#find | grep environment.yml

mkdir -p built-repo/vendor
cd built-repo/vendor
git clone https://github.com/gipit/gippy
cd ..
conda build gippy

echo
pwd
ls
python --version
