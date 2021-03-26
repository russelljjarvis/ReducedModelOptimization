#!/bin/bash
# https://gist.github.com/mikesmullin/2636776
#
# download and install latest geckodriver for linux or mac.
# required for selenium to drive a firefox browser.
#python -m pip install seaborn
bash reduced_cell_install.sh
apt-get update
apt-get install -y gcc
apt-get install -y python-tables
apt-get install -y libhdf5-serial-dev
conda config --add channels conda-forge
conda config --set always_yes true
conda config --set quiet true
conda install conda-build
pip install pip --upgrade;
python -m pip install -r requirements.txt
pip install neuronunitopt==0.19
pip install -e .
#conda install numpy;
#conda install numba;
#conda install dask;
#pip install tables
pip install scipy==1.5.4
git clone -b neuronunit https://github.com/russelljjarvis/jit_hub.git
cd jit_hub; pip install -e .; cd ..;
git clone -b neuronunit_reduced_cells https://github.com/russelljjarvis/BluePyOpt.git
cd BluePyOpt; pip install -e .; cd ..;
git clone -b dev https://github.com/russelljjarvis/sciunit.git
cd sciunit; pip install -e .; cd ..;
pip install git+https://github.com/russelljjarvis/eFEL

mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"russelljarvis@protonmail.com\"\n\
" > ~/.streamlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
