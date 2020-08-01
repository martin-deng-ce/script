# -*- coding:utf-8 -*-
# @Time:2020/7/28 11:29
# @Author:martin
# @File:emial.py.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_eamil(smtpserver, port, sender, psw, receiver):
    msg = MIMEMultipart()
    msg ['Subject'] = "这里是ssp项目自动化测试报告"
    msg ['from'] = sender
    msg ['to'] = receiver
# smtpserver = "smtp.qq.com"
# port = 465
# sender = "1637754392@qq.com"
# psw = "oercynjftapmbghb"
# receiver = "1637754392@qq.com"
# body = '<pre><h1>测试报告，请查收</h1></pre>'

    # msg = MIMEText(body, 'html', "utf-8")
    # msg['from'] = sender
    # msg['to'] = receiver
    # msg['subject'] = "这是自动化测试报告"

    current_path = os.getcwd()
    annex_path = os.path.join(current_path, "result.html")
    annex_path = open(annex_path, "r", encoding="utf-8").read()

    main_path = os.path.join(current_path,"text.html")
    main_body = open(main_path, "r", encoding="utf-8").read()

    body = MIMEText(main_body,"html","utf-8")
    msg.attach(body)

    att = MIMEText(annex, "base64", "utf-8")
    att["Content-type"] = "application/octet-sream"
    att["Content-Disposition"] = 'attachment;filename="ssp_test_report.html"'
    msg.attach(att)

    smtpl = smtplib.SMTP_SSL(smtpserver, port)
    smtpl.login(sender, psw)
    smtpl.sendmail(sender, receiver, msg.as_string())
    smtpl.quit()
# print("发送邮件成功！")
# smtplib.SMTPException
# print("error:抱歉！发送邮件失败。")
if __name__ == '__main__':
    send_eamil("smtp.qq.com", 465, "1637754392@qq.com","oercynjftapmbghb", "163754392@qq.com")
