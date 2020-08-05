# -*- coding:utf-8 -*-
# @Time:2020/7/27 15:33
# @Author:whweia
# @File:test_login.py
import unittest
from interface.school import School
import requests
s = requests.session()

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        self.l = School(s)

    def test_login_success(self):
        r = self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C").text
        self.assertIn("退出登录", r)

    def test_login_user_error(self):
        r = self.l.login("admin1", "660B8D2D5359FF6F94F8D3345698F88C").text
        self.assertNotIn("退出登录", r)


if __name__ == '__main__':
    unittest.main()
