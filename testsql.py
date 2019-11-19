import mysql.connector
import sys
import time
import datetime
import random
class SqlModule:

    def __init__(self, hostname, user, password, port, base_name, table_name):
        self.base_name = base_name
        self.table_name = table_name
        try:
            self.conn = mysql.connector.connect(
                host=hostname,
                port=port,
                user=user,
                password=password,
                use_unicode = True,
                charset = "utf8")


            cursor = self.conn.cursor()
            cursor.execute('SET NAMES utf8')
            cursor.execute('SET CHARACTER SET utf8')
            cursor.execute('SET character_set_connection=utf8')
        except mysql.connector.errors.DatabaseError as e:
            print('Connect to MySQL error' + str(e))
            sys.exit()

# id ip register username os contry gpu cpu ram version uptime status

    def create_base(self):
        try:
            cursor = self.conn.cursor()
            sql_req = """CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'""".format(self.base_name)
            cursor.execute(sql_req)
            self.conn.commit()
        except mysql.connector.Error as error:
            print("Failed! Reason:\n{}".format(error))

    def delete_base(self):
        try:
            cursor = self.conn.cursor()
            sql_req = """DROP DATABASE IF EXISTS {}""".format(self.base_name)
            cursor.execute(sql_req)
        except mysql.connector.Error as error:
            print("Failed! Reason:\n{}".format(error))

    def create_table(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('use {}'.format(self.base_name))
            sql_req = """CREATE TABLE IF NOT EXISTS {} (id VARCHAR(30),
             ip VARCHAR(15) PRIMARY KEY, register TIMESTAMP DEFAULT CURRENT_TIMESTAMP, username VARCHAR(40), os VARCHAR(50),
              contry VARCHAR(5), gpu VARCHAR(50), cpu VARCHAR(60), ram VARCHAR (7), 
              win_version VARCHAR (20), time_c TIME, status VARCHAR(7))""".format(self.table_name)
            cursor.execute(sql_req)
        except mysql.connector.Error as error:
            print("Failed! Reason:\n{}".format(error))

    def add_user(self, *info_user):
        try:
            cursor = self.conn.cursor()
            cursor.execute('use {}'.format(self.base_name))
            info_user = info_user[0]
            sql_req = '''INSERT INTO {} (id, ip, username,os,contry,gpu,cpu,ram,win_version,time_c, status)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
  ON DUPLICATE KEY UPDATE time_c = %s'''.format(self.table_name)
            data = tuple([i for i in info_user] + [info_user[-2]])
            cursor.execute(sql_req, data)
            self.conn.commit()
        except mysql.connector.Error as error:
            print("Failed! Reason:\n{}".format(error))




    def show_all_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('use {}'.format(self.base_name))
            sql_req = """SELECT * FROM {}""".format(self.table_name)
            cursor.execute(sql_req)
            rows = cursor.fetchall()

            return rows
        except mysql.connector.Error as error:
            print("Failed! Reason:\n{}".format(error))



#a = SqlModule("185.139.70.8", 'PanelFavorite', 'gjenjgnew23ad', 3306, 'basestart', 'users')
#a.delete_base()
#a.create_base()
#a.create_table()
#qq=time.strftime('%H:%M:%S')
#data = [str(100000000000),'121.2.13.111','000', ' Windows 10 Pro', '7', 'NVIDIA GeForce GTX 1050 Ti', 'AMD Ryzen 5 1400 Quad-Core Processor', '7.93',
# '10.0.18362 18362', qq,'online']
#a.add_user(data)
#q=a.show_all_users()
#for i in q:
#    print(i)
