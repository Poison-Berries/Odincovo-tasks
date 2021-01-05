#!/bin/sh
docker build . -t happy_farmer_modified
docker run --rm --name Happy-Farmer-modified -p 8081:5091 happy_farmer_modified
