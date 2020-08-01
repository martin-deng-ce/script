# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:21
# @Author:martin
# @File:run_all_case.py.py
import unittest


def all_case():
    # E:\script\untitled\0727\case
    case_dir = 'E:\\script\\untitled\\0727\\case'
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern= "test*.py"
    )
    return discover


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_case())
