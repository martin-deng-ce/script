#
import requests
def login(s, user, pwd):
    url = 'http://192.168.138.128:8081/recruit.students/login/in'
    par = {
    "account": user,
    "pwd": pwd
    }
    r = s.get(url=url, params=par)
    return r
if __name__ == '__main__':
    s = requests.session()
    r = login(s, 'admin', '660B8D2D5359FF6F94F8D3345698F88C')
    print(r.text)