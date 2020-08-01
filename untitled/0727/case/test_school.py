# -*- coding:utf-8 -*-
# @Time:2020/7/29 18:10
# @Author:martin
# @File:test_school.py.py
from interface.school import School
from commen.Mysql import Mysqlhelp
import requests
s = requests.session()
import random
import unittest
import time
class Test_school(unittest.TestCase):
    def setUp(self):
    # def __init__(self):
        self.l = School(s)
        self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
        # self.school = School(self.s)
        self.m = Mysqlhelp()
    def test_add_success(self):
        name = random.randint(10, 100000)
        r = self.l.add(name).json()["code"]
        # return r
        self.assertEqual(r, 1)
        print("准备删除学校")
        time.sleep(1)
        print('开始删除学校')
        self.m.delete_data(name)

if __name__ == '__main__':
    unittest.main()
