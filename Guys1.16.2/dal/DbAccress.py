# encoding: utf-8
# author: QiFuMin
# contact: 1248227761@qq.com
# site: https://www.jianshu.com/u/eaaae8e04a35
# software: PyCharm
# file: DbAccress.py
# time: 20-1-4 上午10:00
from __future__ import unicode_literals
import pymysql
import json

class DbController():
    def __init__(self):
        pass

    def creatConnect(self):
        conn = pymysql.connect(host="localhost", user="root",
                               password="123456", db="RootDB", port=3306, charset="utf8")
        cur = conn.cursor()
        return (conn, cur)


    def close(self,conn, cur):
        cur.close()
        conn.close()

    def get_max_id(self):
        """
        获取最后一个ID,如果没有就默认为10000
        :return:
        """
        conn, cur = self.creatConnect()
        sql = "select rootname from users order by id DESC limit 1"
        try:
            cur.execute(sql)
            result = cur.fetchone()
            user_id=int(result[0])
            self.close(conn,cur)
            return user_id+1
        except:
            self.close(conn, cur)
            return 10000


    def submit_information(self,user_info):
        """
        执行sql语句，存入相应数据库,成功返回true失败返回false
        :return: bool
        """
        conn, cur = self.creatConnect()
        s = '''insert into users (rootname,nickname, pwd, gender,style,birthday,tel,email)'''
        s += ''' values ("%s","%s","%s","%s","%s","%s", "%s","%s")''' % user_info
        # 判断用户昵称是否重复
        sql = "select nickname from users where nickname='%s'" % user_info[1]
        try:
            cur.execute(sql)
            result = cur.fetchone()  # 查不到返回None
        except:
            # 如果出错，依旧返回重复
            result = True
        if result:
            return 'R NameRepeat'
        try:
            cur.execute(s)
            conn.commit()
            print("insert_users is ok")
            return 'T ' + str(user_info[0])
        except:
            print("insert_users FILL")
            conn.rollback()
        self.close(conn, cur)
        return 'F Fail'


    def update_info(self,user_info):
        conn, cur = self.creatConnect()
        #判断用户是否想修改用户名
        sql_test="select nickname from users where rootname='%s'" % user_info[-1]
        cur.execute(sql_test)
        name_tup = cur.fetchone()
        #如果想修改用户名,就需要先判断新用户名是否被占用
        if user_info[0]!=name_tup[0]:
            # 判断用户昵称是否重复
            sql = "select nickname from users where nickname='%s'" % user_info[0]
            try:
                cur.execute(sql)
                result = cur.fetchone()  # 查不到返回None
            except:
                # 如果出错，依旧返回重复
                result = True
            if result:
                return 'R NameRepeat'

        #不修改密码
        sql_test = "select pwd from users where rootname='%s'" % user_info[-1]
        cur.execute(sql_test)
        pwd_tup = cur.fetchone()
        if user_info[1]=="点击设置新密码":
            user_info_list = list(user_info)
            user_info_list[1]= pwd_tup[0]
            user_info=tuple(user_info_list)
        print(user_info)

        #修改数据
        s = '''update users set '''
        s += '''nickname="%s", pwd="%s", gender="%s", style="%s",birthday="%s",tel="%s",email="%s" where rootname="%s"''' % \
             user_info
        try:
            cur.execute(s)
            conn.commit()
            print("update_info is ok")
            print(user_info[1])
            return 'T ' + 'change success'
        except:
            print("update_info FILL")
            conn.rollback()
        self.close(conn, cur)
        return 'R NameRepeat'


    # 在数据库中创建群组--Yuying
    def create_chat_group_in_db(self,friend2_id,group_id=1):
        conn, cur = self.creatConnect()
        s="insert into chat_group(g_id,u_id) values (%d,%d);"%(group_id,friend2_id)
        try:
            cur.execute(s)
            conn.commit()

        except:
            print("Fail to insert group member")
            conn.rollback()
        self.close(conn, cur)

    # 获取群组成员的id--Yuying
    def get_group_member_id(self,group_id):
        conn, cur = self.creatConnect()
        s="select u_id from chat_group where g_id=%s;"%group_id
        cur.execute(s)
        data = cur.fetchall()
        self.close(conn, cur)
        return data

    # 获取群信息
    def get_group_infor(self, group_id):
        conn, cur = self.creatConnect()
        s = "select * from groups where g_id=%s;" % group_id
        cur.execute(s)
        data = cur.fetchall()
        self.close(conn, cur)
        return data

    def save_chat_group_msg(self, sender_id, msg, group_id):
        conn, cur = self.creatConnect()
        print("准备保存", sender_id, msg, group_id)
        s = "insert into group_msg (u_id,message,g_id) values (%d,'%s',%d);" % (sender_id, msg, group_id)
        print(s)
        try:
            cur.execute(s)
            conn.commit()
        except Exception as e:
            print(e)
            print("Fail to insert group message")
            conn.rollback()
        self.close(conn, cur)


    # def main(self):
    #     try:
    #         conn, cur = self.creatConnect()
    #         self.create_users(conn)
    #         self.create_friends(conn)
    #         self.create_history(conn)
    #         conn.commit()
    #     except:
    #         conn = pymysql.connect(host="localhost", user="root",
    #                                password="369852", port=3306, charset="utf8")
    #         cur = conn.cursor()
    #         cur.execute('create database RootDB default character set utf8;')
    #         conn.commit()
    #         create_users(conn)
    #         create_friends(conn)
    #         create_history(conn)
    #         conn.commit()
    #     close(conn, cur)


    # def create_users(conn):
    #     s = 'create table users(\
    #     id int auto_increment primary key,\
    #     rootname int,\
    #     nickname varchar(20),\
    #     pwd varchar(32),\
    #     gender enum("男","女","保密"),\
    #     tel varchar(11),\
    #     address varchar(100),\
    #     email varchar(30),\
    #     birthday varchar(15),\
    #     avatar text,\
    #     style varchar(100),\
    #     onlinestatus enum("在线","离线") default "离线",\
    #     time timestamp default now(),\
    #     last_online timestamp default now())character set utf8;'
    #     cur = conn.cursor()
    #     try:
    #         cur.execute(s)
    #         conn.commit()
    #         print('users ok')
    #     except:
    #         print("create_users FILL")
    #         conn.rollback()
    # """
    # insert into users(rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus)
    #         values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")
    # """
    #
    # def insert_users(rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus):
    #     conn, cur = creatConnect()
    #     s = '''insert into users
    #         (rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus)
    #         values("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")''' % (rootname, nickname, pwd, gender, tel, address, email, birthday, avatar, style, onlinestatus)
    #     try:
    #         cur.execute(s)
    #         conn.commit()
    #         print("insert_users is ok")
    #     except:
    #         print("insert_users FILL")
    #         conn.rollback()
    #     close(conn, cur)


    # def updatestatus_users(rootname, status):
    #     conn, cur = creatConnect()
    #     s = "update users set onlinestatus='%s', last_online=now() where rootname='%s'" % (status, rootname)
    #     try:
    #         cur.execute(s)
    #         conn.commit()
    #         print("update_users is ok")
    #     except:
    #         print("updatestatus_users FILL")
    #         conn.rollback()
    #     close(conn, cur)


    def get_user_info(self, rootname):
        conn, cur = self.creatConnect()
        s = "select rootname,nickname,gender,tel,address,email,birthday,avatar,style,onlinestatus from users where rootname=%s" % rootname
        cur.execute(s)
        data = cur.fetchone()
        self.close(conn, cur)
        return data


    def verify_pwd(self,user_id):
        conn, cur = self.creatConnect()
        s = "select pwd from users where rootname='%s'" % user_id
        cur.execute(s)
        data = cur.fetchone()[0]
        self.close(conn, cur)
        return data


    def select_users(self,rootname):
        conn, cur = self.creatConnect()
        s = "select rootname,nickname,gender,tel,address,email,birthday,avatar,style,onlinestatus from users where rootname='%s'" % rootname
        cur.execute(s)
        data = cur.fetchone()
        self.close(conn, cur)
        return data

    def create_friends(self,conn):
        s = '''create table friends(
            id int auto_increment primary key,
            rootname int not null,
            f_rootname int not null)character set utf8;'''
        cur = conn.cursor()
        try:
            cur.execute(s)
            conn.commit()
            print('create_friends is ok')
        except:
            print("create_friends FILL")
            conn.rollback()

    def insert_friends(self,rootname, f_rootname):
        conn, cur = self.creatConnect()
        s = 'insert into friends(rootname,f_rootname) values("%s","%s"),("%s","%s")' % (
            rootname, f_rootname, f_rootname, rootname)
        try:
            cur.execute(s)
            conn.commit()
            print("insert_friends is ok")
        except Exception as e:
            print(e)
            conn.rollback()
        self.close(conn, cur)

    def delete_friends(self,rootname, f_rootname):
        conn, cur = self.creatConnect()
        s = 'delete from friends where (rootname="%s" and f_rootname="%s") or (rootname="%s" and f_rootname="%s")' %(
            rootname, f_rootname, f_rootname, rootname)
        try:
            cur.execute(s)
            conn.commit()
            print("delete_friends is ok")
        except Exception as e:
            print(e)
            conn.rollback()
        self.close(conn, cur)

    def select_friends(self,rootname):
        conn, cur = self.creatConnect()
        s = "select friends.f_rootname, users.nickname, users.style, users.avatar from friends,users where " \
            "friends.rootname='%s' " \
            "and users.rootname=friends.f_rootname;" % rootname
        cur.execute(s)
        data = cur.fetchall()
        self.close(conn, cur)
        return data

# """
#     create table group(g_id int auto_increment,g_name varchar(30) not null,style char,pic varchar(50));
# """



    # def create_history(conn):
    #     s = '''create table history(
    #     id int auto_increment primary key,
    #     rootname int not null,
    #     f_rootname int not null,
    #     record text,
    #     time timestamp default now())character set utf8;'''
    #     cur = conn.cursor()
    #     try:
    #         cur.execute(s)
    #         conn.commit()
    #         print('create_history ok')
    #     except:
    #         print("create_history FILL")
    #         conn.rollback()
    #
    #
    def insert_history(self,rootname, f_rootname, record):
        conn, cur = self.creatConnect()
        print("history:",rootname, f_rootname)
        s = "insert into history(rootname, f_rootname, record) values('%s', '%s', '%s')" % (
            rootname, f_rootname, record)
        try:
            cur.execute(s)
            conn.commit()
            print("insert_hist is ok")
        except:
            print("insert_history FILL")
            conn.rollback()
        self.close(conn, cur)


    def select_history(self, rootname, f_rootname):
        conn, cur = self.creatConnect()
        s = "select rootname,record from history where ((rootname = '%s')and(f_rootname = '%s')) or (( f_rootname = " \
            "'%s')and(rootname = '%s'))" % (
            rootname, f_rootname, rootname, f_rootname)
        cur.execute(s)
        data = cur.fetchall()
        self.close(conn, cur)
        return data

    def select_group_history(self):
        conn, cur = self.creatConnect()
        s = "select u_id,message from group_msg"
        cur.execute(s)
        data = cur.fetchall()
        self.close(conn, cur)
        return data


"""

create table group_msg(
u_id int,
message text,
date datetime default now(),
g_id int,
constraint g_fk foreign key(g_id) references chat_group(g_id));
    
insert into group_msg(u_id,message,g_id) values ( 10000,"吃了吗",1);

"""




"""
    create
    table
    groups(g_id
    int
    primary
    key
    auto_increment, g_name
    varchar(32)
    not null, style
    varchar(40), pic
    varchar(50));
    
    
    insert into groups values(1,'Group','We Are Team','/home/tarena/qifumin/code/mid_project1/mid_project/Guys1.15.1/static/teamimg.jpg');

"""

if __name__ == '__main__':
    mydbcontroller = DbController()
    aa = mydbcontroller.get_max_id()
    print(aa)
    print(type(aa))
