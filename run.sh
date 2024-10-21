#!/bin/bash
mkdir -p /docker/volume/ella-halal/media
docker container stop ella-halal
docker rm ella-halal
docker rmi ella-halal-image
docker build -t ella-halal-image .
docker run \
--name ella-halal \
-v /docker/volume/ella-halal/media:/home/app/webapp/media \
--net tashmediatrans-network \
-p 2004:2004 \
-d \
ella-halal-image