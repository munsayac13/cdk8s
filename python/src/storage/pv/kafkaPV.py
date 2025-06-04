from constructs import Construct
from cdk8s import App, Chart, Size
import os
import cdk8s_plus_32 as kplus


class KafkaControllerPersistentVolume(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        kplus.PersistentVolume(self, id, 
            metadata={ 'name': 'kafka-controller' },
            storage_class_name="local-storage",
            storage=Size.gibibytes(10),
            access_modes=[kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
            reclaim_policy=kplus.PersistentVolumeReclaimPolicy.RETAIN
        )
        
if __name__ == "__main__":
    import appendPathAndNode as append
    app = App()
    KafkaControllerPersistentVolume(app, "kafka-controller-pv")
    app.synth()
    append.AppendToPVFile("kafka-controller-pv.k8s.yaml", "/data/kafka-controller", "master-2")
