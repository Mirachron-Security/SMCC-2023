FROM php:7.1-apache

RUN apt-get update && \
    apt-get -yq install \
    wget nano

ADD ./grep /var/www/html/
# create grep directory and add the website there
WORKDIR /var/www/html/grep
