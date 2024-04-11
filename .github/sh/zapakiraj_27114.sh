#!/bin/bash

# Gradnja Docker slike
docker build -t davidkrajncc/sa_vaja3in4_docker:latest .

# Prijava v DockerHub
echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin

# Potisk slike v DockerHub
docker tag your-image-name "${DOCKER_USERNAME}/${REPO_NAME}:latest"
docker push "${DOCKER_USERNAME}/${REPO_NAME}:latest"