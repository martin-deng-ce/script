# -*- coding:utf-8 -*-
# @Time:2020/7/30 11:00
# @Author:martin
# @File:Excel_demo.py
import xlrd
class Excelutil(object):
    def __init__(self, excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)
        self.rownum = self.table.nrows
        self.colnum = self.table.ncols
    def dict_data(self):
        if self.rownum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rownum - 1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colnum):
                    s [self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r
if __name__ == '__main__':
    filepath = "testdata.xlsx"
    sheetName = "Sheet1"
    data = Excelutil(filepath,sheetName)
    print(data.dict_data())
    print(type(data.dict_data()))


