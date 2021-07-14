# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChatView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1059, 792)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.massage_btn = QtWidgets.QPushButton(self.centralwidget)
        self.massage_btn.setGeometry(QtCore.QRect(10, 90, 80, 71))
        self.massage_btn.setObjectName("massage_btn")
        self.add_friend_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_friend_btn.setGeometry(QtCore.QRect(10, 170, 80, 71))
        self.add_friend_btn.setObjectName("add_friend_btn")
        self.friend_list = QtWidgets.QListWidget(self.centralwidget)
        self.friend_list.setGeometry(QtCore.QRect(110, 80, 256, 621))
        self.friend_list.setObjectName("friend_list")
        self.message_history = QtWidgets.QTextBrowser(self.centralwidget)
        self.message_history.setGeometry(QtCore.QRect(450, 80, 571, 431))
        self.message_history.setObjectName("message_history")
        self.message_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.message_edit.setGeometry(QtCore.QRect(450, 560, 571, 91))
        self.message_edit.setObjectName("message_edit")
        self.send_massage_btn = QtWidgets.QPushButton(self.centralwidget)
        self.send_massage_btn.setGeometry(QtCore.QRect(910, 660, 80, 71))
        self.send_massage_btn.setObjectName("send_massage_btn")
        self.select_file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.select_file_btn.setGeometry(QtCore.QRect(770, 660, 80, 71))
        self.select_file_btn.setObjectName("select_file_btn")
        self.friend_infor_btn = QtWidgets.QPushButton(self.centralwidget)
        self.friend_infor_btn.setGeometry(QtCore.QRect(410, 20, 61, 51))
        self.friend_infor_btn.setObjectName("friend_infor_btn")
        self.add_guys_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_guys_btn.setGeometry(QtCore.QRect(500, 20, 61, 51))
        self.add_guys_btn.setObjectName("add_guys_btn")
        self.quit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quit_btn.setGeometry(QtCore.QRect(10, 670, 80, 71))
        self.quit_btn.setObjectName("quit_btn")
        self.user_infor_btn = QtWidgets.QPushButton(self.centralwidget)
        self.user_infor_btn.setGeometry(QtCore.QRect(10, 10, 80, 71))
        self.user_infor_btn.setObjectName("user_infor_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1059, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.massage_btn.setText(_translate("MainWindow", "消息"))
        self.add_friend_btn.setText(_translate("MainWindow", "添加好友"))
        self.send_massage_btn.setText(_translate("MainWindow", "发送"))
        self.select_file_btn.setText(_translate("MainWindow", "选择文件"))
        self.friend_infor_btn.setText(_translate("MainWindow", "好友信息"))
        self.add_guys_btn.setText(_translate("MainWindow", "三五成群"))
        self.quit_btn.setText(_translate("MainWindow", "退出"))
        self.user_infor_btn.setText(_translate("MainWindow", "touxiang"))
