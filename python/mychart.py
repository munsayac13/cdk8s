from cdk8s import Chart, App
from imports import k8s
from constructs import Construct

class MyChart(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Define the PersistentVolume
        k8s.KubePersistentVolume(
            self,
            "my-persistent-volume",
            metadata=k8s.ObjectMeta(
                name="my-pv",
                labels={"app": "my-app"},
                annotations={"description": "This is a sample PersistentVolume"},
            ),
            spec=k8s.PersistentVolumeSpec(
                capacity={"storage": "10Gi"},
                access_modes=["ReadWriteOnce"],
                persistent_volume_reclaim_policy="Retain",
                storage_class_name="my-storage-class",
                host_path=k8s.HostPathVolumeSource(path="/mnt/data"),
                # You can add more properties to the spec here, like claimRef, etc.
            )
        )


app = App()
MyChart(app, "my-chart")
app.synth()