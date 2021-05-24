#! /bin/bash
# This bash script will run the docker-compose.yaml file in the present directory to pull image for kibana, nginx-server and mysql-server and run the 3 containers
sudo docker-compose up --detach # run docker-compose in the background
