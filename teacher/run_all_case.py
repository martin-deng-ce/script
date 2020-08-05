# -*- coding:utf-8 -*-
# @Time:2020/7/27 15:32
# @Author:whweia
# @File:run_all_case.py
import unittest
# 加载指定目录下的所有用例


def all_case():
    case_dir = 'D:\\503\\script\\1223\\727\\case'  # 定义case的路径
    discover = unittest.defaultTestLoader.discover(
        case_dir,
        pattern="test*.py" # 执行以test开头的py文件
    )
    return discover


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(all_case())

