# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\teoka\PycharmProjects\notes\client\ui\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 0, 20, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.newGoal = QtWidgets.QPushButton(self.centralwidget)
        self.newGoal.setGeometry(QtCore.QRect(340, 480, 50, 50))
        self.newGoal.setStyleSheet("border-radius:25px;\n"
"background-color: white;\n"
"font-size: 35px;\n"
"padding-bottom: 5px;\n"
"background-color: #081540;\n"
"color: white;\n"
"")
        self.newGoal.setIconSize(QtCore.QSize(16, 16))
        self.newGoal.setObjectName("newGoal")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.todayButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.todayButton.setMinimumSize(QtCore.QSize(0, 35))
        self.todayButton.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding: 10px;\n"
"border-bottom: 1px solid purple;")
        self.todayButton.setObjectName("todayButton")
        self.horizontalLayout.addWidget(self.todayButton)
        self.weeklyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.weeklyButton.setEnabled(True)
        self.weeklyButton.setMinimumSize(QtCore.QSize(0, 35))
        self.weeklyButton.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding: 10px;")
        self.weeklyButton.setObjectName("weeklyButton")
        self.horizontalLayout.addWidget(self.weeklyButton)
        self.overviewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.overviewButton.setMinimumSize(QtCore.QSize(0, 35))
        self.overviewButton.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding: 10px;")
        self.overviewButton.setObjectName("overviewButton")
        self.horizontalLayout.addWidget(self.overviewButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 70, 351, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.goals = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.goals.setContentsMargins(0, 0, 0, 0)
        self.goals.setObjectName("goals")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(440, 70, 331, 131))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.goalDescription = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.goalDescription.setContentsMargins(0, 0, 0, 0)
        self.goalDescription.setObjectName("goalDescription")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(440, 230, 331, 191))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.subgoals = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.subgoals.setContentsMargins(0, 0, 0, 0)
        self.subgoals.setObjectName("subgoals")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Goals"))
        self.newGoal.setText(_translate("MainWindow", "+"))
        self.todayButton.setText(_translate("MainWindow", "Today"))
        self.weeklyButton.setText(_translate("MainWindow", "Weekly"))
        self.overviewButton.setText(_translate("MainWindow", "Overview"))