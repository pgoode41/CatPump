#!/bin/bash

cd ${CATPUMPDIR}

go run fileserver.go&

python3 apiServer.py