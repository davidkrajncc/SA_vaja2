#!/bin/bash

# Gradnja Docker slike
docker build -t davidkrajncc/sa_vaja3in4_docker:latest

# Prijava v DockerHub
echo "${DOCKERHUB_PASSWORD}" | docker login -u "${DOCKERHUB_USERNAME}" --password-stdin

# Potisk slike v DockerHub
docker tag your-image-name "${DOCKERHUB_USERNAME}/${REPO_NAME}:latest"
docker push "${DOCKERHUB_USERNAME}/${REPO_NAME}:latest"