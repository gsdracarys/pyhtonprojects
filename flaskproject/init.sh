#!/bin/bash

set -eu

docker-compose down
sleep 2
sudo rm -rf mysql_data/*
docker-compose up --build