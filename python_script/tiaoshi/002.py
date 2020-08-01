# # # import requests
# # #
# # # url = "http://apis.juhe.cn/simpleWeather/query?city=深圳&key=4611a7abae4afe573fd7ca751d9d423a"
# # # result = requests.get(url=url)
# # # print(result.text)
# # # import requests
# # #
# # # u = "http://apis.juhe.cn/simpleWeather/query"
# # # pa = {
# # #     "city":"南昌",
# # #     "key":"4611a7abae4afe573fd7ca751d9d423a"
# # # }
# # # result = requests.get(url=u, params=pa)
# # # print(result.text)
# # # import requests
# # #
# # # url = "http://apis.juhe.cn/idcard/index?key=aba79053b54a2fbab519a3ff05aa2966&cardno=360481199010010417"
# # # url = "http://apis.juhe.cn/idcard/index"
# # #
# # # par = {
# # #     "key": "aba79053b54a2fbab519a3ff05aa2966",
# # #     "cardno": "360481199010010417"
# # # }
# # #
# # # result = requests.get(url=url, params=par)
# # #
# # # print(result.text)
# #
# # import requests
# # s = requests.session()
# #
# # url_login = "http://192.168.138.128/xiaoqiangshop/user.php"
# # body_login = {
# #             "username":"xiaoqiang1",
# #             "password":"123123",
# #             "act":"act_login",
# #             "back_act":"http://192.168.138.128/xiaoqiangshop/index.php",
# #             "submit":""
# # }
# # result = s.post(url=url_login, data=body_login)
# # # print(result.text)
# #
# # url = "http://192.168.138.132//xiaoqiangshop/flow.php?step=add_to_cart"
# # body = {
# #     'goods': '{"quick":1,"spec":[],"goods_id":140,"number":"1","parent":0}',
# # }
# # result = s.post(url=url, data=body)
# # print(result.text)
# #
# # # import requests
# # # url = "http://192.168.138.128/xiaoqiangshop/flow.php?step=done"
# # # body = {
# # #         "shipping": "1",
# # import requests
# # #         "payment": "1",
# # #         "bonus": "0",
# # #         "bonus_sn": "",
# # #         "postscript": "",
# # #         "how_oos": "0",
# # #         "x": "84",
# # #         "y": "21",
# # #         "step": "done"
# # # }
# # # result = requests.post(url=url, data=body)
# # # print(result.txt)
# #
# # # import requests
# # # s = requests.session()
# # # u = "http://192.168.138.128/xiaoqiangshop/user.php"
# # # b = {
# # #             "username": "xiaoqiang1",
# # #             "password": "123123",
# # #             "act": "act_login",
# # #             "back_act": "http://192.168.138.128/xiaoqiangshop/index.php",
# # #             "submit": "",
# # # }
# # # r = s.post(url=u, data=b)
# # # print(r.text)
# # #
# # # import requests
# # # s = requests.session()
# # # url_login = 'http://192.168.138.128/xiaoqiangshop/user.php'
# # # body_login = {
# # #     "username": "xiaoqiang1",
# # #     "password": "123123",
# # #     "act": "act_login",
# # #     "back_act": "http://192.168.138.128/xiaoqiangshop/",
# # #     "submit": "",
# # # }
# # #
# # # r = s.post(url=url_login, data=body_login)
# # # print(r.text)
#
#
#
#
#
#
#
# import requests
# s = requests.session()
# print("------登录------")
# url_login = 'http://47.113.116.171:8082/recruit.students/login/in?account=admin&pwd=660B8D2D5359FF6F94F8D3345698F88C'
# result = s.get(url=url_login)
# # print(result.text)
# print("-----新建学校-----")
# import random
# c = random.randrange(1,50)
#
# url_add = "http://47.113.116.171:8082/recruit.students/school/manage/addSchoolInfo"
# body_add = {
#     "schoolName": c,
#     "listSchoolType[0].id":"2",
#     "canRecruit":"1",
#     "remark":"",
# }
# r_add = s.post(url=url_add, data=body_add)
# # print(r_add.text)
# print("----禁用学校----")
# url_jinyong = "http://47.113.116.171:8082/recruit.students/school/manage/enableOrDisableSchool"
# # headers = {
# #     "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
# #     "Content-Type": "application/json"
# # }
# body_jinyong = [{"id":"846461","disable":0,"schoolId":"4526"}]
# r_jinyong = s.post(url=url_jinyong, json=body_jinyong)
# # print(r_jinyong.text)
# print("----启用学校----")
# url_qiyong = "http://47.113.116.171:8082/recruit.students/school/manage/enableOrDisableSchool"
# body_qiyong = [{"id":"846461","disable":1,"schoolId":"4526"}]
# r_qiyong = s.post(url=url_qiyong, json=body_qiyong)
# # print(r_qiyong.text)
# print("-----设置学生录入时间------")
# url_luru = "http://47.113.116.171:8082/recruit.students/school/manage/setStudentRecruitTime"
# body_luru = [{"id":"4526","recruitStartTime":"2020-07-22","recruitEndTime":"2020-07-31","isStudentRecruitTime":"1"}]
# r_luru = s.post(url=url_luru, json=body_luru)
# print(r_luru.text)
# print("------设置学生录取时间----")
# url_luqu = "http://47.113.116.171:8082/recruit.students/school/manage/setEnrollmentTime"
# body_luqu = [{"id":"4526","startTime":"2020-07-25","endTime":"2020-08-08","isSelfEnrollmentTime":"1"}]
# r_luqu = s.post(url=url_luqu,json=body_luqu)
# # print(r_luqu.text)
# import unittest
# import time
#
#
# class Test(unittest.TestCase):
#
#     def setUp(self):
#         print("start!")
#
#     def tearDown(self):
#         time.sleep(1)
#         print("end!")
#
#     def test_01(self):
#
#         print("执行测试用例01")
#
#     def test_03(self):
#         print("执行测试用例03")
#
#     def test_02(self):
#         print("执行测试用例02")
#
#     def addtest(self):
#         print("add方法")
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# if __name__ == '__main__':
#
#
#     print('''九九乘法表''')
#     for i in range(1, 10):
#         for j in range(i, 10):
#             print("%d * %d = %d" % (i, j, i * j), end=" ")
#         print("")
#
# if __name__ == '__main__':
#     print('''九九乘法表''')
#     for a  in range(1, 10):
#         for b in range(1, a+1):
#             print("%d * %d= %d" %(b, a, b * a), end=" ")
#         print("")
n = 1
n = '1111'
print(n)
if __name__ == '__main__':
    print(""""maopao""")
n = [89, 3, 56, 17, 92, 9, 43, 21]
d = len(n)
# print(d)
for a in range(0, d-1):
    for b in range(0, a-d-1):
        if n[b] > n[b+1]:
            n[b], n[b+1] = n[b+1], n[b]
    print(n)

