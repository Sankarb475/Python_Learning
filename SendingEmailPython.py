# sending email using Python

import smtplib
from datetime import datetime
from glob import glob
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import time


def sendmail(htmltext, subject, from_address, to_address):

    print("I AM INSIDE sendmail method")

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = (', ').join(to_address.split(','))
    # msg['To'] = to_address
    # Define alternative plaintext
    ptmsg = MIMEMultipart('alternative')
    msg.attach(ptmsg)
    ptmsg.attach(
        MIMEText(
            "\nSending Message using Python.\n "
            , 'text'))
    # Define HTML Message
    HTMLText = MIMEText(htmltext, 'html')
    # Attach HTML
    ptmsg.attach(HTMLText)
    s = smtplib.SMTP('localhost')
    s.sendmail(from_address, to_address, msg.as_string())

e = "This is what we need to print"
htmltext = "<tr><td class='r'>{0}</tr>\n".format(e)

from_address = "sankarb475@gmail.com"
to_address = "sankarb475@gmail.com"
subject = "email using python"

sendmail(htmltext,subject,from_address,to_address)

