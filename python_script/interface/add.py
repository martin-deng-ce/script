# -*- coding:utf-8 -*-
# @Time:2020/7/28 9:21
# @Author:martin
# @File:add.py.py
import requests
# pwd=660B8D2D5359FF6F94F8D3345698F88C
s = requests.session()
import random


class School(object):

    def __init__(self, s):

         self.s = s
         self.host = 'http://47.113.116.171:8082'

    def login(self, usr, pwd):
        url =  self.host + '/recruit.students/login/in'
        par = {
            "account": usr,
            "pwd": pwd
        }
        r = self.s.get(url=url, params=par)
        return r

    def add(self, name):

        url =  self.host + '/recruit.students/school/manage/addSchoolInfo'
        body = {

            "schoolName": name,
            "listSchoolType[0].id": "2",
            "canRecruit": "1",
            "remark": "",
        }
        r = self.s.post(url=url, data=body)
        return r


if __name__ == '__main__':
    s = requests.session()
    l = School(s)
    l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")

    name = random.randint(10, 100000)
    r = l.add(name)
    print(r.text)