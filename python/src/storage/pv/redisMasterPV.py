from constructs import Construct
from cdk8s import App, Chart, Size
#from imports import k8s
import os
import cdk8s_plus_32 as kplus
import appendPathAndNode as append

class RedisMasterPersistentVolume(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        # DOES NOT WORK
        #persistent_volume_spec = k8s.PersistentVolumeSpec(
        #    capacity={ "storage": "10Gi" },
        #    access_modes=["ReadWriteOnce"],
        #    persistent_volume_reclaim_policy="Retain",
        #    storage_class_name="local-storage",
        #    host_path=k8s.HostPathVolumeSource(path="/data/redis-master"),
        #)
        #object_meta = k8s.ObjectMeta(
        #    name="redis-master"
        #)
        #k8s.KubePersistentVolume(self, id, metadata=object_meta, spec=persistent_volume_spec)

        kplus.PersistentVolume(self, id, 
            metadata={ 'name': 'redis-master' },
            storage_class_name="local-storage",
            storage=Size.gibibytes(10),
            access_modes=[kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
            reclaim_policy=kplus.PersistentVolumeReclaimPolicy.RETAIN
        )
        
if __name__ == "__main__":
    app = App()
    RedisMasterPersistentVolume(app, "redis-master-pv")
    app.synth()
    append.AppendToPVFile("redis-master-pv.k8s.yaml", "/data/redis-master", "master-1")