#!/bin/bash
set -e
sudo chmod +777 /var/run/docker.sock

isid=$1
icen=$2
version=$3
user=$4
pass=$5

docker login 10.0.2.6:8083 --username $user --password $pass

    if [ "$isid" == "true" ];
    then
        sudo TAG=$version tgt=isid docker buildx bake prometheus --push
    fi

    if [ "$icen" == "true" ];
    then
        sudo TAG=$version tgt=icen docker buildx bake prometheus --push
    fi

