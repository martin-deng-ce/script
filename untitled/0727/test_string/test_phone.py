# -*- coding:utf-8 -*-
# @Time:2020/7/30 15:49
# @Author:martin
# @File:test_phone.py
from test_string.phone import Phone
import requests
import ddt
data = [
    {"phone":"13979296069","key":""}
]





class Test_phone():
    def __init__(self):
        self.p = Phone()
    def test_phone_location_success(self):
        r = self.p.phone_location("13979296069","63a77489d2c51d26b4031e344b4f0050")
        return r
    def test_phone_location_name_error(self):
        r = self.p.phone_location("","63a77489d2c51d26b4031e344b4f0050")
        return r
    def test_phone_location_key_error(self):
        r = self.p.phone_location("13979296069", "")
        return r
    def test_phone_location_nameandkey_error(self):
        r = self.p.phone_location("13979296069M", "63a77489d2c51d26b4031e344b4f0050M")
        return r

if __name__ == '__main__':
    t = Test_phone()
    r = t.test_phone_location_name_error()
    print(r.text)

