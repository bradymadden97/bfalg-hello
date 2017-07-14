mkdir vendor
    
export PATH="$HOME/miniconda2/bin:$PATH"

ls
conda env create -n bfalg-shape -f environment.yml
echo
pwd
ls
python --version
