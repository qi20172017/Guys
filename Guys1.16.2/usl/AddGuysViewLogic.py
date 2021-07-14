# !/usr/bin/env python
# coding:utf-8
# Time:2020/1/1 20:33
# write_by:QiFuMin
# script_name:RegistViewLogin.py
from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout,
                            QHBoxLayout, QListWidgetItem)

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QFont
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from usl.WinSource.AddGuysView import *



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


class MyAddGuysWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyAddGuysWindow, self).__init__(parent)
        self.setupUi(self)
        # self.friend_list.doubleClicked.connect(self.get_item_id)

    def create_item_widget(self):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(90, 60))
        return item_widget

    def create_label_widget(self, idnumber, nickname, signature, icon):
        label = MyLable(idnumber, nickname, signature, icon)
        return label

    def add_to_list(self, user_info):
        my_item = self.create_item_widget()
        my_label = self.create_label_widget(user_info[0], user_info[1], user_info[2], user_info[3])
        self.friend_list.addItem(my_item)
        self.friend_list.setItemWidget(my_item, my_label)

    def create_frient_list(self, user_list):
        """
        循环调用添加函数
        """
        for user in user_list:
            self.add_to_list(user)

    def get_item_id(self):
        widget = self.friend_list.itemWidget(self.friend_list.currentItem())  # get MyLabel widget
        return widget.get_lb_idnumber()
        # print(widget.get_lb_idnumber())

    def get_item_row(self):
        return self.friend_list.row(self.friend_list.currentItem())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyAddGuysWindow()
    user_list = [['10000', 'aaa', 'foofdjls', '/home/tarena/qifumin/code/mid_project1/mid_project/Guys/static/bg.jpg'],
                 ['10001', 'bbb', 'fdsfdsf',
                  '/home/tarena/qifumin/code/mid_project1/mid_project/Guys/static/image_3.jpg'],
                 ['10002', 'ccc', 'oui97yh',
                  '/home/tarena/qifumin/code/mid_project1/mid_project/Guys/static/tupian01.jpg']
                 ]

    myWin.create_frient_list(user_list)
    myWin.show()
    # myWin.friend_list.doubleClicked.connect()
    sys.exit(app.exec_())
