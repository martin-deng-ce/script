# -*- coding:utf-8 -*-
# @Time:2020/7/23 17:36
# @Author:whweia
# @File:test_add.py
from jiekou.add import add_school
import requests
import random
s = requests.session()


def test_add_school_success():
    name = random.randint(10000, 10000000)
    result = add_school(name, 2, 1, "test")
    return result


def test_add_school_remark_null():
    name = random.randint(10000, 10000000)
    result = add_school(name, 2, 1, "")
    return result


def test_add_school_name_null():
    result = add_school("", 2, 1, "test")
    return result


if __name__ == '__main__':
    test_add_school_success()