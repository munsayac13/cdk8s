from constructs import Construct
from cdk8s import App, Chart, Size
import os
import cdk8s_plus_32 as kplus

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
    current_directory = os.getcwd() + "/dist"
    with open(current_directory + "/valkey-primary-pv.k8s.yaml", "a") as file:
        file.write("  local:\n    path: /data/valkey-primary\n")
        file.write("  nodeAffinity:\n")
        file.write("    required:\n")
        file.write("      nodeSelectorTerms:\n")
        file.write("      - matchExpressions:\n")
        file.write("        - key: kubernetes.io/hostname\n")
        file.write("          operator: In\n")
        file.write("          values:\n")
        file.write("          - master-2\n")
        file.close()