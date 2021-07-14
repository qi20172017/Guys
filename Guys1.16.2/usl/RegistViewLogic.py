# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/1 20:33
# write_by:QiFuMin
# script_name:RegistViewLogin.py
import sys, re
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from usl.WinSource.RegistView import *


class MyRegistWindow(QMainWindow,Ui_MainWindow,QMessageBox):
    def __init__(self,parent=None):
        super(MyRegistWindow, self).__init__(parent)
        self.setupUi(self)

        # self.protocol_View = ProtocolViewLogic.MyProtocolWindow()
        # self.qrButton.clicked.connect(self.print_hello)
        # self.pushButton.clicked.connect(self.show_protocol)

        self.pwd_Text.editingFinished.connect(self.wrong_pwd)
        self.phone_Text.editingFinished.connect(self.wrong_telenum)
        self.nc_Text.editingFinished.connect(self.wrong_nickname)


    def show_protocol(self):
        self.protocol_View.show()

    def print_hello(self):
        print("hello world")

    def name_repeat(self):
        QMessageBox.warning(self, 'Warning', '用户名重复')

    def register_error(self):
        QMessageBox.warning(self, 'Warning', '注册失败')

    # def judge_sex(self):
    #     """
    #     判断性别 男 返回 1
    #             女 返回 0
    #     :return:
    #     """
    #     if self.man_btn.isChecked():
    #         return 1
    #     elif self.woman_btn.isChecked():
    #         return 0

    # def msg(self):
    #     """
    #     选择头像文件位置
    #     :return:
    #     """
    #     # self.directory = QFileDialog.getExistingDirectory(self,
    #     #                                               "选取文件夹",
    #     #                                               "./")  # 起始路径
    #     self.fileName, self.filetype = QFileDialog.getOpenFileName(self,
    #                                                       "选取文件",
    #                                                       "./",
    #                                                       "Picture Files (*.jpg)")  # 设置文件扩展名过滤,注意用双分号间隔
    #     # print(self.fileName, self.filetype)
    #
    #     self.symbol_dir.setText(self.fileName)

    # def create_confirmnum(self):
    #     """
    #     产生验证码
    #     :return:
    #     """
    #     str01 = string.digits+string.ascii_letters
    #     confirmnum = ''
    #     for i in range(0,4):
    #         confirmnum += random.choices(str01)[0]
    #     self.confirm_number02.setText(confirmnum)


    # def lack_info(self):
    #     """
    #     缺少信息，注册信息不完整
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，请讲注册信息补充完整！")

    # def wrong_telenum(self):
    #     """
    #     手机号码错误
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，手机号码错误！")
    #
    # def wrong_nickname(self):
    #     """
    #     昵称须以字母开头
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，昵称须以字母开头！")
    #
    # def wrong_pwd(self):
    #     """
    #     密码须以字母开头
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，密码须以字母开头！")
    #
    # def diff_pwd(self):
    #     """
    #     两次密码不同
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，两次密码不同！")
    #
    # def diff_confirmnum(self):
    #     """
    #     验证码不对
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，验证码错误！")
    #
    # def info_deficiency(self):
    #     """
    #     信息不全 报警
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，请将信息填写完整！")
    #
    # def telenumber_exist(self):
    #     """
    #     手机号被注册则报警
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!',"该手机号已被注册，请更换手机号重新注册！")
    #
    # def nickname_exist(self):
    #     """
    #     昵称被使用则报警
    #     :return:
    #     """
    #     QMessageBox.warning(self, 'Waring!', "对不起，该用户名已存在！")
    #
    # def fail_register(self):
    #     QMessageBox.warning(self, 'Waring!', "对不起，注册失败，请重试！")
    #
    # def success_register(self):
    #     QMessageBox.warning(self, 'Waring!', "恭喜您，注册成功！")
    #




# ------------------------------------------------

    def wrong_telenum(self):
        if not re.findall('^1[0-9]{10}$',self.phone_Text.text()):
            QMessageBox.warning(self, 'Warning', '电话号码错误')

    def wrong_nickname(self):
        if not re.findall(r'^([a-z]|[A-Z])(\w*)$',self.nc_Text.text()):
            QMessageBox.warning(self, 'Warning', '昵称错误')

    def wrong_pwd(self):
        if not re.findall(r'^([a-z]|[A-Z])(\w{5})(\w*)$',self.pwd_Text.text()):
            QMessageBox.warning(self, 'Warning', '密码格式错误')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    myWin=MyRegistWindow()
    myWin.show()
    # myWin.name_repeat()
    sys.exit(app.exec_())
