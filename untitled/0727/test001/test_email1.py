# coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_eamil(smtpserver, port, sender, psw, receiver):
    msg = MIMEMultipart()
    msg ['Subject'] = "这里是ssp项目自动化测试报告"
    msg ['from'] = sender
    msg ['to'] = receiver




    # 通过os获取文件路径
    current_path = os.getcwd()  # 获取当前脚本所在的文件夹路径
    annex_path = os.path.join(current_path, "report.html")  # 附件内容的路径
    print(annex_path)
    annex = open(annex_path, "r", encoding="utf-8").read()

    main_path = os.path.join(current_path, "title.html")  # 正文内容的路径
    print(main_path)
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

if __name__ == '__main__':
    send_eamil("smtp.qq.com", 465, "1637754392@qq.com", "oercynjftapmbghb", "1637754392@qq.com")
