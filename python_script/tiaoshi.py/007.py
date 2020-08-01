def add(a, b):
    c = a + b
    return c
r = add (6, 9)
# print(r)
def add():
    a = 7
    b = 10
    c = a + b
    return c
# print(c)
import requests
# aba79053b54a2fbab519a3ff05aa2966
def shenfen(cardno, key):
    url = 'http://apis.juhe.cn/idcard/index'
    par = {
        "cardno": cardno,
        "key": key
    }
    r = requests.get(url=url, params=par)
    return r
if __name__ == '__main__':
    # 正常流
    r = shenfen(360481199010010417, 'aba79053b54a2fbab519a3ff05aa2966')
    print(r.text)
    # 异常流
    r1 = shenfen('', 'aba79053b54a2fbab519a3ff05aa2966')
    print(r1.text)
    r3 = shenfen(360481199010010418, 'aba79053b54a2fbab519a3ff05aa2966')
    print(r3.text)
def file_write():
    context = input ("请输入你的内容：")
    f = open('hello1.text', 'w')
    f.write(context)
    f.close()
def file_read():
    f = open('hello1.text', 'r')
    line = f.readline()
    print(line)
    f.close()
if __name__ == '__main__':
    file_write()
    file_read()
