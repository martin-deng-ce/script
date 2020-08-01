# -*- coding:utf-8 -*-
# @Time:2020/7/24 10:33
# @Author:martin
# @File:login.py.py
import requests
host = 'http://127.0.0.1'
def login(s, user, pwd, host):
    url = host + '/api/mgr/signin'
    body = {
         "username": user,
         "password": pwd
        }
    r = s.post(url=url, data=body)
    return r

if __name__ == '__main__':
   s = requests.session()
   r = login(s, "byhy", "88888888", host)
   print(r.text)