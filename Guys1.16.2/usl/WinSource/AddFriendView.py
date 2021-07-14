# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddFriendView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 292)
        self.user_id = QtWidgets.QLabel(Form)
        self.user_id.setGeometry(QtCore.QRect(40, 60, 55, 18))
        self.user_id.setObjectName("user_id")
        self.id_edit = QtWidgets.QLineEdit(Form)
        self.id_edit.setGeometry(QtCore.QRect(110, 50, 113, 26))
        self.id_edit.setObjectName("id_edit")
        self.add_btn = QtWidgets.QPushButton(Form)
        self.add_btn.setGeometry(QtCore.QRect(240, 50, 80, 26))
        self.add_btn.setObjectName("add_btn")
        self.back_message = QtWidgets.QLabel(Form)
        self.back_message.setGeometry(QtCore.QRect(150, 120, 91, 51))
        self.back_message.setObjectName("back_message")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.user_id.setText(_translate("Form", "账号"))
        self.add_btn.setText(_translate("Form", "添加"))
        self.back_message.setText(_translate("Form", "成功与否"))
