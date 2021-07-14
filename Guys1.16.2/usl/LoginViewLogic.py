# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/1 20:33
# write_by:QiFuMin
# script_name:RegistViewLogin.py
import sys, re
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from usl.WinSource.LoginView import *


class MyLoginWindow(QMainWindow,Ui_ChatLoginWindow):
    def __init__(self,parent=None):
        super(MyLoginWindow, self).__init__(parent)
        self.setupUi(self)




    def close_login(self):
        """
        关闭登录界面
        :return:
        """
        self.close()

    def remb_num_and_auto_login(self):
        """
        勾选记住密码和自动登录情况
        :return:
        """
        with open('./login_config.txt','r') as f:
            rembpwd = f.readline()
            autologin = f.readline()
        if rembpwd =='1\n':
            self.remember_password.setChecked(True)
            f = open('./user_pwd.txt', 'r')
            user_or_telenum = f.readline()#正则一下去掉\n
            user_or_telenum = re.findall('\w+',user_or_telenum)[0]
            pwd = f.readline()
            f.close()
            self.name_txt.setText(user_or_telenum)
            self.password_txt.setText(pwd)
        if autologin =='1':
            self.auto_login.setChecked(True)

    def take_user_or_telenum(self):
        """
        获取用户名或手机号
        :return:
        """
        return self.name_txt.text()

    def take_pwd(self):
        """
        获取密码
        :return:
        """
        return self.password_txt.text()

    def wrong_nickname_or_telenum_or_pwd(self):
        """
        用户名或者密码不正确
        :return:
        """
        QMessageBox.warning(self, 'Waring!', "用户名/手机号或密码不正确！")

    def nickname_or_telenum_empty(self):
        """
        用户名/手机号不能为空
        :return:
        """
        QMessageBox.warning(self, 'Waring!', "用户名/手机号不能为空！")

    def pwd_empty(self):
        QMessageBox.warning(self, 'Waring!', "登录密码不能为空！")

    def logining(self):
        # QMessageBox.warning(self, 'Note!', "正在登录，请稍后！")
        msg = QMessageBox.question(self, 'Note!', '正在自动登录，是否继续？',
                             QMessageBox.Yes, QMessageBox.No)
        return msg

    def fail_login(self):
        QMessageBox.warning(self, 'Note!', "对不起，登录失败，请重试！")


# ----------------------------------------
#     def launch(self):
#         if self.autologin():
#             return
#
#         else:
#             self.lg.show()
#             self.login_or_register()
#             self.rg.create_confirmnum()

    # def login_or_register(self):
    #     """
    #     登录还是注册
    #     :return:
    #     """
    #     self.lg.login.clicked.connect(self.login_procedure)
    #     self.lg.register_2.clicked.connect(self.register_procedure)

    def autologin(self):
        """
        判断登录时是否记住密码和是否自动登录
        :return:
        """
        if self.lg.auto_login.isChecked():
            if self.lg.remember_password.isChecked():
                f = open('./user_pwd.txt', 'r')
                user_or_telenum = f.readline()#[0:10]
                user_or_telenum = re.findall('\w+', user_or_telenum)[0]
                pwd = f.readline()#[0:]
                f.close()
                msg = self.lg.logining()
                if msg == QMessageBox.Yes:
                    dic_login_info = {"user_or_telenum":user_or_telenum,"pwd":pwd}#上传服务器登录信息
                    # 执行登录程序，查询数据库,若查到返回'OK'
                    data = 'OK'
                    if data == 'OK':#登录成功：
                        #展现聊天界面
                        print("登录成功")
                        return True
                    else:
                        self.lg.fail_login()
                        return False
                else:
                    return

    def adapt_loginconfig_and_userpwd(self,user_or_telenum,pwd):
        """
        登录成功后改写登录设置（记住密码、自动登录、用户名、密码）
        """
        f = open('./login_config.txt', 'w')

        if self.lg.remember_password.isChecked() == True:
            f.write('1\n')
        else:
            f.write('0\n')

        if self.lg.auto_login.isChecked() == True:
            f.write('1')
        else:
            f.write('0')
        f.close()


        if self.lg.remember_password.isChecked() == True:
            t = open('./user_pwd.txt', 'w')
            t.write(user_or_telenum + '\n' + pwd)
            t.close()

    def login_procedure(self):
        """
        进行登录进程，先判断登录信息是否为空
        :return:
        """

        # if self.judge_logincofig():
        #     return
        # else:
        user_or_telenum = self.lg.take_user_or_telenum()#[0:11]
        pwd = self.lg.take_pwd()#[0:]
        if not user_or_telenum:
            self.lg.nickname_or_telenum_empty()
            return 1

        if not pwd:
            self.lg.pwd_empty()
            return 1

        if  (re.findall(r'^1[0-9]{10}$',user_or_telenum) or re.findall(r'^([a-z]|[A-Z])(\w*)$',user_or_telenum)) and \
                re.findall(r'^([a-z]|[A-Z])(\w{5})(\w*)$',pwd):
            #以手机号登录或用户名以字母开头，并且密码以字母开头，那么执行登录，否则报错
            print('登录')
            self.lg.logining()
            dic_login_info = {"user_or_telenum": user_or_telenum, "pwd": pwd}
            # 上传服务器登录信息,查询数据库，若存在返回‘OK’
            data = 'OK'
            if data == 'OK':#登录成功
                self.adapt_loginconfig_and_userpwd(user_or_telenum,pwd)
                #关闭“正在登录”提示self.lg.logining()
                self.lg.close_login()#登录成功后，关闭登录界面
                #显示聊天界面
            else:
                self.lg.fail_login()
        else:
            self.lg.wrong_nickname_or_telenum_or_pwd()



if __name__ == '__main__':
    app=QApplication(sys.argv)
    myWin=MyLoginWindow()
    myWin.show()
    sys.exit(app.exec_())
