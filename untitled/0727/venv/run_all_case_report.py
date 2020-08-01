# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:21
# @Author:martin
# @File:run_all_case.py.py
from commen import HTMLTestRunner
# from commen import HTMLTestRunner
import unittest


def all_case():

    case_dir = 'E:\\script\\untitled\\0727\\case'#定义路径
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern = "test*.py"
    )
    return discover


if __name__ == '__main__':
    pass
    report_dir = 'E:\\script\\untitled\\0727\\report\\report.html'
    fb = open (report_dir, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fb,
        title = "自动化测试报告",
        description = "自动化测试用例执行情况"
    )
    runner.run(all_case())
    fb.close