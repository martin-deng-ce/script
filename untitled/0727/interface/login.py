# -*- coding:utf-8 -*-
# @Time:2020/7/27 11:43
# @Author:martin
# @File:login.py.py
import requests
# pwd=660B8D2D5359FF6F94F8D3345698F88C
# s = requests.session()


class Login_school(object):

    def __init__(self, s):
         self.s = s

    def login(self, usr, pwd):
        url = 'http://47.113.116.171:8082/recruit.students/login/in'
        par = {
            "account": usr,
            "pwd": pwd
        }
        r = self.s.get(url=url, params=par)
        return r

# if __name__ == '__main__':
#     s = requests.session()
#     l = Login_school(s)
#     r =l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
#     print(r.text)

