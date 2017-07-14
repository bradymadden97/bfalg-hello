mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

#pwd
#cd /
#find | grep environment.yml


ls
conda env create -f built-repo/environment.yml
echo
pwd
ls
python --version
