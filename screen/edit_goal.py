# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/edit_goal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewGoalWindow(object):
    def setupUi(self, NewGoalWindow):
        NewGoalWindow.setObjectName("NewGoalWindow")
        NewGoalWindow.resize(1000, 708)
        NewGoalWindow.setStyleSheet("background-color: #F6F5F9;")
        self.centralwidget = QtWidgets.QWidget(NewGoalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(300, 70, 401, 31))
        self.titleEdit.setStyleSheet("border: none; background-color: white; border-bottom: 1px solid #C9C9C9;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.titleEdit.setText("")
        self.titleEdit.setObjectName("titleEdit")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(300, 30, 91, 16))
        self.titleLabel.setStyleSheet("font-size: 20px;")
        self.titleLabel.setObjectName("titleLabel")
        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setGeometry(QtCore.QRect(300, 140, 101, 31))
        self.descriptionLabel.setStyleSheet("font-size: 20px;")
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(40, 610, 131, 41))
        self.cancelButton.setStyleSheet("background-color: #B23535;\n"
"color: white;\n"
"border-radius: 5px; font-size: 15px;")
        self.cancelButton.setObjectName("cancelButton")
        self.modifyGoalButton = QtWidgets.QPushButton(self.centralwidget)
        self.modifyGoalButton.setGeometry(QtCore.QRect(830, 610, 131, 41))
        self.modifyGoalButton.setStyleSheet("background-color: #35B29D;\n"
"color: white;\n"
"border-radius: 5px; font-size: 15px;")
        self.modifyGoalButton.setObjectName("modifyGoalButton")
        self.descriptionEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.descriptionEdit.setGeometry(QtCore.QRect(300, 190, 401, 121))
        self.descriptionEdit.setStyleSheet("border: none; background-color: white; border-bottom: 1px solid #C9C9C9; border-radius: 5px; padding: 10px;")
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(280, 340, 451, 311))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        NewGoalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewGoalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        NewGoalWindow.setMenuBar(self.menubar)

        self.retranslateUi(NewGoalWindow)
        QtCore.QMetaObject.connectSlotsByName(NewGoalWindow)

    def retranslateUi(self, NewGoalWindow):
        _translate = QtCore.QCoreApplication.translate
        NewGoalWindow.setWindowTitle(_translate("NewGoalWindow", "Edit Goal"))
        self.titleEdit.setPlaceholderText(_translate("NewGoalWindow", "Enter a goal title..."))
        self.titleLabel.setText(_translate("NewGoalWindow", "Goal Title"))
        self.descriptionLabel.setText(_translate("NewGoalWindow", "Description"))
        self.cancelButton.setText(_translate("NewGoalWindow", "Cancel"))
        self.modifyGoalButton.setText(_translate("NewGoalWindow", "Modify Goal"))
        self.descriptionEdit.setPlaceholderText(_translate("NewGoalWindow", "Enter a description for your new goal..."))
