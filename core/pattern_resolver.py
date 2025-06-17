import yaml
import re
import sys
import os
from state_checker import is_vm_running, is_disk_full
from utils.logger import log_action
from trigger_remediation import trigger_action

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def load_config(config_path="./config/issue_config.yaml"):
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def resolve_action(log_message, config):
    for rule in config["alerts"]:
        if re.search(rule["pattern"], log_message):
            if rule["verify"] == "is_vm_running" and is_vm_running("localhost"):
                log_action("Skip: VM already running")
                return
            if rule["verify"] == "is_disk_full" and not is_disk_full(85):
                log_action("Skip: Disk space OK")
                return
            log_action(f"Trigger: {rule['action']} for rule: {rule['name']}")
            trigger_action("restart_vm")
            return rule["action"]
    return None


# Example use case
if __name__ == "__main__":
    sample_log = "disk full on /var/log"
    config = load_config()
    resolve_action(sample_log, config)
