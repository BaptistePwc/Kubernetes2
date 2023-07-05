#!/bin/bash

# Déploiement du Secret
kubectl apply -f my-secret-eval.yml

# Déploiement du Deployment
kubectl apply -f my-deployment-eval.yml

# Déploiement du Service
kubectl apply -f my-service-eval.yml

# Déploiement de l'Ingress
kubectl apply -f my-ingress-eval.yml

