#!/bin/bash
#requirement
pip install -r requirements.txt
#Secret
kubectl apply -f my-secret-eval.yml

#Deployment
kubectl apply -f my-deployment-eval.yml

# Service
kubectl apply -f my-service-eval.yml

# Ingress
kubectl apply -f my-ingress-eval.yml

