# encoding: utf-8
# author: QiFuMin
# contact: 1248227761@qq.com
# site: https://www.jianshu.com/u/eaaae8e04a35
# software: PyCharm
# file: ClientManager.py
# time: 20-1-4 上午9:51
from bll.setting import *
from socket import *
import time
from threading import Thread
import json


class ClientManagerController():
    def __init__(self, window):

        self.be_add_friend_info = []
        self.window = window
        self.sockfd = socket()

        # self.rootname = ''
        # 自己的信息
        self.myself_info = []
        # 被查询的好友的信息
        self.friend_info = []
        # 用与加Guys时存放所有好友信息
        self.friends_list = []
        self.create_connect()

    def create_connect(self):
        self.sockfd.connect(CLIENT_ADDR)
        for i in range(3):
            data = 'A'
            # 发送给服务端
            self.sockfd.send(data.encode())  # 转换为字节串

            data = self.sockfd.recv(1024).decode()
            print(data)
            if data == 'A':
                print("Server connection success")  # 打印字符串
                # self.start_send()
                # self.start_receive()
                break
        else:
            print('Server connection failure')
        # time.sleep(2)

    def sc_communication_protocol(self):
        """
        server&client通讯协议
        :return:
        """
        while True:
            print('开始接收反馈。。')
            data = self.receive_data()
            if data[0] == "M":
                print('接收到：>>>>',data[1])
                self.received_message(data[1])

            elif data[0] == "I":
                self.show_user_id(data[1])
                print('注册相应')

            elif data[0] == "Q":
                print('退出相应')

            elif data[0] == "S":
                self.received_file_message(data[1])
                # print('选择文件相应')

            elif data[0] == "C":
                self.save_be_add_friend_infor(data[1])

            elif data[0] == "H":
                self.show_chat_history(data[1])

            elif data[0] == "G":
                self.save_guys_friend_infor(data[1])

            elif data[0] == "E":
                self.save_myself_infor(data[1])

            elif data[0] == "J":
                self.save_friend_infor(data[1])


    def show_user_id(self,user_id):
        """
        用于信息提交成功后显示
        :return: None
        """

    def generate_user_id(self):
        """
        生成五位数从10000开始
        :return: 这个数字
        """
        pass

    def start_receive(self):
        self.receive_thread = Thread(target=self.sc_communication_protocol)  # 创建接收信息线程
        self.receive_thread.setDaemon(True)
        self.receive_thread.start()


    def receive_data(self):
        data = self.sockfd.recv(1024).decode()
        print('接收到：%s'%data)
        data = data.split(' ', 1)
        return data

    def send_data(self, data):
        """
        接受字符串类型
        :param data:
        :return:
        """
        self.sockfd.send(data.encode())

    def login(self,username,pwd):
        """
        L
        点击登录按钮时调用
        处理登录逻辑
        :return:
        """
        data = 'L '+username+' '+pwd
        self.send_data(data)
        return self.receive_data()


    def register(self):
        """
        R
        注册时调用
        :return:
        """

        self.send_data('R')

    def submit_information(self,data):
        """
        'I'
        注册时条用，将用户信息发送给服务器，得到验证后返回bool
        :param data:
        :return:bool
        """
        data = json.dumps(data)
        data = 'I ' + data
        self.send_data(data)
        back_data = self.sockfd.recv(128).decode()
        print(back_data)
        return back_data

    def update_info(self,data):
        '''
        给服务端发送用户更新的数据
        :param data: 新数据
        :return:
        '''
        data = json.dumps(data)
        data = 'UD ' + data
        self.send_data(data)
        back_data = self.sockfd.recv(128).decode()
        print(back_data)
        return back_data


    def do_quit(self):
        """
        Q
        退出按钮被点击时调用
        :return:
        """
        self.send_data('Q')
        # self.sockfd.close()
        # self.receive_thread.join()
        # 还需要关闭程序

    def select_file(self, sender,recever,file_path):
        """
        S
        选择文件按钮
        :return:
        """

        print(file_path)
        print(type(file_path))
        file_name = file_path.split('/')[-1]
        print(type(sender))
        print(type(recever))
        with open(file_path,'r') as f:
            file_data = f.read()
        # time.sleep(0.1)

        # self.save_file(file_name, b_data) # 这里为什么要保存文件呢？？？？这是发送端呀
        data = 'S ' + sender + ' ' + recever + ' ' + file_name + ' ' + file_data
        print(data)
        # self.send_data(data)
        # 发送二进制文件
        self.send_data(data)
        # self.sockfd.send(data.encode())

    def received_file_message(self, data):
        """
        处理接收到文件后的逻辑
        :param data:
        :return:
        """

        data = data.split(' ',2)
        sender_id = data[0]
        file_name = data[1]
        file_data = data[2]
        file_path = CLIENT_FILE_DIR +'/'+file_name  # 使用OS模块获取路径
        message = 'Received File:' + file_path
        self.save_file(file_path,file_data)
        self.window.text_browser_be_add(message, sender_id)

    def save_file(self,file_name,data):
        with open(file_name,'w') as f:
            f.write(data)

    def send_message(self,message,sender,receiver):
        """
        M
        发送消息按钮 ,发送的人，接受的人  数据格式为：指令，空格，发送者，空格，接收者，空格，消息
        :return:
        """
        if receiver == '1':
            message_data = 'YC ' + sender + ' ' + receiver + ' ' + message
        else:
            message_data = 'M '+sender+' '+receiver+' '+message
        self.send_data(message_data)

    def get_user_information(self,user_id):
        """
        获取自己的信息
        :param user_id:
        :return:
        """
        data = 'E ' + user_id
        self.send_data(data)

    def get_friend_information(self,friend_id):
        """
        I
        好友头像，显示好友信息
        :return:
        """
        data = 'J ' + friend_id
        self.send_data(data)

    def add_guys(self,add_guys_id):
        """
        G
        添加伙伴，成为群聊
        :return:
        """
        pass

    def add_guys_friends_list(self,user_id):
        """
        添加Guys时的请求好友列表，返回的时候需要判断
        :param user_id:
        :return:
        """
        data = 'G ' + user_id
        self.send_data(data)

    def friend_list_request(self,user_id):
        """
        去数据库中查询自己的好友列表信息
        :param user_id:
        :return: 好友列表
        """
        data = 'F ' + user_id
        self.send_data(data)
        # 发送后等待接受
        data = self.receive_data()
        data = json.loads(data[1])
        return data

    def add_friends(self,myself_id,target_id):
        """
        F
        添加好友
        :return:
        """
        data = 'B '+myself_id+' '+target_id
        self.send_data(data)
        print(data)

    def save_be_add_friend_infor(self,data):
        print(self.be_add_friend_info)
        self.be_add_friend_info = json.loads(data)
        print(self.be_add_friend_info)

    def save_guys_friend_infor(self,data):
        """
        原理同save_be_add_friend_infor一样，将获取到的信息先保存，然后在被ClientViewMainLogic中的函数将数据添加到页面控件上
        :param data:
        :return:
        """
        self.friends_list = json.loads(data)

    def save_myself_infor(self,data):

        self.myself_info = json.loads(data)
        print('save_myself_info')
        print(self.myself_info)

    def save_friend_infor(self,data):
        self.friend_info = json.loads(data)
        # print(self.myself_info)

    def del_friend(self,myself_id,target_id):
        data = 'D ' + myself_id + ' ' + target_id
        self.send_data(data)
        print(data)

    def received_message(self,data):
        """
        B
        处理获取到的消息,将数据格式处理好加到消息浏览框重
        :return:
        """
        data = data.split(' ',1)
        sender_id = data[0]
        message = data[1]
        # if self.window.friend_id == sender_id:
        self.window.text_browser_be_add(message, sender_id)

    def get_myself_information(self):
        """
        点击自己的头像，显示自己的信息
        :return:
        """
        pass

    def change_guys(self,myself_id, target_id):
        """
        好友列表中，选择好友
        :return:
        """
        print('change_guys',target_id)
        self.get_chat_history(myself_id, target_id)

    def get_chat_history(self, myself, friend):
        """
        查询与好友间的聊天信息
        :param myself: 自己的ID
        :param friend: 朋友的ID
        :return: 聊天记录列表
        """
        data = 'H ' + myself + ' ' +friend
        self.send_data(data)

    def show_chat_history(self,data):
        """
        将查询的历史消息都添加上去
        :param data:
        :return:
        """
        list_data = json.loads(data)
        for item in list_data:
            self.window.text_browser_be_add(item[1],str(item[0]))
        print(list_data)

    # 创建聊天的群组--Yuying
    def create_chat_group(self,be_add_guys_id):
        data = 'Y ' + str(be_add_guys_id)
        self.send_data(data)
        # print(be_add_guys_id)

    def get_state(self):
        """
        获取设置状态
        :return:
        """
        file_path = AUTO_LOGIN_STATE_FILE + '/state.txt'
        with open(file_path,'r') as f:
            result = f.read()
        print(result)
        print(type(result))
        return result

    def get_local_user_info(self):
        file_path = AUTO_LOGIN_STATE_FILE + '/password.txt'
        with open(file_path, 'r') as f:
            result = f.read().split(' ')
        user_id = result[0]
        password = result[1]
        print(user_id)
        print(password)
        return result

    def save_state(self,state):
        file_path = AUTO_LOGIN_STATE_FILE + '/state.txt'
        with open(file_path, 'w') as f:
            f.write(state)

    def save_local_user_info(self,user_id,password):
        file_path = AUTO_LOGIN_STATE_FILE + '/password.txt'
        data = user_id + ' ' + password
        with open(file_path, 'w') as f:
            f.write(data)


if __name__ == '__main__':
    guys_client = ClientManagerController()
    # guys_client.create_connect()
    # guys_client.cs_communication_protocol()

