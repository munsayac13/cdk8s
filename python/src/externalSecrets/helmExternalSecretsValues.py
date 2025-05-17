from constructs import Construct
from cdk8s import App, Chart, Helm
from imports import k8s

class HelmExternalSecretsValues(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        
        extsecnamespace = "external-secrets"

        k8s.KubeNamespace(self, extsecnamespace + "-namespace", metadata={
            'name': extsecnamespace,
            'labels': {
                'name': extsecnamespace,
            },
        })

        Helm(self, id, chart="external-secrets/external-secrets", version="0.14.1", values={
            'certController': {
                'create': True,
            },
            'crds': {
                'conversion': {
                    'enabled': True,
                },
                'createClusterExternalSecret': True,
                'createClusterSecretStore': True,
                'createPushSecret': True,
            },
            'createOperator': True,
            'installCRDs': True,
            'replicaCount': 1,
            'serviceMonitor': {
                'enabled': False
            }
        })