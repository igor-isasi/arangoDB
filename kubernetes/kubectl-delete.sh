#!/bin/bash

kubectl delete -f mi-deployment-cliente.yml
kubectl delete -f mi-cluster-ip-arangodb.yml
kubectl delete -f mi-deployment-arangodb.yml
kubectl delete -f mi-reclamacion-vp.yml