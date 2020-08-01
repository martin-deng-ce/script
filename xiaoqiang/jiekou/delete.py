# -*- coding:utf-8 -*-
# @Time:2020/7/24 11:54
# @Author:martin
# @File:delete.py.py
from jiekou.login import login
from jiekou.add import add_customer
import requests
import random
s = requests.session()
host = 'http://127.0.0.1'
def delete(id):
    s = requests.session()
    login(s, "byhy", "88888888", host)
    # add_customer(name)
     # = add_customer(name)
    url = host + '/api/mgr/customers'
    body = {
        "action":"del_customer",
        "id":id
    }
    r = s.delete(url=url, json=body)
    return r


if __name__ == '__main__':
    name = random.randint(10, 10000)
    y = add_customer(name)
    t = delete(y)
    print(t.text)
    print(t)