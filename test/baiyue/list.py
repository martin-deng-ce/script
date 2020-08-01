# -*- coding:utf-8 -*-
# @Time:2020/7/25 10:39
# @Author:martin
# @File:list.py.py
from baiyue.login import login
import requests
s = requests.session()
host = 'http://127.0.0.1'
def list():
    login(s, "byhy", "88888888")
    url = host + '/api/mgr/customers'
    par = {
            "action":"list_customer",
            "pagenum":"1",
            "pagesize":"5",
            "keywords":"",
            "_":"1595644880583"
    }
    r = s.get(url=url, params=par)
    id = r.json()["retlist"][0]["id"]
    result = r.text
    return result, id
# print(r.text)
# if __name__ == '__main__':
#     s = requests.session()
#     r = list()
#     print(r.text)
def delete_customer():
    result = list()
    id = result[1]
    url = host + '/api/mgr/customers'
    body = {
        "action": "del_customer",
        "id": id
    }
    r = s.delete(url=url, json=body)
    return r
if __name__ == '__main__':
    r = delete_customer()
    print(r.text)