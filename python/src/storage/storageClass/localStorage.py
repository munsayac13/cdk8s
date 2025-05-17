from constructs import Construct
from cdk8s import App, Chart
from imports import k8s

class LocalStorageClass(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        k8s.KubeStorageClass(self, id, metadata=k8s.ObjectMeta(
            name="local-storage",
            annotations={
                "storageclass.kubernetes.io/is-default-class": "true"
            }
        ),
        provisioner="kubernetes.io/no-provisioner", 
        volume_binding_mode="WaitForFirstConsumer")
        #k8s.KubeStorageClass(self, id, metadata={
        #    'name': "local-storage"
        #}, provisioner="kubernetes.io/no-provisioner", volume_binding_mode="WaitForFirstConsumer")

