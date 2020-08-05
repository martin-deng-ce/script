# -*- coding:utf-8 -*-
# @Time:2020/7/23 17:16
# @Author:whweia
# @File:add.py
from jiekou.login import login
import requests
import random

# print(r.text)


def add_school(name, Type, canRecruit, remark):
    s = requests.session()
    login(s, "admin", "660B8D2D5359FF6F94F8D3345698F88C")
    url = 'http://47.113.116.171:8082/recruit.students/school/manage/addSchoolInfo'
    body = {
        "schoolName": name,
        "listSchoolType[0].id": Type,
        "canRecruit": canRecruit,
        "remark": remark
    }
    r = s.post(url=url, data=body)
    return r


if __name__ == '__main__':
    name = random.randint(10000, 10000000)
    r = add_school(name, 2, 1, "test")
    print(r.text)

