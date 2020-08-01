# -*- coding:utf-8 -*-
# @Time:2020/7/27 9:47
# @Author:martin
# @File:99.py.py
if __name__ == '__main__':
    print('''JIUJIUCHENFFA''')
    for i in range(1,10):
        for j in range(i,10):
            # end=(" ")先换行隔开
            print("%d * %d = %2d" % (i, j, i * j), end=" ")
        print("")
if __name__ == '__main__':
    for a in range(1, 10):
        for b in range(1, a):
            print("%d * %d= %2d" % (b, a, b * a), end=" ")
        print("")
