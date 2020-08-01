# -*- coding:utf-8 -*-
# @Time:2020/7/24 9:10
# @Author:martin
# @File:__init__.py.
import json
a = {"id":"890167","disable":1,"schoolId":"4778"}
print(type(a))
c = json.dumps(a) #字典转json
print(type(c))
print(c)

b = {"id":"4778","recruitStartTime":None,"recruitEndTime":None,"isStudentRecruitTime":"0"}
print(type(b))
d = json.dumps(b)#字典转json
print(type(d))
print(d)

e = json.loads(d) #json转字典
print(type(e))
print(e)