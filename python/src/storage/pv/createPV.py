from constructs import Construct
from cdk8s import App, Chart, Size
import os
import cdk8s_plus_32 as kplus


class CreatePersistentVolume(Chart):
    def __init__(self, scope: Construct, id: str, name: str, storageclass: str, storagesize: int):
        super().__init__(scope, id)
        self.name = name
        self.storageclass = storageclass
        self.storagesize = storagesize

        kplus.PersistentVolume(self, id, 
            metadata={ 'name': name },
            storage_class_name=storageclass,
            storage=Size.gibibytes(storagesize),
            access_modes=[kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE],
            reclaim_policy=kplus.PersistentVolumeReclaimPolicy.RETAIN
        )
        
if __name__ == "__main__":
    import appendPathAndNode as append
    app = App()

    CreatePersistentVolume(app, "valkey-primary-pv", "valkey-primary", "local-storage", 10)
    CreatePersistentVolume(app, "vault-pv", "vault", "local-storage", 10)
    CreatePersistentVolume(app, "redis-master-pv", "redis-master", "local-storage", 10)
    CreatePersistentVolume(app, "zookeeper-pv", "zookeeper", "local-storage", 10)
    CreatePersistentVolume(app, "kafka-controller-0-pv", "kafka-controller-0", "local-storage", 10)
    CreatePersistentVolume(app, "kafka-controller-1-pv", "kafka-controller-1", "local-storage", 10)
    CreatePersistentVolume(app, "kafka-controller-2-pv", "kafka-controller-2", "local-storage", 10)
    CreatePersistentVolume(app, "kafka-broker-0-pv", "kafka-broker-0", "local-storage", 10)
    CreatePersistentVolume(app, "kafka-broker-1-pv", "kafka-broker-1", "local-storage", 10)
    CreatePersistentVolume(app, "kafka-broker-2-pv", "kafka-broker-2", "local-storage", 10)

    app.synth()
    append.AppendToPVFile("kafka-controller-0-pv.k8s.yaml", "/data/kafka/controller", "master-1")
    append.AppendToPVFile("kafka-controller-1-pv.k8s.yaml", "/data/kafka/controller", "master-2")
    append.AppendToPVFile("kafka-controller-2-pv.k8s.yaml", "/data/kafka/controller", "master-3")
    append.AppendToPVFile("kafka-broker-0-pv.k8s.yaml", "/data/kafka/broker", "master-1")
    append.AppendToPVFile("kafka-broker-1-pv.k8s.yaml", "/data/kafka/broker", "master-2")
    append.AppendToPVFile("kafka-broker-2-pv.k8s.yaml", "/data/kafka/broker", "master-3")
    append.AppendToPVFile("valkey-primary-pv.k8s.yaml", "/data/valkey-primary", "master-2")
    append.AppendToPVFile("vault-pv.k8s.yaml", "/data/vault", "master-1")
    append.AppendToPVFile("redis-master-pv.k8s.yaml", "/data/redis-master", "master-1")
    append.AppendToPVFile("zookeeper-pv.k8s.yaml", "/data/zookeeper", "master-2")