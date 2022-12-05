#!/bin/bash

kubectl apply -f mi-reclamacion-vp.yml
kubectl apply -f mi-deployment-arangodb.yml
kubectl apply -f mi-cluster-ip-arangodb.yml
kubectl apply -f mi-deployment-cliente.yml