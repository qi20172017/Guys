# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatLoginWindow(object):
    def setupUi(self, ChatLoginWindow):
        ChatLoginWindow.setObjectName("ChatLoginWindow")
        ChatLoginWindow.resize(483, 670)
        # ChatLoginWindow.setStyleSheet("background-image:url(\"../images/bg.jpg\")")
        self.centralwidget = QtWidgets.QWidget(ChatLoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_user = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_user.setGeometry(QtCore.QRect(120, 300, 261, 51))
        self.txt_user.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txt_user.setObjectName("txt_user")
        self.txt_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_pwd.setGeometry(QtCore.QRect(120, 390, 261, 51))
        self.txt_pwd.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.txt_pwd.setObjectName("txt_pwd")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(100, 490, 301, 41))
        self.btn_login.setObjectName("btn_login")
        self.btn_regist = QtWidgets.QPushButton(self.centralwidget)
        self.btn_regist.setGeometry(QtCore.QRect(100, 550, 301, 41))
        self.btn_regist.setObjectName("btn_regist")
        self.chk_remenber_pwd = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_remenber_pwd.setGeometry(QtCore.QRect(140, 460, 91, 16))
        self.chk_remenber_pwd.setObjectName("chk_remenber_pwd")
        self.chk_auto_login = QtWidgets.QCheckBox(self.centralwidget)
        self.chk_auto_login.setGeometry(QtCore.QRect(290, 460, 91, 16))
        self.chk_auto_login.setObjectName("chk_auto_login")
        ChatLoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChatLoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 483, 23))
        self.menubar.setObjectName("menubar")
        ChatLoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChatLoginWindow)
        self.statusbar.setObjectName("statusbar")
        ChatLoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChatLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(ChatLoginWindow)

    def retranslateUi(self, ChatLoginWindow):
        _translate = QtCore.QCoreApplication.translate
        ChatLoginWindow.setWindowTitle(_translate("ChatLoginWindow", "MainWindow"))
        self.btn_login.setText(_translate("ChatLoginWindow", "登录"))
        self.btn_regist.setText(_translate("ChatLoginWindow", "注册"))
        self.chk_remenber_pwd.setText(_translate("ChatLoginWindow", "记住密码"))
        self.chk_auto_login.setText(_translate("ChatLoginWindow", "自动登录"))
