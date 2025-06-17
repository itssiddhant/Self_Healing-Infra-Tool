import datetime

def generate_rca(issue_type, impact, root_cause, resolution, action_items):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"RCA_{issue_type.replace(' ', '_')}_{date_str}.md"
    with open(filename, "w") as f:
        f.write(f"# RCA Report – {issue_type}\n\n")
        f.write(f"**Date:** {datetime.datetime.now()}\n\n")
        f.write(f"**Impact:** {impact}\n\n")
        f.write(f"**Root Cause:** {root_cause}\n\n")
        f.write(f"**Resolution:** {resolution}\n\n")
        f.write("**Action Items:**\n")
        for item in action_items:
            f.write(f"- {item}\n")
    print(f"RCA saved to {filename}")

# Example usage
if __name__ == "__main__":
    generate_rca(
        issue_type="Disk Full",
        impact="Temporary outage on EFR App",
        root_cause="Unattended log growth on /var/log",
        resolution="Deleted logs and increased disk space",
        action_items=["Setup logrotate", "Add disk alert at 80%"]
    )
