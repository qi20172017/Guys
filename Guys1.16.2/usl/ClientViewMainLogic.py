# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/3 22:36
# write_by:QiFuMin
# script_name:ClientMainView.py
from usl.AddFriendViewLogic import MyAddFriendWindow
from usl.AddGuysViewLogic import MyAddGuysWindow
from usl.FrientInforViewLogic import MyFrientInforWindow
from usl.IsQuitViewLogic import MyIsQuitWindow
from usl.ChatViewLogic import MyChatWindow
from usl.LoginViewLogic import MyLoginWindow
from usl.RegistViewLogic import MyRegistWindow
from usl.UserIdViewLogic import MyUserIdWindow
from usl.UserInforViewLogic import MyUserInforWindow
from usl.IsFriendDelLogic import MyIsFriendDelWindow
from usl.IsAutoLoginViewLogin import MyIsAutoLoginWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QThread, pyqtSignal, QObject

import sys
from bll.ClientManager import ClientManagerController
import time
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


class MyClientMainView():
    def __init__(self):
        # 这里是注册中的各个字段，还要添加
        self.nick_name = None
        self.pwd_text = None
        self.gender = None
        self.birthday = None
        self.signature = None
        self.phone = None
        self.email = None

        # 表示文本框输入的消息
        self.message = None

        # 记录自动登录与否的状态
        self.state = '3'

        # 本客户短登录的ID
        self.myself_id = None
        self.friend_id = None

        self.friend_list = []
        # self.be_add_friend_infor = ['as','we','dee','dsfds']

        # 实例化控制器
        self.client_manager_controller = ClientManagerController(self)

        # 实例化所有窗口
        self.addFriendWin = MyAddFriendWindow()
        self.addGuysWin = MyAddGuysWindow()
        self.friendInforWin = MyFrientInforWindow()
        self.isQuitWin = MyIsQuitWindow()
        self.isFriendDelWin = MyIsFriendDelWindow()
        self.chatWin = MyChatWindow()
        self.loginWin = MyLoginWindow()
        self.registWin = MyRegistWindow()
        self.useridWin = MyUserIdWindow()
        self.userInforWin = MyUserInforWindow()
        self.isAutoLoginWin = MyIsAutoLoginWindow()

        # 登录窗口的操作
        self.loginWin.btn_login.clicked.connect(self.verify_pwd)
        self.loginWin.btn_regist.clicked.connect(self.regist_ID)
        self.loginWin.chk_auto_login.stateChanged.connect(self.auto_login_or_not)
        self.loginWin.chk_remenber_pwd.stateChanged.connect(self.auto_login_or_not)

        # 注册窗口的操作
        self.registWin.verify_btn.clicked.connect(self.submit_information)
        self.registWin.affirm_btn.clicked.connect(self.get_security_code)
        # ID显示窗口的操作
        self.useridWin.to_login_btn.clicked.connect(self.id_to_login)

        # 聊天窗口的操作
        self.chatWin.user_infor_btn.clicked.connect(self.get_user_infor)
        self.chatWin.add_friend_btn.clicked.connect(self.open_add_friend_win)
        self.chatWin.add_guys_btn.clicked.connect(self.add_guys)
        self.chatWin.friend_infor_btn.clicked.connect(self.get_friend_infor)
        self.chatWin.quit_btn.clicked.connect(self.open_is_quit_win)
        self.chatWin.select_file_btn.clicked.connect(self.select_file)
        self.chatWin.send_massage_btn.clicked.connect(self.send_message)
        self.chatWin.friend_list.clicked.connect(self.change_guys)
        self.chatWin.friend_list.doubleClicked.connect(self.open_is_friend_del_win)
        # self.chatWin.massage_btn.clicked.connect(self.del_friend)

        # 退出确认窗口
        self.isQuitWin.yes_btn.clicked.connect(self.quit_program)
        self.isQuitWin.cancle_btn.clicked.connect(self.quit_isQuit_win)

        # 删除好友确认窗口
        self.isFriendDelWin.yes_btn.clicked.connect(self.del_friend)
        self.isFriendDelWin.cancle_btn.clicked.connect(self.close_is_friend_del_win)

        # 加好友窗口
        self.addFriendWin.add_btn.clicked.connect(self.add_friend)

        # 好友信息窗口
        # 这个好友信息先不做的

        # 自己信息窗口可更改自己信息
        self.userInforWin.verify_btn.clicked.connect(self.update_user_info)

        # 三五成群窗口
        self.addGuysWin.friend_list.doubleClicked.connect(self.create_group)

        # 自动登录窗口
        self.isAutoLoginWin.cancle_btn.clicked.connect(self.dis_auto_login)

        self.timer = QTimer()  # 初始化一个定时器
        # self.timer.stop()
        # self.timer.timeout.connect(self.verify_pwd())  # 计时结束调用operate()方法

        # self.timer.start(2000)  # 设置计时间隔并启动


    # 这个窗口内部双击添加

    def print_hello(self):
        print('hello')

    def login_ID(self):
        """
        账号登录
        :return:
        """
        self.open_login_win()
        result = self.client_manager_controller.get_state()
        user_info = self.client_manager_controller.get_local_user_info()
        self.timer.timeout.connect(self.verify_pwd)

        if result == '1':
            print('记住密码，输入框显示账号与密码')
            # user_info = self.client_manager_controller.get_local_user_info()
            self.loginWin.txt_user.setText(user_info[0])
            self.loginWin.txt_pwd.setText(user_info[1])
            self.loginWin.chk_remenber_pwd.setChecked(True)
            self.loginWin.chk_auto_login.setChecked(False)
        elif result == '2':
            print('弹出自动登录窗口，自动登录')
            # user_info = self.client_manager_controller.get_local_user_info()
            self.loginWin.txt_user.setText(user_info[0])
            self.loginWin.txt_pwd.setText(user_info[1])
            self.loginWin.chk_remenber_pwd.setChecked(True)
            self.loginWin.chk_auto_login.setChecked(True)
            self.auto_login()
        elif result == '3':
            print('只显示以前的账号，不显示密码')
            self.loginWin.txt_user.setText(user_info[0])
            self.loginWin.chk_remenber_pwd.setChecked(False)
            self.loginWin.chk_auto_login.setChecked(False)

    def auto_login(self):
        self.open_is_auto_login_win()
        self.timer.start(2000)


    def dis_auto_login(self):
        self.close_is_auto_login_win()
        self.timer.stop()

    def regist_ID(self):
        """
        注册用户
        :return:
        """
        self.open_regist_win()

    def id_to_login(self):
        """
        经过注册得到ID后转向登录
        :return:
        """
        self.close_regist_win()
        self.close_userid_win()

    def auto_login_or_not(self):
        """
        0 表示取消
        2 表示选中
        :return:
        """
        auto_state = self.loginWin.chk_auto_login.checkState()
        rem_state = self.loginWin.chk_remenber_pwd.checkState()
        if auto_state == 0:
            if rem_state == 0:
                self.state = '3'
            elif rem_state == 2:
                self.state = '1'
        elif auto_state == 2:
            self.loginWin.chk_remenber_pwd.setChecked(True)
            self.state = '2'
        print(self.state)
        print(type(self.state))


    def get_user_infor(self):
        """
        点击用户头像，显示个人信息
        :return:
        """
        self.client_manager_controller.get_user_information(self.myself_id)
        # 加一点延迟，等待数据加载
        time.sleep(0.1)
        self.open_user_infor_win()
        my_info = self.client_manager_controller.myself_info
        print('-------')
        print(my_info)
        self.userInforWin.id_number.setText(str(my_info[0]))
        self.userInforWin.nc_Text.setText(my_info[1])
        self.userInforWin.pwd_Text.setText('点击设置新密码')
        self.select_gender(my_info[3])
        self.userInforWin.phone_Text.setText(my_info[4])
        self.userInforWin.email_Text.setText(my_info[5])
        self.userInforWin.birthday_Text.setText(my_info[6])
        # self.userInforWin.nc_Text.setText(my_info['avatar'])
        self.userInforWin.gx_Text.setText(my_info[7])

    # 其他信息继续添加进来就行了

    def select_gender(self, gender):
        if gender == '男':
            self.userInforWin.gender_btn1.setChecked(True)
        elif gender == '女':
            self.userInforWin.gender_btn2.setChecked(True)

    def get_friend_infor(self):
        self.client_manager_controller.get_friend_information(self.friend_id)
        # 加一点延迟，等待数据加载
        time.sleep(0.1)
        self.open_friend_infor_win()
        friend_info = self.client_manager_controller.friend_info
        self.friendInforWin.id_number.setText(str(friend_info[0]))
        self.friendInforWin.nc_name.setText(friend_info[1])
        self.friendInforWin.signture.setText(friend_info[8])
        self.friendInforWin.gender.setText(friend_info[2])
        self.friendInforWin.birthday.setText(friend_info[6])
        self.friendInforWin.phone_num.setText(friend_info[3])
        self.friendInforWin.email.setText(friend_info[5])

    def verify_pwd(self):
        """
        登录界面获取输入的账号密码验证
        成功后调用主页面
        :return:
        """
        # 关闭定时器 保证自验证一次
        self.timer.stop()
        self.close_is_auto_login_win()

        username = self.loginWin.txt_user.text()
        print(username)
        print(type(username))
        pwd = self.loginWin.txt_pwd.text()
        print(pwd)
        print(type(pwd))
        self.client_manager_controller.save_state(self.state)
        self.client_manager_controller.save_local_user_info(str(username),str(pwd))
        state = self.client_manager_controller.login(username, pwd)
        print('dddd', state)
        if state[1] == 'T':
            self.close_login_win()
            self.open_chat_win()

            self.myself_id = username
            self.chatWin.user_infor_btn.setText(self.myself_id)
            self.friend_list = self.client_manager_controller.friend_list_request(self.myself_id)
            self.chatWin.create_frient_list(self.friend_list)

            self.client_manager_controller.start_receive()

        # time.sleep(3)
        # self.client_manager_controller.friend_list_request(self.myself_id)
        else:  # 还需要添加行为
            pass

    def submit_information(self):
        """
        注册界面提交信息，格式正确后，跳出账号页面   收集好数据，将数据提交给逻辑
        :return:
        """
        self.pwd_text = self.registWin.pwd_Text.text()
        self.nick_name = self.registWin.nc_Text.text()
        self.birthday = self.registWin.birthday_Text.text()
        self.signature = self.registWin.gx_Text.text()
        self.phone = self.registWin.phone_Text.text()
        self.email = self.registWin.email_Text.text()
        print(self.pwd_text)
        if self.registWin.gender_m_btn.isChecked():
            self.gender = '男'
        elif self.registWin.gender_w_btn.isChecked():
            self.gender = '女'

        # 整合注册数据
        data = {
            'username': self.nick_name,
            'pwd': self.pwd_text,
            'gender': self.gender,
            'signature': self.signature,
            'birthday': self.birthday,
            'phone': self.phone,
            'email': self.email
        }

        result = self.client_manager_controller.submit_information(data).split(" ")
        if result[0] == 'R':
            self.registWin.name_repeat()
        elif result[0] == 'T':
            # 注册成功,显示用户ID
            self.open_userid_win()
            self.useridWin.add_val(result[1])
        elif result[0] == 'F':
            self.registWin.register_error()

    def update_user_info(self):
        """
        更新数据，和上面submit_information很想，只是从不同页面读取数据 等淡汉阳的注册
        :return:
        """
        self.root_name = self.userInforWin.id_number.text()
        self.pwd_text = self.userInforWin.pwd_Text.text()
        print(self.pwd_text)
        self.nick_name = self.userInforWin.nc_Text.text()
        self.birthday = self.userInforWin.birthday_Text.text()
        self.signature = self.userInforWin.gx_Text.text()
        self.phone = self.userInforWin.phone_Text.text()
        self.email = self.userInforWin.email_Text.text()
        print(self.pwd_text)
        if self.userInforWin.gender_btn1.isChecked():
            self.gender = '男'
        elif self.userInforWin.gender_btn2.isChecked():
            self.gender = '女'

        # 整合修改数据
        data = {
            'rootname': self.root_name,
            'username': self.nick_name,
            'pwd': self.pwd_text,
            'gender': self.gender,
            'signature': self.signature,
            'birthday': self.birthday,
            'phone': self.phone,
            'email': self.email
        }

        result = self.client_manager_controller.update_info(data).split(" ")
        print(result[0])
        if result[0] == 'R':
            self.userInforWin.change_name_repeat()
        elif result[0] == 'T':
            # 修改成功,关闭信息窗口
            self.userInforWin.change_success()
            self.userInforWin.close()

        print('update_user_ifon')

    def get_security_code(self):
        """
        注册界面调用模块发送验证码
        :return:
        """
        pass

    def add_friend(self):
        """
        添加好友功能，从界面获取账号，调用逻辑添加
        :return:
        """
        target_id = self.addFriendWin.id_edit.text()
        self.client_manager_controller.add_friends(self.myself_id, target_id)
        time.sleep(0.5)
        self.chatWin.add_to_list(self.client_manager_controller.be_add_friend_info)

    def del_friend(self):
        """
        连接双击事件，先获取当前被点击的item然后得到此项目的行数，然后删除此行
        :return:
        """
        self.close_is_friend_del_win()
        target_id = self.chatWin.get_item_id()
        self.client_manager_controller.del_friend(self.myself_id, target_id)

        print(target_id)
        row_num = self.chatWin.get_item_row()
        self.chatWin.friend_list.takeItem(row_num)
        self.change_guys()
        print(row_num)

    def change_guys(self):
        """
        改变聊天的对象
        :return:
        """
        self.friend_id = self.chatWin.get_item_id()
        self.chatWin.friend_infor_btn.setText(self.friend_id)
        self.chatWin.message_history.clear()
        self.client_manager_controller.change_guys(self.myself_id, self.friend_id)

    # print(self.friend_id)
    # print(type(self.friend_id))

    def add_guys(self):
        """
        查出数据，得到列表
        :return:
        """
        self.open_add_guys_win()
        self.addGuysWin.friend_list.clear()
        self.client_manager_controller.add_guys_friends_list(self.myself_id)
        time.sleep(0.1)
        self.addGuysWin.create_frient_list(self.client_manager_controller.friends_list)
        self.addGuysWin.friend_list.doubleClicked.connect(self.send_add_guys_signal)

    def create_group(self):
        """
        建群的逻辑--Yuying
        调用函数create_chat_group(self.id,friend1.id,friend2.id)
        :return:
        """
        be_add_guys_id = self.addGuysWin.get_item_id()
        # print(be_add_guys_id)
        self.client_manager_controller.create_chat_group(be_add_guys_id)


    def send_add_guys_signal(self):
        """
        被出发后，从页面读取被点击ID，调用逻辑，实行添加
        :return:
        """
        add_guys_id = self.addGuysWin.get_item_id()
        self.client_manager_controller.add_guys(add_guys_id)


    def send_message(self):
        """
        先从输入框获取文本
        聊天界面调用逻辑发送消息
        :return:
        """
        self.message = self.chatWin.message_edit.toPlainText()
        self.text_browser_be_add(self.message, self.myself_id)
        self.chatWin.message_edit.clear()
        self.client_manager_controller.send_message(self.message, self.myself_id, self.friend_id)

    # print(self.message)

    def text_browser_be_add(self, message, who=None):
        """
        向聊天框中添加内容，发送时调用，接受到消息也调用 判断一下是谁发的
        :param message:
        :return:
        """
        message = who + ':' + message
        self.chatWin.message_history.append(message)

    def select_file(self):
        """
        聊天界面打开文件筐，选择文件
        :return:
        """
        file_path = QFileDialog.getOpenFileName()[0]
        print('lujing:', file_path)
        # 添加文件发送路径
        self.text_browser_be_add(file_path, self.myself_id)
        # 发送文件
        self.client_manager_controller.select_file(self.myself_id, self.friend_id, file_path)

    def quit_isQuit_win(self):
        """
        点击取消，自己窗口关闭
        :return:
        """
        self.close_is_quit_win()

    def quit_program(self):
        """
        关闭程序，退出
        :return:
        就是聊天界面退出
        """
        self.close_chat_win()
        self.close_is_quit_win()

    def open_is_auto_login_win(self):
        self.isAutoLoginWin.show()

    def open_login_win(self):
        self.loginWin.show()

    def open_regist_win(self):
        self.registWin.show()

    def open_userid_win(self):
        self.useridWin.show()

    def open_chat_win(self):
        self.chatWin.show()

    def open_user_infor_win(self):
        self.userInforWin.show()

    def open_add_friend_win(self):
        self.addFriendWin.show()

    def open_add_guys_win(self):
        self.addGuysWin.show()

    def open_friend_infor_win(self):
        self.friendInforWin.show()

    def open_is_quit_win(self):
        self.isQuitWin.show()

    def open_is_friend_del_win(self):
        self.isFriendDelWin.show()

    def close_is_auto_login_win(self):
        self.isAutoLoginWin.close()

    def close_login_win(self):
        self.loginWin.close()

    def close_regist_win(self):
        self.registWin.close()

    def close_userid_win(self):
        self.useridWin.close()

    def close_chat_win(self):
        self.chatWin.close()

    def close_user_infor_win(self):
        self.userInforWin.close()

    def close_add_friend_win(self):
        self.addFriendWin.close()

    def close_add_guys_win(self):
        self.addGuysWin.close()

    def close_friend_infor_win(self):
        self.friendInforWin.close()

    def close_is_quit_win(self):
        self.isQuitWin.close()

    def close_is_friend_del_win(self):
        self.isFriendDelWin.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    client_main_win = MyClientMainView()
    client_main_win.login_ID()
    sys.exit(app.exec_())
