import json, re, yaml

def load_logs():
    with open('../logs/mock_logs.json') as f:
        return json.load(f)

def load_patterns():
    with open('issue_patterns.yaml') as f:
        return yaml.safe_load(f)

def detect_issues(logs, patterns):
    matches = []
    for log in logs:
        for issue in patterns:
            if re.search(issue['pattern'], log['message']):
                matches.append({'log': log, 'action': issue['action']})
    return matches

if __name__ == '__main__':
    logs = load_logs()
    patterns = load_patterns()
    results = detect_issues(logs, patterns)
    for r in results:
        print(f"Detected: {r['action']} on log: {r['log']['message']}")
