# -*- coding:utf-8 -*-
# @Time:2020/7/25 11:28
# @Author:martin
# @File:add.py.py
from jiaoyuxitong.login import login
import requests
import random
import re

# s = requests.session()
host = 'http://192.168.138.128:8081'
def add_school(name, Type, canRecruit, remark):
    s = requests.session()
    login(s, "admin", "660B8D2D5359FF6F94F8D3345698F88C")
    url = host + '/recruit.students/school/manage/addSchoolInfo'
    body = {
            "schoolName": name,
            "listSchoolType[0].id": Type,
            "canRecruit": canRecruit,
            "remark": remark
    }
    r = s.post(url=url, data=body)
    # print(r.text)
    id = re.findall('"laccount":(.*?),', r.text)[0]
    # print(id)
    result = r.text
    schoolid = re.findall('"id":(.*?),"schoolName', r.text)[0]
    # print(schoolid)
    result = r.text
    return result, id, schoolid
# print(r.text)
if __name__ == '__main__':
    name = random.randint(100, 100000)
    r = add_school(name, 2, 1, "test")
    print(r.text)