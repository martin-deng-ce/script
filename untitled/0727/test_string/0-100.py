# -*- coding:utf-8 -*-
# @Time:2020/7/27 10:01
# @Author:martin
# @File:0-100.py
# s = 0
# # for i in range(1, 100):
# #     if  i % 2:
# #         s = s + i
# #     else:
# #         continue
# # # print(s)
s = 0
for i in range(1, 100):
    if i % 2:
        s = s + i
    else:
        continue
print(s)
s = 0
for a in range(100):
    s = s + a
print(s)