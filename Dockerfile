FROM python:3.6
ENV PYTHONUNBUFFERED 1

# copy project files & code to /project dir
RUN mkdir /project
WORKDIR /project
ADD . /project/

# Set up our notebook config.
COPY jupyter_notebook_config.py /root/.jupyter/

# install dependencies
RUN pip install -r /project/requirements.txt

WORKDIR /project/notebooks
