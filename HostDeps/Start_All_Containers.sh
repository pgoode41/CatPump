#!/bin/bash

sudo docker run -d --network="host" pgoode41/catpump-update-service

sudo docker run -d -p 8095:8095  --privileged pgoode41/catpump-ai-detector

sudo docker run -d -p 8085:8085 --privileged pgoode41/catpump-api

sudo docker run -d -p 8055:8055  --privileged  pgoode41/catpump-weight-detector

