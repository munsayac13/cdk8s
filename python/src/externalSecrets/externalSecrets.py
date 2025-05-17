from constructs import Construct
from cdk8s import App, Chart
from imports import k8s
#from helm.toolkit.fluxcd.io import HelmRelease, HelmReleaseSpecChartSpecSourceRefKind
#from source.toolkit.fluxcd.io import HelmRepository
from imports import external_secrets

class ExternalSecrets(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        
        extsecnamespace = id

        k8s.KubeNamespace(self, extsecnamespace + "-namespace", metadata={
            'name': extsecnamespace,
            'labels': {
                'name': extsecnamespace,
            },
        })

