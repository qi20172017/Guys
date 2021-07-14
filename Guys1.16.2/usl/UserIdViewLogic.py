# encoding: utf-8
# author: QiFuMin
# contact: 1248227761@qq.com
# site: https://www.jianshu.com/u/eaaae8e04a35
# software: PyCharm
# file: ProtocolViewLogin.py

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from usl.WinSource.UserIdView import *


class MyUserIdWindow(QMainWindow,Ui_Dialog):
    def __init__(self,parent=None):
        super(MyUserIdWindow, self).__init__(parent)
        self.setupUi(self)

        # self.qrButton.clicked.connect(self.print_hello)

    def print_hello(self):
        print("hello world")

    def add_val(self,data):
        self.userid_text.append(data)


if __name__ == '__main__':
    app=QApplication(sys.argv)
    myWin=MyUserIdWindow()
    myWin.show()
    sys.exit(app.exec_())
