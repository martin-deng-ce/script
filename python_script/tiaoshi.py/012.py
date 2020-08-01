# -*- coding:utf-8 -*-
# @Time:2020/7/23 15:36
# @Author:martin
# @File:012.py.py
def file_write():
    context = input("请输入你的内容:")
    f = open('025.txt', 'w+')
    f.write(context)
    f.close
def file_read():
    f = open('025.txt', 'r+')
    line = f.readline()
    print(line)
    f.close
if __name__ == '__main__':
     # file_write()
     # file_read()
def userN():
    usernmae = input("请输入账号: \n")
    password = input('请输入密码: \n')
    return usrname,password
