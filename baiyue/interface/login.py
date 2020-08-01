# -*- coding:utf-8 -*-
# @Time:2020/7/29 9:11
# @Author:martin
# @File:logn.py
import requests
import random
# s = requests.session()
class Baiyue(object): #类的引用
    def __init__(self, s): #类的初始化
        self.s = s # 保持登录
        self.host = 'http://127.0.0.1'
    def login(self,user, pwd):# 函数入参
        url = self.host +'/api/mgr/signin'
        body = {
            "username": user,
            "password": pwd

        }
        r =self.s.post(url=url, data= body)
        return r
    # def list(self):
    #     #     url = self.host+ '/api/mgr/customers'
    #     #     par = {
    #     #         "action":"list_customer",
    #     #         "pagenum":"1",
    #     #         "pagesize":"5",
    #     #         "keywords":"",
    #     #         "_":"1595985259222"
    #     #
    #     #     }
    #     #     r = self.s.get(url=url, params=par)
    #     #     return r
    def add(self,name):
        # login("byhy", "88888888")
        url = self.host + '/api/mgr/customers'
        body = {
            "action":"add_customer",
            "data":{
            "name": name,
            "phonenumber":"13345679934",
            "address":"武汉市桥西医院北路"}
        }
        r = self.s.post(url=url, json=body)

        return r
    # def modify(self,name):
    #     url = self.host + '/api/mgr/customers'
    #     body = {
    #             "action":"modify_customer",
    #             "id": 6,
    #             "newdata":{
    #             "name":name,
    #             "phonenumber":"13345679934",
    #             "address":"武汉市桥西医院北路"}
    #     }
    #     r = self.s.post(url=url, json=body)
    #     return  r

# if __name__ == '__main__':
#     s = requests.session()
#     b = Baiyue(s)
#     b.login("byhy", "88888888")
#     name = random.randint(10, 100000)
#     r = b.add(name)
#     print(r.text)
