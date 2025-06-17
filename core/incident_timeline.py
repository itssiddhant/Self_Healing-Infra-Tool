import os
from datetime import datetime

def generate_timeline(log_path="actions.log", output="incident_timeline.md"):
    if not os.path.exists(log_path):
        print("No actions.log file found.")
        return

    with open(log_path, "r") as f:
        lines = f.readlines()

    with open(output, "w") as f:
        f.write("#Incident Timeline Report\n\n")
        for line in lines:
            try:
                timestamp, event = line.strip().split("] ", 1)
                timestamp = timestamp.strip("[")
                dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                f.write(f"- ⏰ **{dt.strftime('%d %b %Y, %I:%M %p')}** → {event}\n")
            except Exception as e:
                f.write(f"- Malformed log line: {line.strip()}\n")

    print(f"Timeline written to {output}")

if __name__ == "__main__":
    generate_timeline()
