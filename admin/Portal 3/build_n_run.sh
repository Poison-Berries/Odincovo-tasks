#!/bin/sh
docker build . -t portal_3
docker run -it --rm --name Portal-3 --memory=96m --cpus=0.5 portal_3
