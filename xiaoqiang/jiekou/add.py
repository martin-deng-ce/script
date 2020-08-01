# -*- coding:utf-8 -*-
# @Time:2020/7/24 10:33
# @Author:martin
# @File:add.py.py
from jiekou.login import login
import requests
s = requests.session()
import random
host = 'http://127.0.0.1'
def add_customer(name):
    s = requests.session()
    login(s, "byhy", "88888888", host)
    url = host + '/api/mgr/customers'
    body = {"action":"add_customer","data":
        {"name":name,
         "phonenumber":"15768115596",
         "address":"深圳市南山区101号"
        }
    }
    r = s.post(url=url, json=body)
    print(r)
    id = r.json()["id"]
    print(id)
    return id


if __name__ == '__main__':
    name = random.randint(10, 10000)
    id = add_customer(name)
    print(id)

