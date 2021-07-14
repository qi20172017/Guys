# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserIdView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 223)
        font = QtGui.QFont()
        font.setPointSize(36)
        Dialog.setFont(font)
        self.userid_text = QtWidgets.QTextBrowser(Dialog)
        self.userid_text.setGeometry(QtCore.QRect(50, 70, 301, 71))
        self.userid_text.setObjectName("userid_text")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.to_login_btn = QtWidgets.QPushButton(Dialog)
        self.to_login_btn.setGeometry(QtCore.QRect(140, 160, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.to_login_btn.setFont(font)
        self.to_login_btn.setObjectName("to_login_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "您的账号为："))
        self.to_login_btn.setText(_translate("Dialog", "登录"))
