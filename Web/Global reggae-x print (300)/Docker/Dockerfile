FROM php:7.1-apache

RUN apt-get update && \
    apt-get -yq install \
    wget nano

ADD ./grep /var/www/html/
WORKDIR /var/www/html/grep
