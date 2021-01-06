#!/bin/sh
docker build . -t just_login
docker run --rm --name Just-login -p 8082:5000 just_login
