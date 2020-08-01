# -*- coding:utf-8 -*-
# @Time:2020/7/28 21:21
# @Author:martin
# @File:__init__.py.py
#转换
import json
d1 = {
     "a": None,
    "b": False,
    "c": True,
    "d": "BAB2",
    "e": ["1",12],
    "f": ("1n",90),
    "g": {"h": 1,
          "i": "11",
          "j": True}
    }
print(type(d1)) #数据类型是字典
# <class 'dict'> 返回的值
d1_js = json.dumps(d1) #字典转json

print(type(d1_js)) #转换后，数据类型是字符串
# <class 'str'> 返回的值
print(d1_js)
# {"a": null, "b": false, "c": true, "d": "BAB2", "e": ["1", 12], "f": ["1n", 90], "g": {"h": 1, "i": "11", "j": true}}

js_d1 = json.loads(d1_js) #json转字典
print(type(js_d1)) #转换后，数据类型是字典
# <class 'str'>返回的值
print(js_d1)
# {'a': None, 'b': False, 'c': True, 'd': 'BAB2', 'e': ['1', 12], 'f': ['1n', 90], 'g': {'h': 1, 'i': '11', 'j': True}}