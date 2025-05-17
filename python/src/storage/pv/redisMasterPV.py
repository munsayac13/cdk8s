from constructs import Construct
from cdk8s import App, Chart, Size
#from imports import k8s
import os

import cdk8s_plus_32 as kplus
#import cdk8s_plus_31 as kplus


class RedisMasterPersistentVolume(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        kplus.PersistentVolume(self, id, 
            metadata={ 'name': 'redis-master' },
            storage_class_name="local-storage",
            storage=Size.gibibytes(10),
            access_modes=[kplus.PersistentVolumeAccessMode.READ_WRITE_ONCE]
        )
        
if __name__ == "__main__":
    app = App()
    RedisMasterPersistentVolume(app, "redis-master-pv")
    app.synth()
    current_directory = os.getcwd() + "/dist"
    with open(current_directory + "/redis-master-pv.k8s.yaml", "a") as file:
        file.write("  local:\n    path: /data/redis-master\n")
        file.write("  nodeAffinity:\n")
        file.write("    required:\n")
        file.write("      nodeSelectorTerms:\n")
        file.write("      - matchExpressions:\n")
        file.write("        - key: kubernetes.io/hostname\n")
        file.write("          operator: In\n")
        file.write("          values:\n")
        file.write("          - master-1\n")
        file.close()
#PersistentVolume(
#    chart,
#    "MyPersistentVolume",
#    access_modes=[AccessMode.READ_WRITE_ONCE],
#    capacity=Size.gibibytes(10),
#    storage_class_name="my-storage-class",
#    host_path="/mnt/data"
#)

#app.synth()