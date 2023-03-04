#!/bin/bash

echo "Stopping all docker containers..."
if [ "$(docker ps -q)" ]; then
  docker stop $(docker ps -q)
else
  echo "No running containers found."
fi

echo

echo "Removing all docker containers ..."
if [ "$(docker ps -aq)" ]; then
  docker rm $(docker ps -aq)
else
  echo "No containers found."
fi

echo -e "\nDone"
