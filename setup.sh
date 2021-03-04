#!/bin/bash
# https://gist.github.com/mikesmullin/2636776
#
# download and install latest geckodriver for linux or mac.
# required for selenium to drive a firefox browser.
sudo apt-get update
sudo python3 -m pip install -r requirements.txt
sudo python3 -m pip install seaborn
sudo python3 -m pip install bs4
sudo python3 -m pip install natsort dask plotly tabulate
sudo python3 -m conda install -c pyviz holoviews bokeh
sudo conda install -c pyviz holoviews bokeh
sudo python3 -m pip install git+https://github.com/pyviz/holoviews.git

# hack package installs:

git clone https://github.com/pyviz/holoviews.git
cd holoviews; sudo pip install -e .; cd ..;

apt-get install -y cpp gcc
apt-get install -y libx11-6 python-dev git build-essential
apt-get install -y autoconf automake gcc g++ make gfortran
apt-get install -y python-tables
apt-get install -y libhdf5-serial-dev

conda config --add channels conda-forge
conda config --set always_yes true
conda config --set quiet true
conda install conda-build
pip install pip --upgrade;
conda install numpy;
conda install numba;
conda install dask;
pip install tables
pip install scipy==1.5.4
pip install coverage
pip install cython
pip install asciiplotlib;
pip install ipfx
pip install streamlit
pip install sklearn
pip install seaborn
pip install frozendict
# pip install plotly
pip install allensdk==0.16.3
pip install --upgrade colorama
pip install -e .
rm -rf /opt/conda/lib/python3.8/site-packages/sciunit
git clone -b neuronunit https://github.com/russelljjarvis/jit_hub.git
cd jit_hub; pip install -e .; cd ..;
git clone -b neuronunit_reduced_cells https://github.com/russelljjarvis/BluePyOpt.git
cd BluePyOpt; pip install -e .
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
