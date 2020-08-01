# -*- coding:utf-8 -*-
# @Time:2020/7/30 17:35
# @Author:martin
# @File:test_login_ddt_excel.py
from interface.login import Baiyue #导入文件
import requests
s = requests.session()
import unittest #引入框架
import ddt
from  commen.Excel_demo import Excelutil

# filepath = "testdata.xlsx"
filepath = 'E:\\script\\baiyue\\case\\testdata.xlsx'
sheetName = "Sheet1"
d = Excelutil(filepath,sheetName)
data = d.dict_data()
# print(data)

@ddt.ddt
class Test_login(unittest.TestCase): #引入类
    def setUp(self):  #前置条件
    # def __init__(self): #类的初始化
        self.b = Baiyue(s)
    @ddt.data(*data)
    def test_login_success(self,testdata):
        # print(testdata)
        user = testdata["user"]
        pwd = testdata["pwd"]
        expect = testdata["expect"]
        # print(expect)
        result = self.b.login(user, pwd).json()["ret"]
        res = int(expect)
        self.assertEqual(result, res)
        # self.assertEqual(result,expect)

    # def test_login_success(self):
    #     r = self.b.login("byhy", "88888888").json()["ret"] #转字典获取key=values
    #     self.assertEqual(r,0)#断言
    #
    #     # return r
    # def test_login_name_error(self):
    #     r = self.b.login("", "88888888").json()["ret"]
    #     self.assertEqual(r,0)
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