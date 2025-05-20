from constructs import Construct
from cdk8s import App, Chart, Size
from imports import k8s
#import cdk8s_plus_32 as kplus

# Note: To create kubeconfig, 
# check https://medium.com/@atifjaved02/create-kubeconfig-for-your-cluster-with-limited-read-access-1be574241c8c


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

class CreateServiceAccountViewPodsAndServicesOnly(Chart):
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

        clrId = saName + '-clusterrole'
        k8s.KubeClusterRole(self, clrId, metadata={
            'name': saName
        }, rules=[{
            'apiGroups': [''], 
            'resources': ['pods', 'services'], 
            'verbs': ['get', 'list', 'watch']
        }, {
            'apiGroups': ['apps'], 
            'resources': ['deployments', 'replicasets', 'statefulsets'], 
            'verbs': ['get', 'list', 'watch']
        }])

        clrbId = saName + '-clusterrolebinding'
        k8s.KubeClusterRoleBinding(self, clrbId, metadata={ 
            'name': saName 
        }, role_ref={
            'api_group': 'rbac.authorization.k8s.io',
            'kind' : 'ClusterRole',
            'name' : saName
        }, subjects=[{
            'kind': 'ServiceAccount',
            'name': saName,
            'namespace': saNamespace
        }])        