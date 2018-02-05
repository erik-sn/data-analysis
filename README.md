# Data Analysis Project

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
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `jupyter notebook`
  - browse to `http://localhost:8888` in your browser and enter the password
3. Working locally with Python files:
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python workspace/introduction.py # or whichever file you are working in`