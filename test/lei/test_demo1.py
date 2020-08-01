# -*- coding:utf-8 -*-
# @Time:2020/7/25 9:46
# @Author:martin
# @File:test_demo1.py.py
from lei.demo1 import City
import requests
class Test_City():
    def __init__(self):
     self.c = City()
    def test_city_success(self):
        r = self.c.city_location("北京", "4611a7abae4afe573fd7ca751d9d423a")
        return r
    def test_city_null(self):
        r = self.c.city_location("", "4611a7abae4afe573fd7ca751d9d423a")
        return r
    def test_city_key(self):
        r = self.c.city_location("北京", "")
        return r
if __name__ == '__main__':
    t = Test_City()
    r = t.test_city_success()
    r1 = t.test_city_null()
    r2 = t.test_city_key()
    print(r.text)
    print(r1.text)
    print(r2.text)