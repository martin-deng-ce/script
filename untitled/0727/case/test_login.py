# -*- coding:utf-8 -*-
# @Time:2020/7/27 17:00
# @Author:martin
# @File:test_login.py.py
from interface.login1 import School
import requests
import unittest
s = requests.session()


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.l = School(s)

    def test_login_success(self):
        r = self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C").text
        # return r
        self.assertIn("退出登录", r)

    def tes_login_name_error(self):
        r = self.l.login("admin1", "660B8D2D5359FF6F94F8D3345698F88C").text
        # return r
        self.assertNotIn("退出登录", r)


if __name__ == '__main__':
    unittest.main()
