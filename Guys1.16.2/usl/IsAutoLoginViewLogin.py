# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/1 20:33
# write_by:QiFuMin
# script_name:RegistViewLogin.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from usl.WinSource.IsAutoLoginView import *


class MyIsAutoLoginWindow(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super(MyIsAutoLoginWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyIsAutoLoginWindow()
    myWin.show()
    sys.exit(app.exec_())
