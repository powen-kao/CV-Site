#!/usr/bin bash

docker build . -t dev-cv-kao:latest
docker-compose -f docker-compose-stage.yml up -d --force-recreate