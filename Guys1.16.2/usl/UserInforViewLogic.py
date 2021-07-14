# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/1 20:33
# write_by:QiFuMin
# script_name:RegistViewLogin.py
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow, QMessageBox
from usl.WinSource.UserInforView import *


class MyUserInforWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyUserInforWindow, self).__init__(parent)
        self.setupUi(self)

    def change_name_repeat(self):
        QMessageBox.warning(self, 'Warning', '用户名重复,修改失败')

    def change_success(self):
        QMessageBox.warning(self, '提示', '修改成功')


if __name__ == '__main__':
    app=QApplication(sys.argv)
    myWin=MyUserInforWindow()
    myWin.show()
    sys.exit(app.exec_())
