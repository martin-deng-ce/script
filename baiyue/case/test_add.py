# -*- coding:utf-8 -*-
# @Time:2020/7/29 10:08
# @Author:martin
# @File:test_add.py.py
from interface.login import Baiyue
import random
import requests
s = requests.session()
import unittest #引入框架

class Test_add(unittest.TestCase): #类
    def setUp(self):#前置条件
    # def __init__(self): #类的初始化
        self.b = Baiyue(s)
        self.b.login("byhy", "88888888")

    def test_add_success(self):
        name = random.randint(10, 100000)
        r = self.b.add(name).json()["ret"]
        self.assertEqual(r,0)
        # return r

    def test_add_name_error(self):
        name = random.randint(10, 100000)
        r = self.b.add("").json()["ret"]
        self.assertEqual(r, 0)
        # return r

    def test_add_name_null(self):
        name = random.randint(10, 100000)
        r = self.b.add(" ").json()["ret"]
        self.assertEqual(r, 0)
        # return r


if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     t = Test_add()
#     # r = t.test_add_success()
#     # r = t.test_add_name_error()
#     r = t.test_add_name_null()
#     print(r.text)



