from constructs import Construct
from cdk8s import App, Chart, Helm
from imports import cert_manager as cm

class IMCertManager(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        name = "cert-manager"

        cm.Certmanager(self, id, release_name=name, namespace=name, values={
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