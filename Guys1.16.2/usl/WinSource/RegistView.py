# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(467, 597)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.affirm_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.affirm_Text.setGeometry(QtCore.QRect(190, 430, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.affirm_Text.setFont(font)
        self.affirm_Text.setObjectName("affirm_Text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 430, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verify_btn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.verify_btn.setGeometry(QtCore.QRect(200, 470, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.verify_btn.setFont(font)
        self.verify_btn.setObjectName("verify_btn")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 100, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 197, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 157, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nc_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.nc_Text.setGeometry(QtCore.QRect(190, 157, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.nc_Text.setFont(font)
        self.nc_Text.setObjectName("nc_Text")
        self.gx_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.gx_Text.setGeometry(QtCore.QRect(190, 197, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.gx_Text.setFont(font)
        self.gx_Text.setObjectName("gx_Text")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 230, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 390, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 350, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gender_w_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.gender_w_btn.setGeometry(QtCore.QRect(310, 230, 89, 16))
        self.gender_w_btn.setStyleSheet("name=\"sex\";")
        self.gender_w_btn.setObjectName("gender_w_btn")
        self.email_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.email_Text.setGeometry(QtCore.QRect(190, 390, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.email_Text.setFont(font)
        self.email_Text.setObjectName("email_Text")
        self.phone_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_Text.setGeometry(QtCore.QRect(190, 350, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.phone_Text.setFont(font)
        self.phone_Text.setObjectName("phone_Text")
        self.gender_m_btn = QtWidgets.QRadioButton(self.centralwidget)
        self.gender_m_btn.setGeometry(QtCore.QRect(200, 230, 89, 16))
        self.gender_m_btn.setStyleSheet("name=\"sex\" checked;")
        self.gender_m_btn.setObjectName("gender_m_btn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 310, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pwd_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_Text.setGeometry(QtCore.QRect(190, 310, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pwd_Text.setFont(font)
        self.pwd_Text.setObjectName("pwd_Text")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 270, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.birthday_Text = QtWidgets.QLineEdit(self.centralwidget)
        self.birthday_Text.setGeometry(QtCore.QRect(190, 270, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.birthday_Text.setFont(font)
        self.birthday_Text.setObjectName("birthday_Text")
        self.heads_btn = QtWidgets.QPushButton(self.centralwidget)
        self.heads_btn.setGeometry(QtCore.QRect(190, 70, 81, 71))
        self.heads_btn.setText("")
        self.heads_btn.setObjectName("heads_btn")
        self.affirm_btn = QtWidgets.QPushButton(self.centralwidget)
        self.affirm_btn.setGeometry(QtCore.QRect(300, 420, 75, 41))
        self.affirm_btn.setText("")
        self.affirm_btn.setObjectName("affirm_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 467, 22))
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
        self.label_2.setText(_translate("MainWindow", "输入验证码："))
        self.verify_btn.setText(_translate("MainWindow", "确认"))
        self.label_7.setText(_translate("MainWindow", "上传头像："))
        self.label_4.setText(_translate("MainWindow", "个性签名："))
        self.label_3.setText(_translate("MainWindow", "昵称："))
        self.label_6.setText(_translate("MainWindow", "选择性别："))
        self.label_5.setText(_translate("MainWindow", "输入邮箱号码："))
        self.label.setText(_translate("MainWindow", "输入手机号码："))
        self.gender_w_btn.setText(_translate("MainWindow", "女"))
        self.gender_m_btn.setText(_translate("MainWindow", "男"))
        self.label_8.setText(_translate("MainWindow", "设置密码："))
        self.label_9.setText(_translate("MainWindow", "出生日期："))
