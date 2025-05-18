from constructs import Construct
from cdk8s import App, Chart, Helm
from imports import valkey as v

class IMValkey(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        vPrimary = v.ValkeyPrimary(additional_values={
            'nodeSelector': {
                'kubernetes.io/hostname': 'master-2'
            },
            'persistence': {
                'storageClass': 'local-storage',
                'size': '10Gi'
            }
        })
        vReplicas = v.ValkeyReplica(additional_values={
            'replicaCount': 0,
            'persistence': {
                'storageClass': 'local-storage',
                'size': '10Gi'
            }
        })
        vValues = v.ValkeyValues(primary=vPrimary, replica=vReplicas)
        v.Valkey(self, id, values=vValues)

