#!/bin/sh
docker build . -t portal_3
docker run -it --rm --memory=96m --cpus=0.5 portal_3
