# -*- coding:utf-8 -*-
# @Time:2020/7/25 11:29
# @Author:martin
# @File:jinyong.py.py
from jiaoyuxitong.add import add_school
import requests
s = requests.session()
import random
host = 'http://192.168.138.128:8081'

def enable_school()
    url = '/recruit.students/school/manage/enableOrDisableSchool'
    body = [{"id":"590939",
             "disable":0,
             "schoolId":"276"
             }]
    r = s.post(url=url, json=body)

    return r
if __name__ == '__main__':
    name = random.randint(100, 100000)
    y = add_school(name, 2, 1, "test")
    t = enable_school()
    print(r.text)