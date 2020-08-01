# -*- coding:utf-8 -*-
# @Time:2020/7/25 11:28
# @Author:martin
# @File:login.py.py
import requests
s = requests.session()
host = 'http://192.168.138.128:8081'
# "660B8D2D5359FF6F94F8D3345698F88C"
def login (s, account, pwd):
    url = host + '/recruit.students/login/in'
    par = {
        "account": account,
        "pwd": pwd
    }
    r = s.get(url=url, params=par)
    return r
# print(r.text)
if __name__ == '__main__':
    r = login(s, "admin", "660B8D2D5359FF6F94F8D3345698F88C")
    print(r.text)