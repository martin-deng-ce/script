# -*- coding:utf-8 -*-
# @Time:2020/7/27 10:19
# @Author:martin
# @File:maopao.py.py
list = [95,14, 88,3, 72,72, 29, 46, 37]
n = len(list)
print(n)
for a in range(0, n-1):
    for b in range(0, n-a-1):
        if list[b] > list[b+1]:
            list[b], list[b+1] = list[b+1], list[b]
    print(list)
