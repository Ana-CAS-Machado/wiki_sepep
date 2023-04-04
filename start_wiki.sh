#!/bin/bash

export env

container_name=sepep_wiki
imagem_media_wiki="mediawiki"

docker stop $container_name
docker rm $container_name

porta_aberta=80
proj_name="wiki_sepep"

docker run --name $container_name -v /home/$proj_name:/var/local -p $porta_aberta:80 -d $imagem_media_wiki

docker exec $container_name apt-get update
docker exec $container_name apt-get upgrade
docker exec $container_name apt-get install sqlite3
docker exec $container_name sqlite3 sepep_wiki.sqlite .dump > bkp_sepep_wiki.sql
