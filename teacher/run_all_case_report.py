# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:37
# @Author:whweia
# @File:run_all_case_report.py
from commen import HTMLTestRunner
import unittest
# 加载指定目录下的所有用例


def all_case():
    case_dir = 'D:\\503\\script\\1223\\727\\case'  # 定义case的路径
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern="test*.py" # 执行以test开头的py文件
    )
    return discover

if __name__ == '__main__':
    report_dir = 'D:\\503\script\\1223\\727\\report\\report.html'
    fb = open(report_dir, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fb,
        title="自动化测试报告",
        description="自动化测试用例执行情况"

    )
    runner.run(all_case())  # 先执行全部用例
    fb.close()
