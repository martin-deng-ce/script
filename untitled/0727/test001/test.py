# -*- coding:utf-8 -*-
# @Time:2020/7/28 12:19
# @Author:martin
# @File:test.py.py
# coding:utf-8
import smtplib
from email.mime.text import MIMEText

# 参数配置
smtpserver = "smtp.qq.com"  # 发送邮件的服务器
port = 465  # 端口
sender = "1637754392@qq.com"  # 发送的邮箱
psw = "oercynjftapmbghb"  # QQ授权码，这里填写上自己的授权码
receiver = "1637754392@qq.com"  # 接收邮件的邮箱

# 写信模板
body = '<pre><h1>测试报告，请查收`</h1></pre>'

msg = MIMEText(body, 'html', "utf-8")
msg['from'] = sender
msg['to'] = receiver
msg['subject'] = "这是自动化测试报告"  # 邮件的主题

# 写信流程
try:
    smtp1 = smtplib.SMTP_SSL(smtpserver, port)  # 实例化
    smtp1.login(sender, psw)  # 登录
    smtp1.sendmail(sender, receiver, msg.as_string())  # 配置发送邮箱，接收邮箱，以及发送内容
    smtp1.quit()  # 关闭发邮件服务
    print("邮件发送成功!")
except smtplib.SMTPException:
    print("Error: 抱歉！发送邮件失败。")