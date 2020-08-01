# -*- coding:utf-8 -*-
# @Time:2020/7/28 9:21
# @Author:martin
# @File:login.py.py
# import requests
# s = requests.session()
# 660B8D2D5359FF6F94F8D3345698F88C
# host = 'http://192.168.138.128:8081/'

class Login_school(object):

    def __init__(self, s):
         self.s = s
         self.host = 'http://192.168.138.128:8081/'

    def login(self, usr, pwd):
        url = self.host + '/recruit.students/login/in'
        par = {
            "account": usr,
            "pwd": pwd
        }
        r = self.s.get(url=url, params=par)
        return r

if __name__ == '__main__':
    import requests
    s = requests.session()
    l = Login_school(s)
    r =l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
    print(r.text)

