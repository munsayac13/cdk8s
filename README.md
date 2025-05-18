# Install cdk8s-cli
npm install -g cdk8s-cli

# Initialize project - python
cdk8s init python-app

# Initialize project - typescript
cdk8s init typescript-app

# Initialize project - go
cdk8s init go-app

## IMPORT Charts
cdk8s import helm:oci://registry-1.docker.io/bitnamicharts/jenkins@13.6.6
cdk8s import helm:https://charts.jetstack.io/cert-manager@1.15.5
cdk8s import helm:https://charts.external-secrets.io/external-secrets@0.17.0
cdk8s import helm:https://fluxcd-community.github.io/helm-charts/flux2@2.15.0
cdk8s import helm:oci://registry-1.docker.io/bitnamicharts/valkey@3.0.6

## IMPORT CRDS
kubectl get crd -o yaml middlewares.traefik.io > middlewares.traefik.io.yaml
cdk8s import middlewares.traefik.io.yaml
cdk8s import certificates.cert-manager.io.yaml 

## Install cdk8s-plus-32 and cdk8s via pip3
pip3 install cdk8s-plus-32 cdk8s
OR
pipenv shell
pip3 install cdk8s-plus-32 cdk8s
