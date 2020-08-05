# -*- coding:utf-8 -*-
# @Time:2020/7/23 16:06
# @Author:whweia
# @File:login.py
import requests
host = 'http://47.113.116.171:8082'
# 660B8D2D5359FF6F94F8D3345698F88C


def login(s, user, pwd):
    url = host + '/recruit.students/login/in'
    par = {
        "account": user,
        "pwd": pwd
    }
    r = s.get(url, params=par)
    return r

#
# if __name__ == '__main__':
#     s = requests.session()
#     r = login(s, "admin", "660B8D2D5359FF6F94F8D3345698F88C")
#     print(r.text)
