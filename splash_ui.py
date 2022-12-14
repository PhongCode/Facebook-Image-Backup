# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class SplashClass(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/static/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget#Form {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:0.00568182 rgba(170, 85, 127, 255), stop:0.988636 rgba(109, 25, 27, 255), stop:1 rgba(66, 164, 255, 255));\n"
"    border-color: #fff;\n"
"}\n"
"  \n"
"")
        self.Icon = QtWidgets.QLabel(Form)
        self.Icon.setGeometry(QtCore.QRect(10, 205, 51, 51))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("static/logo.png"))
        self.Icon.setScaledContents(True)
        self.Icon.setObjectName("Icon")
        self.Title = QtWidgets.QLabel(Form)
        self.Title.setGeometry(QtCore.QRect(60, 210, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.Title.setFont(font)
        self.Title.setStyleSheet("QLabel#Title {\n"
"    color: #fff;\n"
"}")
        self.Title.setScaledContents(True)
        self.Title.setWordWrap(False)
        self.Title.setIndent(0)
        self.Title.setObjectName("Title")
        self.Description = QtWidgets.QLabel(Form)
        self.Description.setGeometry(QtCore.QRect(61, 240, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        self.Description.setFont(font)
        self.Description.setStyleSheet("QLabel#Description {\n"
"    color: #fff;\n"
"}")
        self.Description.setObjectName("Description")
        self.Progress = QtWidgets.QProgressBar(Form)
        self.Progress.setGeometry(QtCore.QRect(0, 268, 500, 6))
        self.Progress.setStyleSheet("QProgressBar {\n"
"     background-color: #FFF;\n"
"     color: #005068;\n"
"     border-style: none;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"     border: none;\n"
"     background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #1C3334, stop:1 #376E6F);\n"
"            }")
        self.Progress.setProperty("value", 10)
        self.Progress.setFormat("")
        self.Progress.setObjectName("Progress")
        self.Author = QtWidgets.QLabel(Form)
        self.Author.setGeometry(QtCore.QRect(320, 250, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(6)
        font.setBold(False)
        font.setWeight(50)
        self.Author.setFont(font)
        self.Author.setAcceptDrops(False)
        self.Author.setStyleSheet("QLabel#Author {\n"
"    color: #fff;\n"
"}")
        self.Author.setScaledContents(False)
        self.Author.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Author.setObjectName("Author")
        self.Image_0 = QtWidgets.QLabel(Form)
        self.Image_0.setGeometry(QtCore.QRect(50, 30, 391, 141))
        self.Image_0.setText("")
        self.Image_0.setPixmap(QtGui.QPixmap("static/splash01.png"))
        self.Image_0.setScaledContents(True)
        self.Image_0.setObjectName("Image_0")
        self.Image_1 = QtWidgets.QLabel(Form)
        self.Image_1.setGeometry(QtCore.QRect(50, 30, 391, 141))
        self.Image_1.setText("")
        self.Image_1.setPixmap(QtGui.QPixmap("static/splash02.png"))
        self.Image_1.setScaledContents(True)
        self.Image_1.setObjectName("Image_1")
        self.Image_2 = QtWidgets.QLabel(Form)
        self.Image_2.setGeometry(QtCore.QRect(50, 30, 391, 141))
        self.Image_2.setText("")
        self.Image_2.setPixmap(QtGui.QPixmap("static/splash03.png"))
        self.Image_2.setScaledContents(True)
        self.Image_2.setObjectName("Image_2")
        self.Image_3 = QtWidgets.QLabel(Form)
        self.Image_3.setGeometry(QtCore.QRect(50, 30, 391, 141))
        self.Image_3.setText("")
        self.Image_3.setPixmap(QtGui.QPixmap("static/splash04.png"))
        self.Image_3.setScaledContents(True)
        self.Image_3.setObjectName("Image_3")
        self.Image_4 = QtWidgets.QLabel(Form)
        self.Image_4.setGeometry(QtCore.QRect(50, 30, 391, 141))
        self.Image_4.setText("")
        self.Image_4.setPixmap(QtGui.QPixmap("static/splash05.png"))
        self.Image_4.setScaledContents(True)
        self.Image_4.setObjectName("Image_4")
        self.Image_5 = QtWidgets.QLabel(Form)
        self.Image_5.setGeometry(QtCore.QRect(50, 30, 391, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Image_5.sizePolicy().hasHeightForWidth())
        self.Image_5.setSizePolicy(sizePolicy)
        self.Image_5.setText("")
        self.Image_5.setPixmap(QtGui.QPixmap("static/splash06.png"))
        self.Image_5.setScaledContents(True)
        self.Image_5.setObjectName("Image_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Facekup - Download everything"))
        self.Title.setText(_translate("Form", "Facekup"))
        self.Description.setText(_translate("Form", "Facebook image backup version 1.0.19"))
        self.Author.setText(_translate("Form", "www.nguyentrieuphong.com "))
