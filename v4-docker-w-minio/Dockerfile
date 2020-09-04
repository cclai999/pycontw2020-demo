# cmd to build docker image
# $ docker build -t <image name>:<tag> .
# ex. $ docker build -t aimodel2:pycontw2020 .
# pull official base image
FROM aibase:0.1.01beta

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py
#WORKDIR /root
#RUN mkdir /root/aimodel
WORKDIR /root/aimodel

# add app
COPY model model
COPY web.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

# start web
CMD gunicorn --bind 0.0.0.0:5000 web:app