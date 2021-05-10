# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/new_subgoal.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewGoalWindow(object):
    def __init__(self, NewGoalWindow):
        NewGoalWindow.setObjectName("NewGoalWindow")
        NewGoalWindow.resize(1000, 708)
        NewGoalWindow.setStyleSheet("background-color: #F6F5F9;")
        self.centralwidget = QtWidgets.QWidget(NewGoalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.titleEdit.setGeometry(QtCore.QRect(300, 320, 401, 41))
        self.titleEdit.setStyleSheet("border: none; background-color: white; border-bottom: 1px solid #C9C9C9;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.titleEdit.setText("")
        self.titleEdit.setObjectName("titleEdit")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(300, 280, 141, 31))
        self.titleLabel.setStyleSheet("font-size: 20px;")
        self.titleLabel.setObjectName("titleLabel")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(40, 610, 131, 41))
        self.cancelButton.setStyleSheet("background-color: #B23535;\n"
"color: white;\n"
"border-radius: 5px; font-size: 15px;")
        self.cancelButton.setObjectName("cancelButton")
        self.createSubgoalButton = QtWidgets.QPushButton(self.centralwidget)
        self.createSubgoalButton.setGeometry(QtCore.QRect(830, 610, 131, 41))
        self.createSubgoalButton.setStyleSheet("background-color: #35B29D;\n"
"color: white;\n"
"border-radius: 5px; font-size: 15px;")
        self.createSubgoalButton.setObjectName("createSubgoalButton")
        NewGoalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewGoalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        NewGoalWindow.setMenuBar(self.menubar)

        self.retranslateUi(NewGoalWindow)
        QtCore.QMetaObject.connectSlotsByName(NewGoalWindow)

    def retranslateUi(self, NewGoalWindow):
        _translate = QtCore.QCoreApplication.translate
        NewGoalWindow.setWindowTitle(_translate("NewGoalWindow", "New Subgoal"))
        self.titleEdit.setPlaceholderText(_translate("NewGoalWindow", "Enter a subgoal title..."))
        self.titleLabel.setText(_translate("NewGoalWindow", "Subgoal Title"))
        self.cancelButton.setText(_translate("NewGoalWindow", "Cancel"))
        self.createSubgoalButton.setText(_translate("NewGoalWindow", "Create Subgoal"))
