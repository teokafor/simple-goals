# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/new_goal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewGoalWindow(object):
    def setupUi(self, NewGoalWindow):
        NewGoalWindow.setObjectName("NewGoalWindow")
        NewGoalWindow.resize(800, 550)
        NewGoalWindow.setStyleSheet("background-color: #F6F5F9;")
        self.centralwidget = QtWidgets.QWidget(NewGoalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(190, 100, 401, 31))
        self.titleEdit.setStyleSheet("border: none; background-color: white; border-bottom: 1px solid #C9C9C9;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.titleEdit.setText("")
        self.titleEdit.setObjectName("titleEdit")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(190, 60, 91, 16))
        self.titleLabel.setStyleSheet("font-size: 20px;")
        self.titleLabel.setObjectName("titleLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(190, 170, 101, 31))
        self.descriptionLabel.setStyleSheet("font-size: 20px;")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(30, 460, 131, 41))
        self.cancelButton.setStyleSheet("background-color: #B23535;\n"
"color: white;\n"
"border-radius: 5px; font-size: 15px;")
        self.cancelButton.setObjectName("cancelButton")
        self.createGoalButton = QtWidgets.QPushButton(self.centralwidget)
        self.createGoalButton.setGeometry(QtCore.QRect(640, 460, 131, 41))
        self.createGoalButton.setStyleSheet("background-color: #35B29D;\n"
"color: white;\n"
"border-radius: 5px; font-size: 15px;")
        self.createGoalButton.setObjectName("createGoalButton")
        self.descriptionEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.descriptionEdit.setGeometry(QtCore.QRect(190, 220, 401, 41))
        self.descriptionEdit.setStyleSheet("border: none; background-color: white; border-bottom: 1px solid #C9C9C9; border-radius: 5px; padding: 10px;")
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(240, 290, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        NewGoalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewGoalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        NewGoalWindow.setMenuBar(self.menubar)

        self.retranslateUi(NewGoalWindow)
        QtCore.QMetaObject.connectSlotsByName(NewGoalWindow)

    def retranslateUi(self, NewGoalWindow):
        _translate = QtCore.QCoreApplication.translate
        NewGoalWindow.setWindowTitle(_translate("NewGoalWindow", "MainWindow"))
        self.titleEdit.setPlaceholderText(_translate("NewGoalWindow", "Enter a goal title..."))
        self.titleLabel.setText(_translate("NewGoalWindow", "Goal Title"))
        self.descriptionLabel.setText(_translate("NewGoalWindow", "Description"))
        self.cancelButton.setText(_translate("NewGoalWindow", "Cancel"))
        self.createGoalButton.setText(_translate("NewGoalWindow", "Create Goal"))
        self.descriptionEdit.setPlaceholderText(_translate("NewGoalWindow", "Enter a description for your new goal..."))