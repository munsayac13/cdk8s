from constructs import Construct
from cdk8s import App, Chart, Size
import os
import cdk8s_plus_32 as kplus
import appendPathAndNode as append

class ValkeyPrimaryPersistentVolume(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        kplus.PersistentVolume(self, id, 
            metadata={ 'name': 'valkey-primary' },
            storage_class_name="local-storage",
            storage=Size.gibibytes(10),
            access_modes=[kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
            reclaim_policy=kplus.PersistentVolumeReclaimPolicy.RETAIN
        )
        
if __name__ == "__main__":
    app = App()
    ValkeyPrimaryPersistentVolume(app, "valkey-primary-pv")
    app.synth()
    append.AppendToPVFile("valkey-primary-pv.k8s.yaml", "/data/valkey-primary", "master-2")