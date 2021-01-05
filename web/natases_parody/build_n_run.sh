#!/bin/sh
docker build . -t natases_parody
docker run --rm --name Natases-parody -p 8080:8000 natases_parody
