# -*- coding:utf-8 -*-
# @Time:2020/7/25 9:26
# @Author:martin
# @File:demo1.py.py
import requests
# key=4611a7abae4afe573fd7ca751d9d423a
class City():
    def city_location(self,city, key):
        url = 'http://apis.juhe.cn/simpleWeather/query'
        par = {
            "city": city,
            "key": key

        }
        r = requests.get(url=url, params=par)
        # print(r.text)
        return r

if __name__ == '__main__':
    c = City()
    r= c.city_location("北京", "4611a7abae4afe573fd7ca751d9d423a")
    print(r.text)