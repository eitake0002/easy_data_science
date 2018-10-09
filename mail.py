#!/bin/env python3

import smtplib
from email.mime.text import MIMEText
import datetime
import traceback

FROM_MAIL = FROM_MAIL
TO_MAIL = TO_MAIL


def send_mail(subject='ERR', message):
    """Send mail function.

    Parameters
    ----------
    subject : str
    message : str

    Return
    ------
    bool
    """
    jp = 'iso-2022-jp'
    text_type = 'plain'
    msg = MIMEText(message.encode(jp), text_type, jp,)

    fromaddr = FROM_MAIL
    toaddr = TO_MAIL

    d = datetime.datetime.today()
    date = d.strftime("%Y-%m-%d")

    msg['Subject'] = subject
    msg['From'] = fromaddr
    msg['To'] = toaddr

    try:
        server = smtplib.SMTP("10.3.1.164", 25)
        server.send_message(msg)
        server.quit()

        print("Successfully sent email")
    except Exception:
        traceback.print_exc()


import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = MAIL_ADDRESS
MY_PASSWORD = PASSWORD
TO_ADDRESS = SEND_MAIL
BCC = BCC_MAIL_ADDRESS
SUBJECT = SUBJECT
BODY = BODY


def create_message(from_addr, to_addr, bcc_addrs, ubject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()
