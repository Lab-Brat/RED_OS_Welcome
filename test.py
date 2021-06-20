# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(826, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(320, 0, 1021, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")

        self.redos_icon = QtWidgets.QLabel(self.centralwidget)
        self.redos_icon.setGeometry(QtCore.QRect(10, 10, 151, 71))
        self.redos_icon.setText("")
        self.redos_icon.setPixmap(QtGui.QPixmap("logo.png"))
        self.redos_icon.setScaledContents(True)
        self.redos_icon.setObjectName("redos_icon")

        self.click1 = QtWidgets.QPushButton(self.centralwidget)
        self.click1.setGeometry(QtCore.QRect(30, 110, 171, 41))
        self.click1.setObjectName("click1")
        self.click2 = QtWidgets.QPushButton(self.centralwidget)
        self.click2.setGeometry(QtCore.QRect(30, 160, 171, 41))
        self.click2.setObjectName("click2")
        self.click3 = QtWidgets.QPushButton(self.centralwidget)
        self.click3.setGeometry(QtCore.QRect(30, 210, 171, 41))
        self.click3.setObjectName("click3")
        self.click4 = QtWidgets.QPushButton(self.centralwidget)
        self.click4.setGeometry(QtCore.QRect(30, 260, 171, 41))
        self.click4.setObjectName("click4")
        self.click5 = QtWidgets.QPushButton(self.centralwidget)
        self.click5.setGeometry(QtCore.QRect(30, 310, 171, 41))
        self.click5.setObjectName("click5")
        self.click6 = QtWidgets.QPushButton(self.centralwidget)
        self.click6.setGeometry(QtCore.QRect(30, 360, 171, 41))
        self.click6.setObjectName("click6")
        self.click7 = QtWidgets.QPushButton(self.centralwidget)
        self.click7.setGeometry(QtCore.QRect(30, 410, 171, 41))
        self.click7.setObjectName("click7")

        self.autostart = QtWidgets.QRadioButton(self.centralwidget)
        self.autostart.setGeometry(QtCore.QRect(30, 490, 112, 23))
        self.autostart.setObjectName("autostart")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(250, 110, 541, 331))
        self.stackedWidget.setObjectName("stackedWidget")


        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page")
        self.stackedWidget.addWidget(self.page1)

        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page2)

        self.page1UI()
        self.page2UI()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "Добро пожаловать в РЕД_ОС"))

        self.autostart.setText(_translate("MainWindow", "autostart"))
        self.autostart.toggled.connect(self.click_auto)

        self.click1.setText(_translate("MainWindow", "Click Me!"))
        self.click2.setText(_translate("MainWindow", "Click Me!"))
        self.click2.clicked.connect(self.click_2)
        self.click3.setText(_translate("MainWindow", "Click Me!"))
        self.click4.setText(_translate("MainWindow", "Click Me!"))
        self.click5.setText(_translate("MainWindow", "Click Me!"))
        self.click6.setText(_translate("MainWindow", "Click Me!"))
        self.click7.setText(_translate("MainWindow", "Click Me!"))



    def page1UI(self):
        layout = QtWidgets.QFormLayout()
        sex = QtWidgets.QHBoxLayout()
        sex.addWidget(QtWidgets.QRadioButton("Male"))
        sex.addWidget(QtWidgets.QRadioButton("Female"))
        layout.addRow(QtWidgets.QLabel("Sex"),sex)
        layout.addRow("Date of Birth",QtWidgets.QLineEdit())

        self.page1.setLayout(layout)

    def page2UI(self):
        layout = QtWidgets.QFormLayout()
        sex = QtWidgets.QHBoxLayout()
        sex.addWidget(QtWidgets.QRadioButton("Page2"))
        sex.addWidget(QtWidgets.QRadioButton("Female"))
        layout.addRow(QtWidgets.QLabel("Sex"),sex)
        layout.addRow("Date of Birth",QtWidgets.QLineEdit())

        self.page2.setLayout(layout)

    # def button_clicked1(self):
    #     print("it works!")

    def click_2(self):
        i = 2
        self.stackedWidget.setCurrentIndex(i)



    def click_auto(self, selected):
        if selected:
            param = 1
            out = lambda: os.system('./Off.sh {0}'.format(param))
            out()
            #print('./Off.sh {0}'.format(param))
        else:
            param = 0
            out = lambda: os.system('./Off.sh {0}'.format(param))
            out()
            #print('./Off.sh {0}'.format(param))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
