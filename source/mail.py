import os
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail(to, subject, body):
    ID = 'c.yuze.sys24@morijyobi.ac.jp'
    PASS = os.environ['MAIL_PASS']
    HOST = 'smtp.gmail.com'
    PORT = 587
    
    msg = MIMEMultipart()
    
    msg.attach(MIMEText(body, 'html'))
    
    msg['Subject'] = subject
    msg['From'] = ID
    msg['To'] = to
    # msg['Cc'] = cc
    # msg['Bcc'] = bcc
    
    # file_name = os.path.basename(file_path)
    # f = open(file_path, 'rb')
    # attachment = MIMEApplication(f.read(), Name=file_name)
    # attachment.add_header('Content-Disposition', 'attachment', filename=file_name)
    # f.close()
    # msg.attach(attachment)
    
    # ここから送信処理
    server = SMTP(HOST, PORT)
    server.starttls()
    server.login(ID, PASS)
    
    server.send_message(msg)
    server.quit()