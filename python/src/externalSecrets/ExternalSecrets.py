from constructs import Construct
from cdk8s import App, Chart, Helm
from imports import k8s
from imports import external_secrets as es

class IMExternalSecrets(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        #esAffinity = es.ExternalSecretsAffinity(additional_values={
        #    'podAntiAffinity': {
        #        'requiredDuringSchedulingIgnoredDuringExecution': [{
        #            'labelSelector': {
        #                'matchLabels': {
        #                    'app.kubernetes.io/name': 'external-secrets-cert-controller'
        #                }
        #            },
        #            'topologyKey': 'kubernetes.io/hostname'
        #        }]
        #    },
        #    'nodeAffinity': {
        #        'requiredDuringSchedulingIgnoredDuringExecution': {
        #            'nodeSelectorTerms': [{
        #                'matchExpressions': [{
        #                    'key': 'doks.digitalocean.com/node-pool',
        #                    'operator': 'In', 
        #                    'values': [
        #                        'master-1'
        #                    ]
        #                }]
        #            }]
        #        }
        #    }
        #})

        esCrds = es.ExternalSecretsCrds(
            conversion={ 'enabled': True }, 
            create_cluster_external_secret=True, 
            create_cluster_secret_store=True,
            create_push_secret=True
        )

        esServiceMonitor = es.ExternalSecretsServiceMonitor(enabled=False)
        esServiceAccount = es.ExternalSecretsServiceAccount(automount=True, create=True)

        #esValues = es.ExternalsecretsValues(affinity=esAffinity, crds=esCrds, service_monitor=esServiceMonitor, service_account=esServiceAccount)
        esValues = es.ExternalsecretsValues(crds=esCrds, service_monitor=esServiceMonitor, service_account=esServiceAccount)
        es.Externalsecrets(self, id, release_name="external-secrets", values=esValues)