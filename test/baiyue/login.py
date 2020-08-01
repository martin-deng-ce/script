# -*- coding:utf-8 -*-
# @Time:2020/7/25 10:38
# @Author:martin
# @File:login.py.py
import requests
s = requests.session()
host = 'http://127.0.0.1'
def login(s, username, password):
    url = host + '/api/mgr/signin'
    body = {
        "username": username,
        "password": password
    }
    r = s.post(url=url, data=body)
    return r
# print(r.text)
if __name__ == '__main__':
    s = requests.session()
    r = login(s, "byhy", "88888888")
    print(r.text)
