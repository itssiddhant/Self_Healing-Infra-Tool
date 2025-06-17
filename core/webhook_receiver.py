from flask import Flask, request, jsonify
from pattern_resolver import load_config, resolve_action
from utils.logger import log_action

app = Flask(__name__)
CONFIG = load_config()


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    log_message = data.get("log")
    if not log_message:
        return jsonify({"error": "Missing 'log' in request"}), 400

    action = resolve_action(log_message, CONFIG)
    if action:
        return jsonify({"status": "triggered", "action": action}), 200
    else:
        return jsonify({"status": "ignored", "reason": "no match or not verified"}), 200


if __name__ == "__main__":
    app.run(port=5050)
