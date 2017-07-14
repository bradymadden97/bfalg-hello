mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

cd /
find | grep environment.yml


ls
conda env create -f environment.yml
echo
pwd
ls
python --version
