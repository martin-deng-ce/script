import requests
s = requests.session()


print("------登录-------")
url_login = 'http://192.168.64.128/xiaoqiangshop/user.php'

body_login = {
    "username": "xiaoqiang1",
    "password": "123123",
    "act": "act_login",
    "back_act": "http://192.168.64.128/xiaoqiangshop/",
    "submit": "",
}

r = s.post(url=url_login, data=body_login)
print(r.text)


print("------搜索商品--------")
url_search = 'http://192.168.64.128/xiaoqiangshop/goods.php?id=134'
r_search = s.get(url=url_search)

print("------加入购物车------")
url_cart = 'http://192.168.64.128/xiaoqiangshop/flow.php?step=add_to_cart'
body_cart = {
    'goods': '{"quick":1,"spec":[],"goods_id":134,"number":"1","parent":0}'
}
r_cart= s.post(url=url_cart, data=body_cart)
print(r_cart.text)
