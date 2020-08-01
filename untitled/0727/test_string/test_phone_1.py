# -*- coding:utf-8 -*-
# @Time:2020/7/30 16:01
# @Author:martin
# @File:test_phone_1.py
from test_string.phone import Phone
import requests
import unittest
import ddt
import json
data = [
    {"phone":"13979296069","key":"63a77489d2c51d26b4031e344b4f0050","expect":"200"},
    {"phone":"","key":"63a77489d2c51d26b4031e344b4f0050","expect":"201"},
    {"phone":"13979296069","key":"","expect":"101"},
]

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





        # r = self.p.phone_location("13979296069","63a77489d2c51d26b4031e344b4f0050")
        # return r






#     def test_phone_location_name_error(self):
#         r = self.p.phone_location("","63a77489d2c51d26b4031e344b4f0050")
#         return r
#     def test_phone_location_key_error(self):
#         r = self.p.phone_location("13979296069", "63a77489d2c51d26b4031e344b4f0050M")
#         return r
#     def test_phone_location_nameandkey_error(self):
#         r = self.p.phone_location("13979296069M", "63a77489d2c51d26b4031e344b4f0050M")
#         return r
#
# if __name__ == '__main__':
#     t = Test_phone()
#     r = t.test_phone_location_nameandkey_error()
#     print(r.text)