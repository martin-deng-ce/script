import requests
# import json
# id = 4629
# url_zizhu = "http://47.113.116.171:8082/recruit.students/school/manage/setStudentRecruitTime"
# body_zizhu = '[{"id":"%d","recruitStartTime":null,"recruitEndTime":null,"isStudentRecruitTime":"0"}]'% id
# js_body = json.loads(body_zizhu)
# print(js_body)
# r_zizhu = s.post(url=url_zizhu, json=js_body).json()
# print(r_zizhu.text)
# a = 3
# a = '111'
# print(a)
# a = b = c = 1
# print(a)
# name = "yoyo"
# age = "26"
# print("%s is %d years old" %(name, age))

# def add(a, b):
#     c = a + b
#     return c
# print(c)
#  r = add (6, 9)
#  print(r)

import requests
def login(s, user, pwd):
    url = 'http://192.168.138.128:8081/recruit.students/login/in'
    par = {
    "account": user,
    "pwd": pwd
    }
    r = requests.get(url=url, params=par)
    return r
if __name__ == '__main__':
    s = requests.session()
    r = login(s, 'admin', '660B8D2D5359FF6F94F8D3345698F88C')
    print(r.text)

