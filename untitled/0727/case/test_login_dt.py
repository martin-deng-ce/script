# -*- coding:utf-8 -*-
# @Time:2020/7/30 14:08
# @Author:martin
# @File:test_login_dt.py
from interface.school import School
import requests
import unittest
import ddt
s = requests.session()
data = [
    {"user":"admin", "psw":"660B8D2D5359FF6F94F8D3345698F88C","expect": True},
    {"user":"admin1","psw":"111111","expect": False,},
    # {"user":"admin2","psw":"222222","expect": False},
    # {"user":"admin3","psw":"xxxxxx","expect": False},
]

@ddt.ddt
class Test1(unittest.TestCase):
    def setUp(self):
        # self.s = requests.session()
        self.l = School(s)

    @ddt.data(*data)
    def test_login_success(self,testdata):
        print("本次测试数据:%s" % testdata)
        user = testdata["user"]
        psw = testdata["psw"]
        expect = testdata["expect"]
        result = self.l.login( user, psw).text
        if "退出登录" in result:
            i = True
        else:
            i = False



        self.assertEqual(i, expect)
        #实际结果
        # result = is_self.l.login_success(res)
        # #True的断言，实际结果= 期望结果
        # expect = testdata["expect"]
        # self.assertTrue(result==expect)

    # def tearDown(self):
    #     self.s.close()
if __name__ == '__main__':
    unittest.main()






    # def test_login_success(self):
    #     r = self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C").text
    #     # return r
    #     self.assertIn("退出登录", r)
    #
    # def tes_login_name_error(self):
    #     r = self.l.login("admin1", "660B8D2D5359FF6F94F8D3345698F88C").text
    #     # return r
    #     self.assertNotIn("退出登录", r)


# if __name__ == '__main__':
#     unittest.main()
