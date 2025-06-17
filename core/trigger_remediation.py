import subprocess
from utils.logger import log_action

def restart_vm():
    log_action("Restarting VM via PowerShell script")
    subprocess.run(["powershell", "./remediation/scripts/restart_script.ps1"])

def clear_temp():
    log_action("Clearing temp logs via Bash script")
    subprocess.run(["bash", "./remediation/scripts/clear_disk_temp.sh"])

# Mapping action strings to function calls
ACTION_MAP = {
    "restart_vm": restart_vm,
    "clear_temp": clear_temp,
}

def trigger_action(action_name):
    if action_name in ACTION_MAP:
        ACTION_MAP[action_name]()
    else:
        log_action(f"Unknown action: {action_name}")

# Example usage
if __name__ == "__main__":
    trigger_action("restart_vm")
    trigger_action("clear_temp")
