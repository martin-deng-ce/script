# -*- coding:utf-8 -*-
# @Time:2020/7/30 12:06
# @Author:martin
# @File:ddt.py
import requests
import unittest
import ddt
data = [
    {"user":"admin1","psw":"111111","expect": True},
    {"user":"admin2","psw":"222222","expect": True},
    {"user":"admin3","psw":"xxxxxx","expect": False},
]

@ddt.ddt
class Testl(unittest.TestCase):

    @ddt.data(*data)
    def test_01(self,testdata):
        print(testdata)

if __name__ == '__main__':
    unittest.main()
