from constructs import Construct
from cdk8s import App, Chart, Helm
import cdk8s_plus_32 as kplus

class HelmRedisValues(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        Helm(self, id, chart="bitnami/redis", version="21.1.3", values={
            "master": {
                "nodeSelector": {
                    "kubernetes.io/hostname" : "master-1"
                },
                "persistence": {
                    "storageClass": "local-storage",
                    "size": "10Gi"
                }
            },
            "metrics": {
                "enabled": True,
                "livenessProbe": {
                    "enabled": True
                }
            },
            "replica": {
                "replicaCount": 0,
                "persistence": {
                    "storageClass": "local-storage",
                    "size": "10Gi"
                }
            }
        })
             