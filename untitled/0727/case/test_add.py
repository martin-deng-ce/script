# -*- coding:utf-8 -*-
# @Time:2020/7/27 14:12
# @Author:martin
# @File:test_add.py.py
from interface.add import Add_school
import requests
import random
s = requests.session()


class Test_ADD_School():


    def __init__(self):
        self.p = Add_school(s)

    #     # self.a = Add_school(s)
    #     # self.l = Login_school()
    #     # self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")

    def test_add_school_success(self):
        name = random.randint(100, 10000)
        r = self.p.add_school(name, 2, 1, "test")
        return r

if __name__ == '__main__':
    t = Test_ADD_School()
    r = t.test_add_school_success()
    print(r.text)

