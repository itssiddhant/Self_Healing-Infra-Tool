import os
from utils.logger import log_action
from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Set environment variables for auth
subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
resource_group = os.getenv("AZURE_RESOURCE_GROUP")
vm_name = os.getenv("AZURE_VM_NAME")


def restart_vm():
    credential = DefaultAzureCredential()
    compute_client = ComputeManagementClient(credential, subscription_id)
    async_restart = compute_client.virtual_machines.begin_restart(resource_group, vm_name)
    async_restart.wait()
    print(f"VM '{vm_name}' restart initiated successfully.")
    log_action(f"Azure VM '{vm_name}' restarted via Self-Healing Tool")


if __name__ == "__main__":
    restart_vm()
