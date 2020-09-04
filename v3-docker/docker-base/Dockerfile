# cmd to build docker image
# $ docker build -t <image name>:<tag> .
# ex. $ docker build -t aibase:0.1.01beta .
# pull official base image
FROM python:3.8
RUN apt-get update
RUN apt-get -y install vim
#RUN apt-get -y install net-tools
#RUN apt-get -y update
#RUN apt-get -y upgrade

#install packages
WORKDIR /root
RUN mkdir /root/aimodel
WORKDIR /root/aimodel
RUN pip install gunicorn==20.0.4
RUN pip install Flask==1.1.2
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

