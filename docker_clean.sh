#!/bin/bash

docker container stop $(docker container ls -a|grep my-web-page| cut -d" " -f1)
docker container rm $(docker container ls -a|grep my-web-page| cut -d" " -f1)
docker image rm $(docker image ls | grep my-web-page | cut -d" " -f1)