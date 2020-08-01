# -*- coding:utf-8 -*-
# @Time:2020/7/29 16:35
# @Author:martin
# @File:__init__.py.py
import xlrd
testdata = xlrd.open_workbook('testdata.xlsx') #打开表格，参数文件路径
table = testdata.sheet_by_name('Sheet1') #通过表中名称获取表
nrows = table.nrows#获取总行数
ncols= table.ncols #获取总列数
print(table.row_values(0)) #获的第一行的值
print(table.col_values(0))# 获的第一列的值
