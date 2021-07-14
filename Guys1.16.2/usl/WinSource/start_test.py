# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/1 20:33
# write_by:QiFuMin
# script_name:RegistViewLogin.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from usl.WinSource.untitled02 import *
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QVBoxLayout,
                            QHBoxLayout, QListWidget, QListWidgetItem,QMenu,QAction)

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont


class MyLable(QWidget):
    def __init__(self, idnumber, title, subtitle, icon_path):
        super(MyLable, self).__init__()
        self.lb_idnumber = idnumber
        self.lb_title = QLabel(title)
        self.lb_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lb_subtitle = QLabel(subtitle)
        self.lb_subtitle.setFont(QFont("Arial", 8, QFont.StyleItalic))
        self.lb_icon = QLabel()
        self.lb_icon.setFixedSize(40, 40)
        pixMap = QPixmap(icon_path).scaled(self.lb_icon.width(), self.lb_icon.height())
        self.lb_icon.setPixmap(pixMap)
        self.double_click_fun = None
        self.init_ui()


    def init_ui(self):
        """handle layout"""
        ly_main = QHBoxLayout()
        ly_right = QVBoxLayout()
        ly_right.addWidget(self.lb_title)
        ly_right.addWidget(self.lb_subtitle)
        ly_right.setAlignment(Qt.AlignVCenter)
        ly_main.addWidget(self.lb_icon)
        ly_main.addLayout(ly_right)
        self.setLayout(ly_main)
        self.resize(90, 60)

    def get_lb_title(self):
        return self.lb_title.text()

    def get_lb_idnumber(self):
        return self.lb_idnumber

    def get_lb_subtitle(self):
        return self.lb_subtitle.text()


class MyChatWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyChatWindow, self).__init__(parent)
        self.setupUi(self)
        self.listWidget.doubleClicked.connect(self.get_item_infor)


    def create_item_widget(self):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(90, 60))
        return item_widget

    def create_label_widget(self,idnumber,nickname,signature,icon):
        label = MyLable(idnumber, nickname, signature, icon)
        return label

    def add_to_list(self,item,label):
        self.listWidget.addItem(item)

        self.listWidget.setItemWidget(item, label)

    def create_frient_list(self,idnumber,nickname,signature,icon):
        my_item = self.create_item_widget()
        my_label = self.create_label_widget(idnumber,nickname,signature,icon)
        self.add_to_list(my_item,my_label)

    def get_item_infor(self):
        widget = self.listWidget.itemWidget(self.listWidget.currentItem())  # get MyLabel widget
        # self.doubleclick_fun(widget.get_lb_title(), widget.get_lb_subtitle())

        print(widget.get_lb_idnumber())



    def print_hello(self):
        print('hello')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyChatWindow()
    for i in range(3):
        myWin.create_frient_list('2345','qifumin','go on',
                                 '/home/tarena/qifumin/code/mid_project1/mid_project/Guys/static/bg.jpg')




    # my_item = QListWidgetItem()
    # myWin.listWidget.setItemWidget(my_item,myWin.my_widget)
    myWin.show()
    sys.exit(app.exec_())
