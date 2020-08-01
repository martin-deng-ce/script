# -*- coding:utf-8 -*-
# @Time:2020/7/29 11:02
# @Author:martin
# @File:all_case.py
import unittest
import os
def all_case():
    current_path = os.getcwd()
    print(current_path)
    case_path = os.path.join(current_path, "case")
    print(case_path)
    discover = unittest.defaultTestLoader.discover(
        case_path,
        pattern= "test*.py"
                                                   )
    return discover

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())
