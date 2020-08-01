# -*- coding:utf-8 -*-
# @Time:2020/7/30 17:01
# @Author:martin
# @File:test_phone_dt_excel.py
from test_string.phone import Phone
from commen.Excel_demo import Excelutil
import requests
import unittest
import ddt
import json
filepath = "testdata.xlsx"
sheetName = "Sheet1"
# data= Excelutil(filepath,sheetName)
d = Excelutil(filepath,sheetName)
data = d.dict_data()
print(data)


# data = [
#     {"phone":"13979296069","key":"63a77489d2c51d26b4031e344b4f0050","expect":"200"},
#     {"phone":"","key":"63a77489d2c51d26b4031e344b4f0050","expect":"201"},
#     {"phone":"13979296069","key":"","expect":"101"},
# ]

@ddt.ddt
class Test_phone(unittest.TestCase):
    # def __init__(self):
    def setUp(self):
        self.p = Phone()
    @ddt.data(*data)
    def test_phone_location_success(self,testdata):
        print(testdata)
        phone = testdata["phone"]
        key = testdata["key"]
        expect = testdata["expect"]
        result =self.p.phone_location(phone,key).json()["resultcode"]
        self.assertEqual(result,expect)


if __name__ == '__main__':
    unittest.main()