# -*- coding:utf-8 -*-
# @Time:2020/7/24 17:32
# @Author:martin
# @File:test_demo.py.py
from lei.demo import Cardno
import requests
class Test_Cardno():
    def __init__(self):
        self.c = Cardno()
    def test_cardno_success(self):
        r = self.c.cardno_location("360481199010010417", "aba79053b54a2fbab519a3ff05aa2966")
        return r
    def test_cardno_null(self):
        r = self.c.cardno_location("", "aba79053b54a2fbab519a3ff05aa2966")
        return r
if __name__ == '__main__':
        t = Test_Cardno()
        r = t.test_cardno_success()
        r1 = t.test_cardno_null()
        print(r.text)
        print(r1.text)