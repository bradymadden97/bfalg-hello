mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

conda env create -f environment.yml

pwd
ls
python --version
