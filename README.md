# Self-Healing Infra Tool 🔧

A modular tool that detects known system failures from logs and remediates them using Power Automate or Azure Functions.

## 🚀 Features

- **Real-Time Log Monitoring** – Streams and detects known issues from logs dynamically.
- **Config-Driven Rules** – Easily add new issue patterns and remediations via YAML.
- **Verification Layer** – Smart checks prevent redundant or false remediation.
- **Webhook Support** – Accepts external alerts (Splunk, App Insights, etc.).
- **Automated Remediation** – Executes PowerShell/Bash scripts or Azure Functions.
- **RCA Generator** – Auto-creates Markdown RCA files from resolved issues.
- **Streamlit Dashboard** – Displays logs and remediations live.
- **Incident Timeline Generator** – Markdown timeline from `actions.log` for documentation.
- **GitHub Actions CI** – Linting + demo validation pipeline.


## Folder Structure
- `logs/`: sample and real logs
- `detection/`: log parser and issue patterns
- `remediation/`: scripts and Azure functions
- `alerts/`: email/Slack alerts
- `utils/`: logger and helper functions

## 🧪 Usage

1. Clone the repo:
```bash
git clone https://github.com/yourusername/SelfHealing-Infra-Tool.git
cd SelfHealing-Infra-Tool
```
2. Install Requirements:
```bash
pip install -r requirements.txt
```
3. Start Log Streaming:
```bash
python core/log_streamer.py
```
4. Run pattern resolver on logs:
```bash
python core/pattern_resolver.py
```
5. Trigger webhook listener:
```bash
python core/webhook_receiver.py
```
6. Generate RCA after remediation:
```bash
python alerts/rca_generator.py
```
7. View Dashboard:
```bash
streamlit run web/dashboard/streamlit_dashboard.py
```
