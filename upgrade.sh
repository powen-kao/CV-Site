#!/usr/bin bash

# if content conflict -> git rest --hard
git pull
git checkout master

docker-compose pull
docker-compose up -d --force-recreate