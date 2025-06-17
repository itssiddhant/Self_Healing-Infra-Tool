import smtplib
from email.message import EmailMessage

def send_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = 'infra-alerts@example.com'
    msg['To'] = to

    with smtplib.SMTP('localhost') as s:
        s.send_message(msg)

# Example usage:
# send_alert('Service Down', 'Restart triggered due to 500 error', 'you@example.com')
