#!/bin/env python3

import smtplib
from email.mime.text import MIMEText
import datetime
import traceback

FROM_MAIL = "mailto:noreply@occ-manager.com"
TO_MAIL = "eiki.takeuchi@oracle.com"


def send_mail(subject='ERR', message):
    """
    メール通知の関数です。

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


if __name__ == '__main__':
    subject = "[System Backup] <関数名> <引数（VMインスタンス名、スナップショット名など）>"
    send_mail(subject, "Test Message")
