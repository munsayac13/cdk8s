from constructs import Construct
from cdk8s import App, Chart, Helm
import cdk8s_plus_32 as kplus

class HelmCertManagerValues(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        Helm(self, id, chart="cert-manager/cert-manager", version="v1.17.2", values={
            "crds": {
                "enabled": True,
                "keep": True
            },
            "enabled": True,
            "namespace": "cert-manager",
            "nodeSelector": {
                "kubernetes.io/hostname": "master-1"
            },
            "prometheus": {
                "enabled": False,
                "podmonitor": {
                    "enabled": True
                },
                "servicemonitor": {
                    "enabled": True
                }
            },
            "replicaCount": 0,
            "resources": {
                "limits": {
                    "cpu": "500m",
                    "memory": "512Mi"
                },
                "requests": {
                    "cpu": "32m",
                    "memory": "32Mi"
                }
            }
        })
             