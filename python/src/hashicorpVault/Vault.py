from constructs import Construct
from cdk8s import App, Chart, Helm
from imports import vault as v

class IMVault(Chart):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        #vVaultServerDataStorage = v.VaultServerDataStorage(
        #    access_mode="ReadWriteOnce", 
        #    enabled=True, 
        #    mount_path="/vault/data", 
        #    size="10Gi",
        #    storage_class="local-storage"
        #)      
        #vVaultServer = v.VaultServer(data_storage=vVaultServerDataStorage)
        #vVaultUI = v.VaultUi(enabled=True, external_port=8200, service_type="ClusterIP", target_port=8200)
        
        v.Vault(self, id, release_name="vault", values={
            'server': {
                'data_storage': {
                    'access_mode': 'ReadWriteOnce', 
                    'enabled': True, 
                    'mount_path': '/vault/data', 
                    'size': '10Gi', 
                    'storage_class': 'local-storage'
                }
            }, 
            'ui': {
                'enabled': True, 
                'external_port': 8200, 
                'service_type': 'ClusterIP', 
                'target_port': 8200
            }
        })

if __name__ == "__main__":
    app = App()
    IMVault(app, "vault-from-imports")
    app.synth()    