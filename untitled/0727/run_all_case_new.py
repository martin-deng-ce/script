# -*- coding:utf-8 -*-
# @Time:2020/7/28 16:04
# @Author:martin
# @File:run_all_case_new.py.py

import unittest # 引入框架
from commen import HTMLTestRunner  # 生成测试报告
import os
#写邮件
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class Run_all(object):
    def __init__(self):
        self.current_path = os.getcwd() #当前文件路径
        self.report_path = os.path.join(self.current_path, "report")  #测试报告的路径
        self.result_path = os.path.join(self.report_path, "result.html") #
        self.case_path = os.path.join(self.current_path, "case") #用例的路径

    def all_case(self):#运行case目录下所有以test开头的文件


        discover = unittest.defaultTestLoader.discover(
            self.case_path,
            pattern= "test*.py"
        )
        return discover

    def case_report(self):#运行测试用例生成的报告
        fb = open(self.result_path, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream = fb,
            title = "自动化测试报告",
            description = "自动化测试用例执行情况"

        )
        runner.run(self.all_case())
        fb.close()

    def send_email(self, smtpserver, port, sender,psw,receiver):#封装邮件
        #邮件模板
        msg = MIMEMultipart()
        msg['Subject'] = "项目自动化测试报告"
        msg['from'] = sender
        msg['to'] = receiver
           #通过os获取文件路径
        annex = open(self.result_path, "r", encoding= "utf-8").read()

        main_body = '<pre><h1>这是XX项目的接口自动化测试报告，请查阅！自动发送的邮件，不用回复。' \
                    '<br />联系人：<br />xxx   研发部' \
                    '<br />联系电话：15768115596<br />邮箱地址：martin@163.com<br />' \
                    '联系地址：深圳市南山区科技园南路1001号<br /></h1></pre>'  # 正文的内容
        body = MIMEText(main_body, "html", "utf-8")
        msg.attach(body)
         #添加容器
        att = MIMEText(annex, "base64", "utf-8")
        att["Content-type"] = "application/octet-sream"
        att["Content-Disposition"] = 'attachment;filename="ssp_test_report.html"'
        msg.attach(att)
        #链接邮件发送
        try:
            smtpl = smtplib.SMTP_SSL(smtpserver, port)
            smtpl.login(sender, psw)
            smtpl.sendmail(sender, receiver, msg.as_string())
            smtpl.quit()
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 抱歉！发送邮件失败。")

if __name__ == '__main__':
    r = Run_all()
    r.case_report()
    r.send_email("smtp.qq.com", 465, "1637754392@qq.com", "oercynjftapmbghb", "1637754392@qq.com")