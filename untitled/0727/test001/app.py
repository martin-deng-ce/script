# -*- coding:utf-8 -*-
# @Time:2020/8/3 11:34
# @Author:martin
# @File:app.py
import csv
import os
import time
#启动类
class App(object):
    def __init__(self):
        self.content = ""
        self.startTime = 0
    #启动App
    def LaunchApp(self):
        cmd = "adb shell am start -W -n com.android.browser/.BrowserActivity"
        self.content = os .popen(cmd)
    #停止App
    def StopApp(self):
        cmd = "adb shell am force-stop com.android.browser"
        os .popen(cmd)
    #获取启动时间
    def GetLaunchedTime(self):
        for line in self.content.readlines():
            if "ThisTime" in line:
                self.startTime = line.split(":")
                break
        return self.startTime
#控制类
class Controller(object):
    def __init__(self,count):
        self.app = App()
        self.counter = count
        self.alldata = [("timestamp","elapsedtime")]
    #单次测试过程
    def testprocess(self):
        self.app.LaunchApp()
        time.sleep(5)
        elapsedtime = self.app.GetLaunchedTime()
        self.app.StopApp()
        currenttime = self.getCurrentTime()
        self.alldata.append((currenttime,elapsedtime))
        print(self.alldata)

    #多次执行测试过程
    def run(self):
        while self.counter > 0 :
            self.testprocess()
            self.counter = self.counter - 1
    #获取当前时间戳
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime
    #数据存储到CSV中
    def SaveDatatoCSV(self):
        csvfile = open("test_startTime.csv","w")
        writer = csv.writer(csvfile)
        writer.writerows(self.alldata)
        csvfile.close()

if __name__ == '__main__':
    controller = Controller(5)
    controller.run()
    controller.SaveDatatoCSV()






