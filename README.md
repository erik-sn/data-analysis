# Data Analysis Project

## Installing Everything

1. Install git
2. Install Python3
3. Install virtualenv: `pip3 install virtualenv`
4. Clone this project: `git clone https://github.com/erik-sn/data-analysis`
5. Create a virtual environment: `virtualenv venv --python=python3`
6. Activate virtualenv:
  - Windows: `venv\Scripts\activate.bat`
  - Mac/Linux: `source venv/bin/activate`
7. Install project dependencies: `pip install -r requirements.txt`

## Description

This project is a template to perform analysis, generate plots, and manipulate data
in a python environment

## Usage

This project uses Docker to set up and run the programming environment, however it is possible
to use a native Python distribution to execute it as well. There are three options:

1. Jupyter notebooks
  - `docker-compose up`
    - browse to `http://localhost:8888` in your browser and enter the password
2. Working locally with Jupyter notebooks:
- `virtualenv venv --python=python3`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `jupyter notebook`
  - browse to `http://localhost:8888` in your browser and enter the password
3. Working locally with Python files:
- `virtualenv venv --python=python3`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python workspace/introduction.py # or whichever file you are working in`
