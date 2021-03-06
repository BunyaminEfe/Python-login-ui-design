# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(694, 567)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        Login.setWindowOpacity(1.0)
        Login.setLayoutDirection(QtCore.Qt.LeftToRight)
        Login.setAutoFillBackground(False)
        Login.setStyleSheet("*{\n"
"\n"
"font-family: century gothik;\n"
"font-size: 24px;\n"
"}\n"
"\n"
"QFrame{\n"
"background: #333;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"#Login{\n"
"border-image: url(:/fotos/wp1968953.jpg);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(34, 255, 0);\n"
"border-radius: 60px;\n"
"}\n"
"\n"
"QToolButton{\n"
"    background-color: rgb(34, 255, 0);\n"
"border-radius: 45px;\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton{\n"
"    background-color: rgb(34, 255, 0);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(34, 255, 0);\n"
"    border-radius: 15px;\n"
"    background: rgb(110, 179, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    background: transparent;\n"
"    border: none;\n"
"    color: #717072;\n"
"    border-bottom: 1px sold #717072;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(124, 104, 431, 341))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 30, 161, 51))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 391, 41))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 371, 31))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setPlaceholderText("Kullanıcı Adı")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 180, 371, 31))
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(290, 40, 101, 101))
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setAutoFillBackground(False)
        self.toolButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/fotos/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName("toolButton")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login Bejo"))
        self.label.setText(_translate("Login", "GİRİŞ EKRANI"))
        self.pushButton.setText(_translate("Login", "GİRİŞ YAP"))
        self.lineEdit_2.setPlaceholderText(_translate("Login", "Şifre"))
import iconfoto


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
