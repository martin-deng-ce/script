# -*- coding:utf-8 -*-
# @Time:2020/7/24 17:18
# @Author:martin
# @File:demo.py.py
import requests
# key = aba79053b54a2fbab519a3ff05aa2966
class Cardno():
    def cardno_location(self, cardno, key):
        url = 'http://apis.juhe.cn/idcard/index'
        par = {
                "cardno": cardno,
                "key": key
        }
        r = requests.get(url=url, params=par)
        return r
if __name__ == '__main__':
    c = Cardno()
    r = c.cardno_location("360481199010010417", "aba79053b54a2fbab519a3ff05aa2966")
    print(r.text)
