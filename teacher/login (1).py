# -*- coding:utf-8 -*-
# @Time:2020/7/24 15:49
# @Author:whweia
# @File:login.py
# import requests
host = 'http://127.0.0.1:8002'


def login(s, user, pwd):
    url = host + '/api/mgr/signin'
    body = {
        "username": user,
        "password": pwd
    }
    r = s.post(url=url, data=body)
    return r

# if __name__ == '__main__':
#     r = login().text
#     print(r)