# -*- coding:utf-8 -*-
# @Time:2020/7/29 15:28
# @Author:martin
# @File:test_modify.py.py
from interface.login1 import Baiyue
import requests

s = requests.session()
import random
class Testmodfiy():
    def __init__(self):
        self.l = Baiyue(s)
        self.l.login("byhy", "88888888")
        name= random.randint(10, 100000)
        self.l.add(name)

    def test_modify_customer_success(self):
        id1 = self.add(name)
        r = self.l.modify_customer("")
        return r

if __name__ == '__main__':
    t = Testmodfiy()
    r = t.test_modify_customer_success()
    print(r.text)
