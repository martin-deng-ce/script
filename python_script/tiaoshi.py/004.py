import requests
s = requests.session()
url_login = 'http://192.168.138.128/xiaoqiangshop/user.php'
body_login = {
    "username": "xiaoqiang1",
    "password": "123123",
    "act": "act_login",
    "back_act": "http://192.168.138.128/xiaoqiangshop/",
    "submit": "",
}
r_add = s.post(url=url_login, data=body_login)
# print(r_add.text)
s = 0
i = 1
while i < 100:
    if i % 2:
        s = s + 1
    else:
        pass
# print(s)
a = 1
a = "111"
print(a)