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
        self.centralwidget = QtWidgets.QWidget(NewGoalWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 120, 71, 21))
        self.label.setObjectName("label")
        NewGoalWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NewGoalWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        NewGoalWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NewGoalWindow)
        self.statusbar.setObjectName("statusbar")
        NewGoalWindow.setStatusBar(self.statusbar)

        self.retranslateUi(NewGoalWindow)
        QtCore.QMetaObject.connectSlotsByName(NewGoalWindow)

    def retranslateUi(self, NewGoalWindow):
        _translate = QtCore.QCoreApplication.translate
        NewGoalWindow.setWindowTitle(_translate("NewGoalWindow", "MainWindow"))
        self.label.setText(_translate("NewGoalWindow", "Hello, world!"))
