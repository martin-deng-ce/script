print("------登录------")
import requests
s = requests.session()
url_login = 'http://47.113.116.171:8082/recruit.students/login/in?account=admin&pwd=660B8D2D5359FF6F94F8D3345698F88C'
result = s.get(url=url_login)
print(result.text)
print("-----新建学校-----")
import random
c = random.randrange(1,1000000)

url_add = "http://47.113.116.171:8082/recruit.students/school/manage/addSchoolInfo"
body_add = {
    "schoolName": c,
    "listSchoolType[0].id":"2",
    "canRecruit":"1",
    "remark":"",
}
r_add = s.post(url=url_add, data=body_add)
print(r_add.text)
print("----禁用学校----")
import re
id = re.findall('"laccount":(.*?),', r_add.text)
print(id[0])
schoolid = re.findall('{"id":(.*?),"schoolName', r_add.text)
print(schoolid[0])

url_jinyong = "http://47.113.116.171:8082/recruit.students/school/manage/enableOrDisableSchool"
headers = {
    "User-Agent": " Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    "Content-Type": "application/json"
}
body_jinyong = [{"id":id[0],"disable":0,"schoolId":schoolid[0]}]
r_jinyong = s.post(url=url_jinyong, json=body_jinyong)
print(r_jinyong.text)
print("----启用学校----")
url_qiyong = "http://47.113.116.171:8082/recruit.students/school/manage/enableOrDisableSchool"
body_qiyong = [{"id":id[0],"disable":1,"schoolId":schoolid[0]}]
r_qiyong = s.post(url=url_qiyong, json=body_qiyong)
print(r_qiyong.text)
print("-----设置学校自主招生------")
import json
id = schoolid[0]
print(id)
url_zizhu = "http://47.113.116.171:8082/recruit.students/school/manage/setStudentRecruitTime"
body_zizhu = '[{"id":"%s","recruitStartTime":null,"recruitEndTime":null,"isStudentRecruitTime":"0"}]'% id
js_body = json.loads(body_zizhu)
print(js_body)
r_zizhu = s.post(url=url_zizhu, json=js_body).json()
print(r_zizhu)



print("-----设置学生录入时间------")
url_luru = "http://47.113.116.171:8082/recruit.students/school/manage/setStudentRecruitTime"
body_luru = [{"id":"4526","recruitStartTime":"2020-07-22","recruitEndTime":"2020-07-31","isStudentRecruitTime":"1"}]
r_luru = s.post(url=url_luru, json=body_luru)
# print(r_luru.text)
print("------设置学生录取时间----")
url_luqu = "http://47.113.116.171:8082/recruit.students/school/manage/setEnrollmentTime"
body_luqu = [{"id":"4526","startTime":"2020-07-25","endTime":"2020-08-08","isSelfEnrollmentTime":"1"}]
r_luqu = s.post(url=url_luqu,json=body_luqu)
# print(r_luqu.text)
