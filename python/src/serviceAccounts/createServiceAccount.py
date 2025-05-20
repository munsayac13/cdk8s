from constructs import Construct
from cdk8s import App, Chart, Size
from imports import k8s
#import cdk8s_plus_32 as kplus

class CreateServiceAccountViewAccess(Chart):
    def __init__(self, scope: Construct, id: str, saNamespace: str):
        super().__init__(scope, id)

        saName = id
        saId = saName + '-serviceaccount'
        k8s.KubeServiceAccount(self, saId, metadata={
            'name': saName,
            'namespace': saNamespace
        })

        sId = saName + '-secret'
        k8s.KubeSecret(self, sId, type='kubernetes.io/service-account-token', metadata={
            'name': saName,
            'namespace': saNamespace,
            'annotations': {
                'kubernetes.io/service-account.name': saName
            }
        })

        clrbId = saName + '-clusterrolebinding'
        k8s.KubeClusterRoleBinding(self, clrbId, metadata={ 
            'name': saName 
        }, role_ref={
            'api_group': 'rbac.authorization.k8s.io',
            'kind' : 'ClusterRole',
            'name' : 'view'
        }, subjects=[{
            'kind': 'ServiceAccount',
            'name': saName,
            'namespace': saNamespace
        }])


class CreateServiceAccountClusterAdminAccess(Chart):
    def __init__(self, scope: Construct, id: str, saNamespace: str):
        super().__init__(scope, id)

        saName = id
        saId = saName + '-serviceaccount'
        k8s.KubeServiceAccount(self, saId, metadata={
            'name': saName,
            'namespace': saNamespace
        })

        sId = saName + '-secret'
        k8s.KubeSecret(self, sId, type='kubernetes.io/service-account-token', metadata={
            'name': saName,
            'namespace': saNamespace,
            'annotations': {
                'kubernetes.io/service-account.name': saName
            }
        })

        clrbId = saName + '-clusterrolebinding'
        k8s.KubeClusterRoleBinding(self, clrbId, metadata={ 
            'name': saName 
        }, role_ref={
            'api_group': 'rbac.authorization.k8s.io',
            'kind' : 'ClusterRole',
            'name' : 'cluster-admin'
        }, subjects=[{
            'kind': 'ServiceAccount',
            'name': saName,
            'namespace': saNamespace
        }])