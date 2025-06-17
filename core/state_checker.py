import subprocess

def is_vm_running(vm_name: str) -> bool:
    """Simulated system status check. Replace with real cloud or CLI status check."""
    try:
        result = subprocess.run(["ping", "-c", "1", vm_name], capture_output=True)
        return result.returncode == 0
    except Exception:
        return False

def is_disk_full(threshold_percent=90) -> bool:
    """Check disk usage on Unix-like systems."""
    try:
        result = subprocess.run(["df", "--output=pcent", "/"], capture_output=True, text=True)
        percent_str = result.stdout.strip().split("\n")[1].replace("%", "").strip()
        return int(percent_str) >= threshold_percent
    except Exception:
        return False

# Example usage
if __name__ == "__main__":
    if is_vm_running("localhost"):
        print("VM is already running.")
    else:
        print("VM needs restart.")

    if is_disk_full(85):
        print("Disk is nearly full. Clean-up needed.")
    else:
        print("Disk space OK.")
