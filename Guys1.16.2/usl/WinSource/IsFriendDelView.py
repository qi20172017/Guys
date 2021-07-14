# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IsFriendDelView.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(309, 189)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 40, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancle_btn = QtWidgets.QPushButton(Dialog)
        self.cancle_btn.setGeometry(QtCore.QRect(70, 130, 80, 26))
        self.cancle_btn.setObjectName("cancle_btn")
        self.yes_btn = QtWidgets.QPushButton(Dialog)
        self.yes_btn.setGeometry(QtCore.QRect(160, 130, 80, 26))
        self.yes_btn.setObjectName("yes_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "确认删除此好友？"))
        self.cancle_btn.setText(_translate("Dialog", "Cancle"))
        self.yes_btn.setText(_translate("Dialog", "Yes"))
