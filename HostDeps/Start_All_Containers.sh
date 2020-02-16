#!/bin/bash
#######################################################
function Catpump_Update_Service {
    sudo docker pull \
        pgoode41/catpump-update-service 
        
    sudo docker run \
        -d \
        --network="host" \
        --restart unless-stopped \
        pgoode41/catpump-update-service 
}
#######################################################
function Catpump_Ai_Detector {
    sudo docker pull \
        pgoode41/catpump-ai-detector

    sudo docker run \
        -d \
        -p 8095:8095  \
        --privileged \
        --restart unless-stopped \
        pgoode41/catpump-ai-detector
}
#######################################################
function Catpump_Api {
    sudo docker pull \
        pgoode41/catpump-api

    sudo docker run \
        -d \
        -p 8085:8085 \
        --privileged \
        --restart unless-stopped \
        pgoode41/catpump-api
}
#######################################################
function Catpump_Weight_Detector {
    sudo docker pull \
        pgoode41/catpump-weight-detector

    sudo docker run \
        -d \
        -p 8055:8055  \
        --privileged  \
        --restart unless-stopped \
        pgoode41/catpump-weight-detector
}
#######################################################
Catpump_Update_Service
Catpump_Api
Catpump_Weight_Detector
#sleep 60
Catpump_Ai_Detector