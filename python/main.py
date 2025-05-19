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
from src.storage.storageClass.localStorage import LocalStorageClass
from src.storage.pv.redisMasterPV import RedisMasterPersistentVolume
from src.storage.pv.valkeyPrimaryPV import ValkeyPrimaryPersistentVolume


#from src.storage.pv.justAnotherPV import JustAnotherPersistentVolume

app = App()

# Persisten Volumes
LocalStorageClass(app, "local-storage-storageclass")
RedisMasterPersistentVolume(app, "redis-master-pv")
#JustAnotherPersistentVolume(app, "justanother-pv")

# Helm and Deployments
HelmExternalSecretsValues(app, "external-secrets-from-helm")
HelmRedisValues(app, "redis-from-helm")
HelmCertManagerValues(app, "cert-manager-from-helm")

# Imported Apps
IMExternalSecrets(app, "external-secrets-from-imports")
IMCertManager(app, "cert-manager-from-imports")
IMValkey(app, "valkey-from-imports")
IMVault(app, "vault-from-imports")

app.synth()
