#!/bin/bash

curl -sfL https://get.k3s.io | sh -

export KUBECONFIG='/etc/rancher/k3s/k3s.yaml'

k3s server --disable-network-policy