# -*- coding:utf-8 -*-
"""
"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    f = open(newfile, 'rb')
    mail_body = f.read()
    f.close()

    smtpserver = 'smtp.qq.com'
    user = '920100886@qq.com'
    password = 'rjlxvpppnaecbfhb'
    sender = '920100886@qq.com'
    receiver = ['xiangyb@tigerft.com']

    subject = '自动化测试报告 ' + str(time.strftime("%Y%m%d %H:%M:%S", time.localtime()))
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    msg['From'] = 'xiangyb@tigerft.com <xiangyb@tigerft.com>'
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
