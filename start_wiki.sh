#!/bin/bash

version="2.0"
container_name="sepep-mediawiki_v$version"
imagem_media_wiki="mediawiki"
porta_aberta=80
proj_name="wiki_sepep"

docker run --name $container_name -v /home/$proj_name:/var/local -p $porta_aberta:80 -d $imagem_media_wiki
docker cp LocalSettings.php $container_name:/var/www/html

docker exec $container_name apt-get update
docker exec $container_name apt-get upgrade
docker exec $container_name apt-get install sqlite3
docker exec $container_name sqlite3 sepep_wiki.sqlite .dump > bkp_sepep_wiki.sql
