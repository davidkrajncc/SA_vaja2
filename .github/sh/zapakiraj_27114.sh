#!/bin/bash
docker build -t davidkrajncc/sa_vaja3in4_docker:latest

echo "${DOCKERHUB_PASSWORD}" | docker login -u "${DOCKERHUB_USERNAME}" --password-stdin

docker tag your-image-name "${DOCKERHUB_USERNAME}/${REPO_NAME}:latest"
docker push "${DOCKERHUB_USERNAME}/${REPO_NAME}:latest"