# -*- coding:utf-8 -*-
# @Time:2020/7/24 9:15
# @Author:martin
# @File:test_add.py.py
from jiekou.add import add_school
import requests
import random
s = requests.session()

def test_add_school_success():
    name = random.randint(10, 10000)
    result = (name, 2, 1, "test")
    return result

if __name__ == '__main__':
    name = random.randint(10, 10000)
    result = test_add_school_success()
    print(result.text)