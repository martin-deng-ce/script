# -*- coding:utf-8 -*-
# @Time:2020/8/3 11:03
# @Author:martin
# @File:test_app.py
import os
import time
cmd = "adb shell am start -W -n com.android.browser/.BrowserActivity"
print("打开app")
content = os.popen(cmd)
print("获取启动时间")
for line in content.readlines():
    if "ThisTime" in line:
        startTime = line.split(":")[1]
        print(startTime)
time.sleep(2)
print("关闭app")
cmd = "adb shell am force-stop com.android.browser"
os.popen(cmd)