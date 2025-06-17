import json
import re 
import yaml
from utils.logger import log_action


def load_logs():
    with open("../logs/mock_logs.json") as f:
        return json.load(f)


def load_patterns():
    with open("issue_patterns.yaml") as f:
        return yaml.safe_load(f)


def detect_issues(logs, patterns):
    matches = []
    for log in logs:
        for issue in patterns:
            if re.search(issue["pattern"], log["message"]):
                matches.append({"log": log, "action": issue["action"]})
    return matches


if __name__ == "__main__":
    logs = load_logs()
    patterns = load_patterns()
    results = detect_issues(logs, patterns)
    for r in results:
        print(f"Detected: {r['action']} on log: {r['log']['message']}")
        log_action(f"Detected issue: {r['action']} | Log: {r['log']['message']}")
