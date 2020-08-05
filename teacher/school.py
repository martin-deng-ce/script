# -*- coding:utf-8 -*-
# @Time:2020/7/27 11:02
# @Author:whweia
# @File:login.py
# 660B8D2D5359FF6F94F8D3345698F88C
import requests
import random


class School(object):
    def __init__(self, s):
        self.s = s

    def login(self,user, pwd):
        url = 'http://47.113.116.171:8082/recruit.students/login/in'
        par = {
            "account": user,
            "pwd": pwd
        }
        r = self.s.get(url, params=par)
        return r

    def add(self, name):
        url = 'http://47.113.116.171:8082/recruit.students/school/manage/addSchoolInfo'
        body={
            "schoolName": name,
            "listSchoolType[0].id": "2",
            "canRecruit": "2",
            "remark": ""
        }
        r = self.s.post(url, data=body)
        return r

#
# if __name__ == '__main__':
#     s = requests.session()
#     l = School(s)
#     r = l.login("admin", "660B8D2D5359FF6F94F8D3345698F88C")
#     print(r.text)


