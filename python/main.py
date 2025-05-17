#!/usr/bin/env python
from constructs import Construct
from cdk8s import App, Chart, Size
from imports import k8s

import cdk8s_plus_32 as kplus

# apps
from src.externalSecrets.externalSecrets import ExternalSecrets
from src.redis.helmRedisValues import HelmRedisValues

# storage
from src.storage.storageClass.localStorage import LocalStorageClass
from src.storage.pv.redisMasterPV import RedisMasterPersistentVolume

#from src.storage.pv.justAnotherPV import JustAnotherPersistentVolume

app = App()

ExternalSecrets(app, "external-secrets")

# Persisten Volumes
LocalStorageClass(app, "local-storage-storageclass")
RedisMasterPersistentVolume(app, "redis-master-pv")
#JustAnotherPersistentVolume(app, "justanother-pv")

# Helm
HelmRedisValues(app, "redis-from-helm")

app.synth()
