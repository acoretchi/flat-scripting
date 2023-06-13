import smtplib
from email.message import EmailMessage
from typing import Dict, List


SEND_TO = [
    "armand.coretchi@gmail.com",
    # "laszlowheatley@gmail.com"
]
SERVER = "smtp.gmail.com"
USER = "armand.coretchi@gmail.com"
KEY = ""


def get_smtp_conn():
    server = smtplib.SMTP_SSL(SERVER, 465)
    server.login(USER, KEY)
    return server


def send_property_alert(properties: Dict[str, List[str]]):
    body = "NEW PROPERTIES:\n\n"
    for agency, links in properties.items():
        if len(links) > 0:
            body += f"{agency.upper()}: \n"
            for link in links:
                body += f" - {link}\n"

    msg = EmailMessage()
    msg["from"] = USER
    msg["bcc"] = SEND_TO
    msg["subject"] = "NEW PROPERTIES"
    msg.set_content(body)

    server = get_smtp_conn()
    server.send_message(msg)
    server.quit()
