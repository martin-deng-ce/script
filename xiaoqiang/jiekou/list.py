# -*- coding:utf-8 -*-
# @Time:2020/7/24 11:19
# @Author:martin
# @File:list.py.py
from jiekou.login import login
import requests
s = requests.session()
host = 'http://127.0.0.1'
def list():
    login(s, "byhy", "88888888", host)
    url = host + '/api/mgr/customers'
    par = {
        "action": "list_customer",
        "pagenum": "1",
        "pagesize": "5",
        "keywords": "",
        "_": "1595558273039"
    }
    r = s.get(url=url, params=par)
    return r
    id
if __name__ == '__main__':
    s = requests.session()
    r = list()
    print(r.text)

