# -*- coding:utf-8 -*-
# @Time:2020/7/29 16:36
# @Author:martin
# @File:mysql.py
import pymysql #写入数据库模块
#配置链接
class Mysqlhelp(object):
    def connect(self):
        try:
            self.conn = pymysql.connect(
            host = "192.168.138.128",#mysql服务ip地址
            port = 3306,#mysql服务端口号
            user = "root",#访问mysql的用户名
            password = "root",#访问mysql的密码
            database = "recruit_students" #默认链接到的数据库名称
        )
            self.cursor = self.conn.cursor() #创建用于交互的cursor的对象，建立游标
        except Exception as e:
            print(e)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_data(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchone()
        except:
            pass
        finally:
            pass
    def delete_data(self, param):
        try:
            self.connect()
            sql = 'delete from t_school_info where f_school_name = "%s"' %param
            print(sql)
            self.cursor.execute(sql)
            result = self.conn.commit()
            return result
        except:
            pass



# # sql_select = "select*from t_school_info"
# # sql_del = "delete from t_school_info where f_school_name='66120'"
# sql1 = "insert into 't_school_info'('f_id', 'f_school_name')values('287','1778') "
# # cursor.execute(sql_del)#执行sql
# cursor.execute(sql1)
# conn.commit()#提交至数据库
#
# cursor.close()#关闭游标
#
#
# conn.close()#最后把数据库链接关闭

