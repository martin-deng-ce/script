# -*- coding:utf-8 -*-
# @Time:2020/7/29 10:38
# @Author:martin
# @File:login1.py.py
from interface.login import Baiyue #导入文件
import requests
s = requests.session()
import unittest #引入框架

class Test_login(unittest.TestCase): #引入类
    def setUp(self):  #前置条件
    # def __init__(self): #类的初始化
        self.b = Baiyue(s)

    def test_login_success(self):
        r = self.b.login("byhy", "88888888").json()["ret"] #转字典获取key=values
        self.assertEqual(r,0)#断言

        # return r
    def test_login_name_error(self):
        r = self.b.login("", "88888888").json()["ret"]
        self.assertEqual(r,0)
        # return r

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     t = Test_login()
#     r = t.test_login_success()
#     # r = t.test_login_name_error()
#     print(r.text)

# if __name__ == '__main__':
#     unittest.main()
