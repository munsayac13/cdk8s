from cdk8s import App, Chart, Size
from constructs import Construct
from cdk8s_plus_32 import PersistentVolume, PersistentVolumeAccessMode

class JustAnotherPersistentVolume(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        PersistentVolume(
            self,
            id,
            access_modes=[PersistentVolumeAccessMode.READ_WRITE_ONCE],
            capacity=Size.gibibytes(32),
            local_path="/mnt/data"
        )