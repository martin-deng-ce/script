# -*- coding:utf-8 -*-
# @Time:2020/7/30 14:45
# @Author:martin
# @File:test_login_dt_excel.py
from interface.school import School
from commen.Excel_demo import Excelutil
import requests
import unittest
import ddt
s = requests.session()

filepath = "testdata.xlsx"
sheetName = "Sheet1"
# data= Excelutil(filepath,sheetName)
d = Excelutil(filepath,sheetName)
data = d.dict_data()
print(data)

# data = [
#     {"user":"admin", "psw":"660B8D2D5359FF6F94F8D3345698F88C","expect": True},
#     {"user":"admin1","psw":"111111","expect": False},
#     {"user":"admin2","psw":"222222","expect": False},
#     {"user":"admin3","psw":"xxxxxx","expect": False},
# ]

@ddt.ddt
class Test1(unittest.TestCase):
    def setUp(self):
        self.l = School(s)

    @ddt.data(*data)
    def test_0(self,testdata):
        print("本次测试数据:%s" %testdata)
        user = testdata["user"]
        psw = testdata["psw"]
        result = self.l.login(user, psw).text
        #实际结果
        if "退出登录"  in  result:
            i = True
        else:
            i = False


        #True的断言，实际结果= 期望结果
        expect = testdata["expect"]
        self.assertEqual(i,expect)

    # def tearDown(self):
    #     self.s.close()
if __name__ == '__main__':
    unittest.main()