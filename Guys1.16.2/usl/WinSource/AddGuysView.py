# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_guys.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 587)
        self.friend_list = QtWidgets.QListWidget(Form)
        self.friend_list.setGeometry(QtCore.QRect(70, 30, 256, 481))
        self.friend_list.setObjectName("friend_list")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
