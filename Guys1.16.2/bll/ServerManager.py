# encoding: utf-8
# author: QiFuMin
# contact: 1248227761@qq.com
# site: https://www.jianshu.com/u/eaaae8e04a35
# software: PyCharm
# file: ServerManager.py
# time: 20-1-4 上午9:53
from bll.setting import *
from socket import *
from select import *
import json
import time
import hashlib
from dal.DbAccress import DbController

class ServerManagerController():
    def __init__(self):
        self.my_db_controller = DbController()

        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sockfd.bind(SERVER_ADDR)
        self.sockfd.listen(5)

        self.rlist = []
        self.wlist = []
        self.xlist = []

        self.all_online_clients = {}  # 记录在线的客户端的套接字
        self.chat_connects = {}  # 将聊天双方的套接字绑定在一起

        # 读IO列表，等待就绪的
        self.rlist.append(self.sockfd)
        # 为什么放到异常列表呢？？？？？？
        # self.xlist.append(self.sockfd)

    def run(self):
        while True:
            print("等待root客户端连接...")
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            print(rs)
            for r in rs:
                if r is self.sockfd:
                    connfd, addr = self.sockfd.accept()
                    print("有root客户端连接:", addr)
                    self.rlist.append(connfd)
                else:
                    # 判断接受的类型
                    self.handler(r)
            for x in xs:
                if x is self.sockfd:
                    x.close()


    def handler(self,connfd):
        data = connfd.recv(1024).decode()
        print(data)

        if not data:
            self.rlist.remove(connfd)
            print('移除')
            connfd.close()
            print('关闭')
        else:
            data = data.split(' ', 1)

            if data[0] == 'A':
                print("handler>data:", data)
                connfd.send(b'A')
                print('通讯成功')

            elif data[0] == 'L':
                print("handler>data:", data)
                print('登录请求')
                self.verify_pwd(connfd,data[1])

            elif data[0] == 'M':
                # 接受消息，调用转发函数
                print("handler>data:", data)
                print(data)
                self.message_route(connfd,data[1])

            elif data[0] == 'R':
                print("handler>data:", data)

                print(data)
                self.send_data(connfd,'R')

            elif data[0] == 'S':
                print("handler>data:", data)

                print(data)
                self.file_message_route(connfd,data[1])

            elif data[0] == 'Q':
                print("handler>data:", data)

                print(data)
                self.send_data(connfd,'Q')

            elif data[0] == 'I':
                # 注册提交的数据
                print("handler>data:", data)
                print(data)
                self.submit_information(connfd,data[1])

            elif data[0] == 'F':
                # 获取好友列表的请求
                print("handler>data:", data)
                print(data)
                self.get_friend_list(connfd,data[1])

            elif data[0] == 'B':
                # 添加好友请求
                print("handler>data:", data)
                print(data)
                self.add_friends(connfd,data[1])

            elif data[0] == 'D':
                #
                print("handler>data:", data)
                print(data)
                self.del_friends(connfd, data[1])

            elif data[0] == 'H':
                #
                print("handler>data:", data)
                print(data)
                self.get_chat_history(connfd, data[1])

            elif data[0] == 'G':
                # 获取好友列表的请求
                print("handler>data:", data)
                print(data)
                self.guys_friend_list(connfd, data[1])

            elif data[0] == 'E':
                print("handler>data:", data)
                print(data)
                self.get_user_infor(connfd, data[1])

            elif data[0] == 'J':
                print("handler>data:", data)
                print(data)
                self.get_friend_infor(connfd, data[1])

            elif data[0] == 'Y':
                print("handler>data:", data)
                print(data)
                self.create_chat_group_process(data[1])

            elif data[0] == 'YC':
                print("handler>data:", data)
                print(data)
                self.create_chat_group_msg(data[1])

            elif data[0] == 'UD':
                self.update_info(connfd, data[1])

    # 创建群组，成员存进数据库-Yuying
    def create_chat_group_process(self, new_add_person):
        new_add_person = int(new_add_person)
        self.my_db_controller.create_chat_group_in_db(new_add_person)

    def create_chat_group_msg(self, data):
        # 这里是切割两下
        data = data.split(' ',2)
        sender_id = data[0]
        group_id = data[1]
        msg = data[2]
        member_list = list(self.my_db_controller.get_group_member_id(group_id))
        for i in member_list:
            if str(i[0]) == sender_id:
                continue
            elif i[0] in self.all_online_clients:
                # print("在线的好友",self.all_online_clients)
                message = 'M ' + sender_id + ' ' + msg
                member_connfd = self.all_online_clients[i[0]]
                self.send_data(member_connfd, message)
        self.save_chat_group_msg_to_db(int(sender_id), msg, int(group_id))

    # 群消息存储到数据库中group_message表--Yuying
    def save_chat_group_msg_to_db(self, sender_id, msg, group_id):
        self.my_db_controller.save_chat_group_msg(sender_id, msg, group_id)

    def get_user_infor(self,connfd, user_id):

        response_data = self.my_db_controller.get_user_info(user_id)

        json_data = json.dumps(response_data)
        data = 'E ' + json_data
        self.send_data(connfd, data)

    def get_friend_infor(self, connfd, friend_id):

        response_data = self.my_db_controller.get_user_info(friend_id)
        json_data = json.dumps(response_data)
        data = 'J ' + json_data
        self.send_data(connfd, data)

    def add_friends(self,connfd,data):
        """
        data的格式为自己的ID空格目标好友的ID
        :param connfd:
        :param data:
        :return:
        """
        data = data.split(' ')
        self.my_db_controller.insert_friends(data[0],data[1])
        response_data = self.my_db_controller.get_user_info(data[1])
        data = 'C ' + json.dumps(response_data)
        self.send_data(connfd, data)

    def del_friends(self,connfd,data):
        data = data.split(' ')
        self.my_db_controller.delete_friends(data[0], data[1])


    def generate_user_id(self):
        """
        生成新注册用户的ID
        :return:
        """
        return self.my_db_controller.get_max_id()

    def submit_information(self,connfd,data):
        """
        :param data:
        :return: bool
        """
        # if self.my_db_controller.submit_information(data):
        #     return self.send_data(connfd,)# 这里没写完
        # else:
        #     return self.send_data(connfd, )

        print(data)

        data = json.loads(data)
        rootname = self.generate_user_id()
        pwd = self.change_passwd(data['pwd'])
        user_data = (
            rootname,
            data['username'],
            pwd,
            data['gender'],
            data['signature'],
            data['birthday'],
            data['phone'],
            data['email'],
        )
        result = self.my_db_controller.submit_information(user_data)
        print(result)
        self.send_data(connfd, result)


    def update_info(self, connfd, data):
        data = json.loads(data)
        #不修改密码,就不加密
        if data['pwd']=="点击设置新密码":
            pwd = data['pwd']
        else:
            pwd = self.change_passwd(data['pwd'])
        print(pwd)
        user_data = (
            data['username'],
            pwd,
            data['gender'],
            data['signature'],
            data['birthday'],
            data['phone'],
            data['email'],
            data['rootname']
        )
        print('**********')
        print(user_data)
        result = self.my_db_controller.update_info(user_data)
        print(result)
        self.send_data(connfd, result)


    def change_passwd(self,passwd):
        # 生产hash对象
        hash = hashlib.md5("*#06#".encode())  # 加盐生产对象
        # 对密码进行加密
        hash.update(passwd.encode())
        # 提取加密后的密码
        return hash.hexdigest()


    def verify_pwd(self,conncd,data):
        data = data.split(' ')
        user_id = int(data[0])
        user_pwd = data[1]
        db_user_pwd = self.my_db_controller.verify_pwd(user_id)
        if db_user_pwd == self.change_passwd(user_pwd):
            data = 'L '+'T'
            self.user_online(conncd,user_id)
        else:
            data = 'L '+'F'
        self.send_data(conncd,data)

    def user_online(self,conncd,user_id):
        """

        :param conncd:
        :param user_id:
        :return:
        """
        self.all_online_clients[user_id] = conncd

    def user_offline(self,user_id):
        """

        :param conncd:
        :param user_id:
        :return:
        """
        del self.all_online_clients[user_id]

    def message_route(self,connfd,data):
        """
        这里data数据格式是去掉了指令后的，后半部分
        :param data:
        :return:
        """
        data = data.split(' ',2)
        sender_id = data[0]
        receiver_id = data[1]
        message = data[2]
        # print(user_id)
        # print(message)
        self.save_chat_records(sender_id,receiver_id,message)
        if receiver_id in self.all_online_clients:
            target_socket = self.all_online_clients[receiver_id]
            data = 'M '+sender_id+' '+message
            self.send_data(target_socket, data)
        else:
            data = 'M ' + sender_id + ' ' + 'Friend is outline'
            self.send_data(connfd, data)

    def file_message_route(self,connfd,data):
        """
               这里data数据格式是去掉了指令后的，后半部分
               :param data:
               :return:
               """
        data = data.split(' ', 3)
        sender_id = data[0]
        receiver_id = data[1]
        file_name = data[2]
        # 这里还有data[3]为文件内容
        file_data = data[3]
        # 还要再配合静态文件里面规定的路径，将文件统一保存在某个位置
        file_path = SERVER_FILE_DIR + '/' + file_name  # 使用OS模块获取路径
        self.save_file(file_path, file_data)
        self.save_chat_records(sender_id, receiver_id, file_name)
        if receiver_id in self.all_online_clients:
            target_socket = self.all_online_clients[receiver_id]
            data = 'S ' + sender_id + ' ' + file_name + ' ' + file_data
            self.send_data(target_socket, data)
        else:
            data = 'M ' + sender_id + ' ' + 'Friend is outline'
            self.send_data(connfd, data)

    def save_file(self, file_name, data):
        with open(file_name, 'w') as f:
            f.write(data)

    def save_chat_records(self, sender, receiver, message):
        self.my_db_controller.insert_history(sender, receiver, message)

    def get_chat_history(self,connfd,data):
        """
        查询出好友消息然后转为json发回去
        :param connfd:
        :param data:
        :return:
        """
        data = data.split(' ',1)
        myself_id = data[0]
        friend_id = data[1]
        if friend_id == '1':
            history_message = self.my_db_controller.select_group_history()
        else:
            history_message = self.my_db_controller.select_history(myself_id,friend_id)
        json_data = json.dumps(history_message)
        response_data = 'H ' + json_data
        self.send_data(connfd,response_data)

    def get_friend_list(self,connfd,user_id):
        """
        得到查询好友列表的指令后调用，去数据库重查询好友的id,好友的昵称，好友的签名，好友的头像
        :param connfd: 用户的套接字
        :param user_id: 用户的ID
        :return:
        """
        frind_list = self.my_db_controller.select_friends(user_id)
        group_info = self.my_db_controller.get_group_infor(1)[0]
        frind_list = list(frind_list)
        frind_list.append(group_info)
        data = 'F ' + json.dumps(frind_list)
        self.send_data(connfd,data)

    def guys_friend_list(self,connfd,user_id):
        """
        得到查询好友列表的指令后调用，去数据库重查询好友的id,好友的昵称，好友的签名，好友的头像
        :param connfd: 用户的套接字
        :param user_id: 用户的ID
        :return:
        """
        frind_list = self.my_db_controller.select_friends(user_id)
        data = 'G ' + json.dumps(frind_list)
        self.send_data(connfd,data)

    def receive_data(self, connfd):
        return connfd.recv(1024).decode()

    def send_data(self, connfd, data):
        # time.sleep(3)
        # data = data +' '
        connfd.send(data.encode())
        print('发送成功：%s'%data)


if __name__ == '__main__':
    guys_server = ServerManagerController()
    guys_server.run()
