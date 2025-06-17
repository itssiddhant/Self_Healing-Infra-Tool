import datetime

def log_action(action):
    with open('actions.log', 'a') as f:
        f.write(f"[{datetime.datetime.now()}] {action}\n")
