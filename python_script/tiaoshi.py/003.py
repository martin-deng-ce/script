# # print("hello world")
# # print("hello\nworld")
# # name="yoyo"
# # print('mya name is:'+name)
# # name="yoyo"
# # age=26
# # print("%s is %d years old"%(name,age))
# # name = input("input your name:")
# # print("my name is :"+ name)
# # coding:utf-8
# #
# # a = 1
# # b = 2
# # a = "2"
# # b = "1"
# # print(a,b)
# # c = 15
# # print(c/5)
# #
# nums =[12, 99, 18, 76, 2]
# count = len(nums)
# for i in range(0, count-1):
#     for j in range(0, count-i-1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]
#         print(nums)
# s1 = "hello world!"
# print(s1[4])
#
# for a in range(10):
#     print(a)
# nums = [12, 99, 18, 76, 2]
# count = len(nums)
# for j in range(0, count-1):
#     if nums[j] > nums[j+1]:
#         nums[j], nums[j+1] = nums[j+1], nums[j]  # 交换
# print(nums)
# import requests
#
# url = "http://apis.juhe.cn/simpleWeather/query"
# par = {
#     "city":"深圳",
#     "key":"4611a7abae4afe573fd7ca751d9d423a"
# }
# result = requests.get(url=url, params=par)
# print(result.text)
# import requests
#
# url_login= "http://192.168.138.128/xiaoqiangshop/user.php",
# body_login = {
#             "username":"xiaoqiang1",
#             "password":"123123",
#             "act":"act_login",
#             "back_act":"http://192.168.138.128/xiaoqiangshop/index.php",
#             "submit":""
# }
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
# }
# result = requests.post(url=url_login, data=body_login, headers=headers)
# print(result.txt)

# import requests
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded"
# }
# url = "http://192.168.138.132//xiaoqiangshop/flow.php?step=add_to_cart"
# body = {
#     "goods": '{"quick":1,"spec":[],"goods_id":140,"number":"1","parent":0}',
# }
#
# result = requests.post(url=url, data=body, headers=headers)
# print(result.txt)
#
# import requests
# url = "http://192.168.138.128/xiaoqiangshop/flow.php?step=done"
# body = {
#         "shipping": "1",
#         "payment": "1",
#         "bonus": "0",
#         "bonus_sn": "",
#         "postscript": "",
#         "how_oos": "0",
#         "x": "84",
#         "y": "21",
#         "step": "done"
# }
# result = requests.post(url=url, data=body)
# # print(result.txt)
# a = 1
# a = "111"
# print(a)
n = [89, 3, 56, 17, 92, 9, 43, 21]
d = len(n)
print(d)
for a in range(0, d-1):
    for b in range(0, d-a-1):
        if n[b] > n[b+1]:
            n[b], n[b+1] = n[b+1], n[b]
    print(n)
list = [95,14, 88,3, 72,72, 29, 46, 37]
n = len(list)
print(n)
for a in range(0, n-1):
    for b in range(0, n-a-1):
        if list[b] > list[b+1]:
            list[b], list[b+1] = list[b+1], list[b]
    print(list)