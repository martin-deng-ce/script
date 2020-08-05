# -*- coding:utf-8 -*-
# @Time:2020/7/27 11:42
# @Author:martin
# @File:__init__.py.py
# if __name__ == '__main__':
#
#     for i in range(1,10):
#
#         for j  in range(i, 10):
#
#              print("%d * %d= %d" %(i, j, i*j),end=" ")
#         print("")
# list = [89, 72, 3, 45, 23, 78, 21, 5]
# c = len(list)
# # print(c)
# for a in range(0, c-1):
#     for b in range(0,c-a-1):
#         if list[b] > list[b+1]:
#
#             list[b],list[b+1] = list[b+1],list[b]
#     print(list)
s = 0

# for i in range(1,100):
#     # if  i%2:
#         s+=i
#     # else:
#     #     continue
# print(s)
#
# s = 0
# i = 1
# while i < 100:
#     if i %2:
#
#         s = s+i
#         if s >1000:
#             break
#
#     i = i+1
# print(s)

# s = 0
# i = 0
# while i <100:
#     if i %2:
#         s = s+i
#     else:
#         pass
#     i = i +1
# print(s)
# s = 0
# for i in range(100):
#     if i %2:
#         s =s +i
#         if s >1000:
#             break
#         else:
#             continue
# print(s)
list = [1,4,7,2, 5,9]
list.sort()
print(list)
list.append(3)
print(list)
del list[1]
print(list)
list.remove(9)
print(list)
e = list.pop()
print(e)
print(list)
print(len(list))
list.sort()
print(list)
e = list[2]
print(e)