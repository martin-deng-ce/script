# -*- coding:utf-8 -*-
# @Time:2020/7/24 16:33
# @Author:martin
# @File:shili.py.py
class people (object):
    def hand(self):
        print("这是我对象的手")
    def foot(self):
        print("这是我对象的脚")
if __name__ == '__main__':
    p = people()
    print(p.hand())
    print(p.foot())
class deng():
    def ce(self):
        print("c")

    def bin(self):
        print("112")
if __name__ == '__main__':
     n = deng()
     print(n.ce())
     print(n.bin())
class count():
    def add(self,a, b):
        return a + b
    def acc(self,a, b):
        return a - b
    def aff(self,a, b):
        return self.add(a, b)*self.acc(a, b)
a = count()
print a aff(3, 1)
