# -*- coding:utf-8 -*-
# @Time:2020/7/27 16:21
# @Author:martin
# @File:school.py.py
import requests
# pwd=660B8D2D5359FF6F94F8D3345698F88C
s = requests.session()
import random
# from commen.Mysql import Mysqlhelp

class School(object):

    def __init__(self, s):

         self.s = s
         self.host = 'http://192.168.138.128:8081'

    def login(self, user, psw):
        url = self.host + '/recruit.students/login/in'
        par = {
            "account": user,
            "pwd": psw
        }
        r = self.s.get(url=url, params=par)
        return r

    def add(self, name):

        url = self.host + '/recruit.students/school/manage/addSchoolInfo'
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
    r = l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
    print(r.text)
#
    name = random.randint(10, 1000000)
    r = l.add(name)
    print(r.text)