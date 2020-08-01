# # # # # # # # # # # coding:utf-8
# # # # # # # # # # # a = 1
# # # # # # # # # # # a = "111"
# # # # # # # # # # # # print(a)
# # # # # # # # # # # b = [1,2,3,4,5,6,7,8,9,10]
# # # # # # # # # # # s = 0
# # # # # # # # # # # for i in b:
# # # # # # # # # # #     # s = s + i
# # # # # # # # # # # # print(s)
# # # # # # # # # # # a = b = c = 1
# # # # # # # # # # # # print (a,b,c)
# # # # # # # # # # # d, e, f =1, 2, "hello"
# # # # # # # # # # # # print(d, e, f)
# # # # # # # # # # # a = 12
# # # # # # # # # # # b = 13
# # # # # # # # # # # # print(a+b)
# # # # # # # # # # # # print(a-b)
# # # # # # # # # # # # print(a*b)
# # # # # # # # # # # # print(a/b)
# # # # # # # # # # c = 17
# # # # # # # # # # # print(c&5)
# # # # # # # # # a = 10.1200
# # # # # # # # # b = 5
# # # # # # # # # # print(a+b)
# # # # # # # # # # conding:utf-8
# # # # # # # # # s = "hello"
# # # # # # # # # a = "world"
# # # # # # # # # # print(s+a)
# # # # # # # # # # print(s*3)
# # # # # # # # s1 = "hello world!"
# # # # # # # # # print(s1[1:4])
# # # # # # # # # print(s1[4:])
# # # # # # # # # print(s1[:4])
# # # # # # # # # print(s1[4])
# # # # # # # # # print(s1[::-1])
# # # # # # # # # # print(s1[6:3:-1])
# # # # # # # # print (len(s1))
# # # # # # # # # print(s1.count("1"))
# # # # # # # # coding:utf-8
# # # # # # # a = None
# # # # # # # b = ''
# # # # # # # c = 0
# # # # # # # print(bool(a))  # False
# # # # # # # print(bool(b))  # False
# # # # # # # print(bool(c))  # False
# # # # # # # d = 1
# # # # # # # e = -1
# # # # # # # f = '0'
# # # # # # # print(bool(d))  # True
# # # # # # # print(bool(e))  # True
# # # # # # # print(bool(f))  # True
# # # # # # # #  判断语句
# # # # # # # print(bool(c > d))
# # # # # # # print(bool(c < d))
# # # # # # # print(bool(c == d))
# # # # # # # print(bool(c != d))
# # # # # #
# # # # # # a = 3
# # # # # # b = 5
# # # # # # if a > 0 and b > 0:
# # # # # #     # print(a+b)
# # # # # # a = 3
# # # # # # b = 5
# # # # # # if a < 0 or b > 0:
# # # # # #     # print(a-b)
# # # # # a = 3
# # # # # b = 5
# # # # # c = 0
# # # # # if not c:
# # # # #     # print(c+100)
# # # # # # conding:utf-8
# # # l =  [1, 4, 7, 2, 5, 8]
# # # l.append(3)
# # # print(1)
# # # del l[1]
# # # l.remove(1)
# # # print(l)
# # # print(l)
# # # l[0] = 100
# # # print (1)
# # # print (1[0])
# # # e = l.pop()
# # # print (e)
# # # print(l)
# # # # l = [1, 4, 7, 2, 5, 8]
# # # # print (len(l))
# # # # l.sort()
# # # # print(l)
# # # # print(l.count(1))
# # #
# # age = 30
# # if age > 25:
# #     # print("you are too old")
# # age = 9
# # if age > 25:
# #     print("you are too old")
# # elif age < 10:
# #     print("you are so young")
# # else:
# #     print("it's a boy")
# # n = " hello world123"
# # for i in n:
# #     print(i)
# l = [ "he", '12',12, "hello", "22"]
# for i in  l:
#     print(i)
# s = 0
# for i in list(range(100)):
#     if i & 2:
#         s += i
#     else:
#         continue
# print(s)

# s = 0
# for i  in(range(10)):
#     s+=i
# print(s)
# for i in list(range(10)):
# s = 0
# for i in (range(0,100)):
#     if i & 2:
#        s += i
#     else:
#         continue
# print(s)
#
# s = 0
# i = 1
# while i < 100:
#     if i & 2:
#         s += i
#         if s > 1000:
#      i  += 1
# print(s)
# if __name__ == "__main__":
#     print(u"九九乘法表：")
#     for i in range(1,10):
#         for j in range(i,10):
#             # end=" "
#             print("%d * %d=%2d"%(i, j, i * j),end=" ")
#
#         print("") #
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%d * %d = %2d"%(j, i, i* j),end=" ")
#     print(" ")
# s = 0
# for i in list(range(100)):
#     if i & 2:
#         s += i
#         if s > 1000:
#             break
#         else:
#             continue
# print(s)
# s = 0
# i = 1
# while i < 100:
#     if i & 2:
#         s += i
#     else:
#         continue
# print(s)
# a = 1
# a = "111"
# print(a)
# s = 0
# i = 1
# while i < 100:
#     if not i % 2:
#         s = s + i
#         if s > 1000:
#             break
#     i = i + 1
# print(s)
# s = 0
# i = 1
# while i < 100:
#     if i % 2:
#         s +=i
#     else:
#          pass
#     i +=1
# print(s)
# for i range(10):
import unittest
class Test(unittest.TestCase):
    def testAdd(self):
        a = 1
        b = 2
        c = a + b
        self.assertEqual(c, 3)

    def testMultiply(self):
        a = 2
        b = 3
        c = a * b
        self.assertEqual(c, 5)

if __name__ == '__main__':

    unittest.main()