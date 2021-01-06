#!/bin/sh
docker build . -t reverse_me
docker run --rm --name Reverse-me -p 4444:4444 reverse_me
