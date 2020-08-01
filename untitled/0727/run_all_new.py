from commen import HTMLTestRunner
# from commen import HTMLTestRunner
import unittest
import os
c = os.getcwd()
report = os.path.join(c, 'report')

def all_case():

    case_dir = os.path.join(c, 'case')
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern = "test*.py"
    )
    return discover


if __name__ == '__main__':
    report_dir = os.path.join(report, 'report.html')
    fb = open (report_dir, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = fb,
        title = "自动化测试报告",
        description = "自动化测试用例执行情况"
    )
    runner.run(all_case())
    fb.close