from collections import defaultdict
import datetime

class AlertCorrelator:
    def __init__(self, time_window=60):
        self.time_window = time_window  # in seconds
        self.alerts = defaultdict(list)

    def add_alert(self, alert_type):
        now = datetime.datetime.now()
        self.alerts[alert_type] = [t for t in self.alerts[alert_type] if (now - t).seconds < self.time_window]
        self.alerts[alert_type].append(now)

    def is_spike(self, alert_type, threshold=3):
        return len(self.alerts[alert_type]) >= threshold

if __name__ == "__main__":
    ac = AlertCorrelator()
    ac.add_alert("ERROR 500")
    ac.add_alert("ERROR 500")
    ac.add_alert("ERROR 500")
    print("Spike:", ac.is_spike("ERROR 500"))
