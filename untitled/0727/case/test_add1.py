# -*- coding:utf-8 -*-
# @Time:2020/7/27 16:30
# @Author:martin
# @File:test_add1.py.py
from interface.login1 import School
import requests
import random
import unittest
s = requests.session()
from commen.Mysql import Mysqlhelp
import time

class TestAdd(unittest.TestCase):
    def setUp(self):
    # def __init__(self):
        self.l = School(s)
        self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
        self.m =Mysqlhelp()

    def test_add_school_success(self):
        name = random.randint(10, 100000)
        r = self.l.add(name).text
        self.assertIn('学校创建成功', r)
        # return r
        print("准备删除学校")
        time.sleep(5)
        print("开始删除学校")
        self.m.delete_data(name)

    def test_add_school_name_error(self):
        name = random.randint(10, 100000)
        r = self.l.add("").text
        self.assertNotIn('学校创建成功', r)
        # return r
    def test_add_school_name_null(self):
        name = random.randint(10,100000)
        r = self.l.add("%").text
        self.asserNotIn("学校创建成功", r)


if __name__ == '__main__':
    unittest.main()
# if __name__ == '__main__':
#     t = Testadd()
#     r = t.test_add_school_success()
#     print(r.text)