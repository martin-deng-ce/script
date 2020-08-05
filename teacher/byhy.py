# -*- coding:utf-8 -*-
# @Time:2020/7/24 15:57
# @Author:whweia
# @File:byhy.py
from jiekou.login import login
host = 'http://127.0.0.1:8002'
import requests
s = requests.session()

# 先登录
def list():
    login(s, "byhy", "88888888")
    url = host + '/api/mgr/customers?action=list_customer&pagenum=1&pagesize=5&keywords='
    r = s.get(url)
    id = r.json()["retlist"][0]["id"]
    result = r.text
    return result, id


def del_customer():
    # login(s, "byhy", "88888888")
    result = list()
    id = result[1]
    url = host + '/api/mgr/customers'
    body = {
            "action":"del_customer",
            "id": id
            }
    r = s.delete(url=url, json=body)
    return r


if __name__ == '__main__':

    r = del_customer()
    print(r.text)

