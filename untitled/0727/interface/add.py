# -*- coding:utf-8 -*-
# @Time:2020/7/27 11:43
# @Author:martin
# @File:add.py.py
from interface.login import Login_school
import requests
import random
s = requests.session()


class Add_school():

    def __init__(self, s):
        # self.l = Login_school(s)
        # self.l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
        self.s = s
        Login_school(s).login("admin", "660B8D2D5359FF6F94F8D3345698F88C")


    def add_school (self, name, Type, canRecruit, remark):
        url = 'http://47.113.116.171:8082/recruit.students/school/manage/addSchoolInfo'
        body = {

                "schoolName": name,
                "listSchoolType[0].id": Type,
                "canRecruit": canRecruit,
                "remark": remark,
        }
        r = self.s.post(url=url, data=body)
        return r
if __name__ == '__main__':
    s = requests.session()
    # l = Login_school(s)
    # l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")

    name = random.randint(100, 10000)
    b = Add_school(s)
    r = b.add_school(name, 2, 1, "test")
    # r = Add_school(s).add_school(name, 2, 1, "test")
    print(r.text)