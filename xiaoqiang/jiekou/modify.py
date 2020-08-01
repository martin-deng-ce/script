# -*- coding:utf-8 -*-
# @Time:2020/7/24 11:54
# @Author:martin
# @File:modify.py.py
from jiekou.add import add_customer
import requests
s = requests.session()
import random
import re
host = 'http://127.0.0.1/api/mgr/customers'
def modify_school():
    s = requests.session()
    add_customer(name)
    url = host + '/api/mgr/customers'
    body = {"action":"modify_customer","id":123,"newdata":{"name":"今天真好看！"}}
    r = s.put(url=url, json=body)
    return r1

if __name__ == '__main__':
     s = requests.session()
     name = random.randint(10, 10000)
     r = modify_school()