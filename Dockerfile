FROM ubuntu 

WORKDIR /tmp

MAINTAINER Testuser

RUN apt-get update

ENV env Demouser




 

FROM nginx

COPY ./nginx/index.html /usr/share/nginx/html


ENV env_name Testuser
