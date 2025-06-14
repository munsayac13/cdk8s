#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart, Size
from imports import k8s

import cdk8s_plus_32 as kplus

# apps
from src.externalSecrets.helmExternalSecretsValues import HelmExternalSecretsValues
from src.redis.helmRedisValues import HelmRedisValues
from src.certManager.helmCertManagerValues import HelmCertManagerValues

from src.externalSecrets.ExternalSecrets import IMExternalSecrets
from src.certManager.CertManager import IMCertManager
from src.redis.Valkey import IMValkey
from src.hashicorpVault.Vault import IMVault

# storage
from src.storage.pv.createPV import CreatePersistentVolume
from src.storage.storageClass.localStorage import LocalStorageClass
#from src.storage.pv.justAnotherPV import JustAnotherPersistentVolume


# service accounts
from src.serviceAccounts.createServiceAccount import CreateServiceAccountViewAccess, CreateServiceAccountClusterAdminAccess, CreateServiceAccountViewPodsAndServicesOnly

app = App()

# Persisten Volumes
LocalStorageClass(app, "local-storage-storageclass")
#JustAnotherPersistentVolume(app, "justanother-pv")

CreatePersistentVolume(app, "valkey-primary-pv", "valkey-primary", "local-storage", 10)
CreatePersistentVolume(app, "vault-pv", "vault", "local-storage", 10)
CreatePersistentVolume(app, "kafka-controller-pv", "kafka-controller", "local-storage", 10)
CreatePersistentVolume(app, "redis-master-pv", "redis-master", "local-storage", 10)

# Helm and Deployments
HelmExternalSecretsValues(app, "external-secrets-from-helm")
HelmRedisValues(app, "redis-from-helm")
HelmCertManagerValues(app, "cert-manager-from-helm")

# Imported Apps
IMExternalSecrets(app, "external-secrets-from-imports")
IMCertManager(app, "cert-manager-from-imports")
IMValkey(app, "valkey-from-imports")
IMVault(app, "vault-from-imports")

# Service Accounts
CreateServiceAccountViewAccess(app, 'nodelocal-ro', 'default')
CreateServiceAccountClusterAdminAccess(app, 'nodelocal-admin', 'default')
CreateServiceAccountViewPodsAndServicesOnly(app, 'nodelocal-ro-pods-services-only', 'default')

app.synth()
