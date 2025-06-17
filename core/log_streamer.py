import time


def stream_logs(file_path):
    with open(file_path, "r") as file:
        file.seek(0, 2)  # Move to end of file
        while True:
            line = file.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()


if __name__ == "__main__":
    for log_line in stream_logs("../logs/mock_logs.json"):
        print(f"[LogStream] {log_line}")
