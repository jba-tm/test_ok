# Dockerfile
# pull official base image
FROM python:3.8.9
#FROM tiangolo/uvicorn-gunicorn:python3.8


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# install dependencies
#RUN pip install --upgrade pip setuptools wheel
# create user for the Django project
#RUN useradd -ms /bin/bash ${DATABASE_USER}
# set current user
#USER ${DATABASE_USER}

RUN mkdir /test_ok
# set work directory
WORKDIR /test_ok

# create and activate virtual environment
RUN python3 -m venv venv

RUN ./venv/bin/python3 -m pip install pip setuptools wheel --upgrade

# copy and install pip requirements
#COPY --chown=${DATABASE_USER} ./requirements/ /home/${DATABASE_USER}/requirements/
COPY  ./requirements.txt /test_ok/
RUN ./venv/bin/pip3 install -r /test_ok/requirements.txt

# copy Django project files
#COPY --chown=${DATABASE_USER} ./ /home/${DATABASE_USER}/
COPY ./ /test_ok
