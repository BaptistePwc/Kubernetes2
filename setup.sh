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

#logs

kubectl get pods
kubectl get events
kubectl get ingress
kubectl describe configmap my-app-config
kubectl logs my-app-7c6f4fcbbb-8rmrd -c fastapi-container

#test
curl http://10.43.47.90:8000/users
curl http://10.43.47.90:8000/status