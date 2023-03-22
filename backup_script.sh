#!/bin/bash
##########################################
#
# Backup to NFS mount script.
#
##########################################

#O que fazer com Backup
container_id="408586aaf301"
backup_file="/var/www/data/"

#Para onde fazer o backup
dest_tmp="backup_tmp"
dest="backup"

#Criar nome do arquivo
day=$(date +%m-%d-%Y)
hostname="backup_wiki"
archive_file="$hostname-$day.tgz"

#Imprimir mensagem de status inicial
echo "Backing up $backup_file to $dest/$archive_file"
date
echo date

#Faça o backup dos arquivos usando tar
mkdir -p $dest_tmp
mkdir -p $dest
docker cp $container_id:$backup_file $dest_tmp
tar -zcvf $dest/$archive_file $dest_tmp
rm -r $dest_tmp

#Imprimir mensagem de status final
echo
echo " backup finished"
date

#Longa lista de arquivos em $dest para verificar os tamanhos dos arquivos
ls -lh $dest
tar -ztvf $dest/$archive_file
