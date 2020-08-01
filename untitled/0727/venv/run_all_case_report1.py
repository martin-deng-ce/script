# -*- coding:utf-8 -*-
# @Time:2020/7/28 9:46
# @Author:martin
# @File:run_all_case1_report.py.py
from commen import HTMLTestRunner
# from commen import HTMLTestRunner
import unittest
import os
current_path = os.getcwd()
report1_path = os.path.join(current_path, 'report1')

def all_case():

    case_dir = os.path.join(current_path, 'case')
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern = "test*.py"
    )
    return discover



# current_path = os.getcwd()
# print(current_path)
# # print(os.dir.abspath(os.dir.dirname(os.getcwd())))
# case_path = os.path.join(current_path, 'case')
# report1_path = os.path.join(current_path, 'report1')
# print(report1_path)
# report1_html = os.path.join(current_path, 'report1_html')
# print(report1_html)









if __name__ == '__main__':
    pass
    # result_path = os.path.join(current_path, 'case')
    report1_html = os.path.join(current_path, 'report1_html')
    fb = open (report_html, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fb,
        title = "自动化测试报告",
        description = "自动化测试用例执行情况"
    )
    runner.run(all_case())
    fb.close