from jiekou.login import login
import requests
import random
def add_school(name, type, canRecruit, remark):
    s = requests.session()
    login(s, 'admin', '660B8D2D5359FF6F94F8D3345698F88C')
    url = 'http://192.168.138.128:8081/recruit.students/school/manage/addSchoolInfo'
    body = {
        "schoolName": name,
        "listSchoolType[0].id": type,
        "canRecruit": canRecruit,
        "remark": remark
    }
    r = s.post(url=url, data=body)
    return r
# if __name__ == '__main__':
#     name = random.randint(100, 10000)
#     r = add_school(name, 2, 1, "test")
#     print(r.text)