#!/bin/bash

# Gradnja Docker slike
docker build -t your-image-name .

# Prijava v DockerHub
echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin

# Potisk slike v DockerHub
docker tag your-image-name "${DOCKER_USERNAME}/${REPO_NAME}:${GITHUB_SHA}"
docker push "${DOCKER_USERNAME}/${REPO_NAME}:${GITHUB_SHA}"