# -*- coding:utf-8 -*-
# @Time:2020/7/24 11:58
# @Author:martin
# @File:tiaoshi.py.py

import requests
s = requests.session()
url = 'http://127.0.0.1/api/mgr/customers'
body = {"action":"add_customer","data":
    {"name":"今天真好看",
     "phonenumber":"15768115596",
     "address":"深圳市南山区101号"
    }
}
r = s.post(url=url, json=body)
print(r)