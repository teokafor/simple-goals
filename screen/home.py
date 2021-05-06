# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/home.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 701)
        MainWindow.setStyleSheet("background-color: #F6F5F9; font-size: 20px;")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(500, 0, 20, 711))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.newGoal = QtWidgets.QPushButton(self.centralwidget)
        self.newGoal.setGeometry(QtCore.QRect(430, 630, 50, 50))
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
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1001, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.expandLeft = QtWidgets.QHBoxLayout()
        self.expandLeft.setSpacing(0)
        self.expandLeft.setObjectName("expandLeft")
        self.overviewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.overviewButton.setMinimumSize(QtCore.QSize(0, 35))
        self.overviewButton.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding: 10px;")
        self.overviewButton.setObjectName("overviewButton")
        self.expandLeft.addWidget(self.overviewButton)
        self.todayButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.todayButton.setMinimumSize(QtCore.QSize(0, 35))
        self.todayButton.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding: 10px;\n"
"border-bottom: 1px solid purple;")
        self.todayButton.setObjectName("todayButton")
        self.expandLeft.addWidget(self.todayButton)
        self.weeklyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.weeklyButton.setEnabled(True)
        self.weeklyButton.setMinimumSize(QtCore.QSize(0, 35))
        self.weeklyButton.setStyleSheet("background-color: white;\n"
"border: none;\n"
"padding: 10px;")
        self.weeklyButton.setObjectName("weeklyButton")
        self.expandLeft.addWidget(self.weeklyButton)
        self.expandLeft.setStretch(0, 1)
        self.expandLeft.setStretch(1, 1)
        self.expandLeft.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.expandLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.newSubgoal = QtWidgets.QPushButton(self.centralwidget)
        self.newSubgoal.setGeometry(QtCore.QRect(930, 560, 25, 25))
        self.newSubgoal.setStyleSheet("border-radius:25px;\n"
"background-color: white;\n"
"font-size: 35px;\n"
"padding-bottom: 5px;\n"
"background-color: #081540;\n"
"color: white;\n"
"")
        self.newSubgoal.setIconSize(QtCore.QSize(16, 16))
        self.newSubgoal.setObjectName("newSubgoal")
        self.widgetTest = QtWidgets.QWidget(self.centralwidget)
        self.widgetTest.setGeometry(QtCore.QRect(30, 80, 451, 511))
        self.widgetTest.setObjectName("widgetTest")
        self.scrollArea = QtWidgets.QScrollArea(self.widgetTest)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 451, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 451, 511))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.goals = QtWidgets.QVBoxLayout()
        self.goals.setContentsMargins(0, -1, -1, -1)
        self.goals.setSpacing(25)
        self.goals.setObjectName("goals")
        self.verticalLayout.addLayout(self.goals)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.subgoalWidget = QtWidgets.QWidget(self.centralwidget)
        self.subgoalWidget.setGeometry(QtCore.QRect(530, 80, 451, 321))
        self.subgoalWidget.setObjectName("subgoalWidget")
        self.subgoalScrollArea_nw = QtWidgets.QScrollArea(self.subgoalWidget)
        self.subgoalScrollArea_nw.setEnabled(False)
        self.subgoalScrollArea_nw.setGeometry(QtCore.QRect(10, 10, 431, 301))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subgoalScrollArea_nw.sizePolicy().hasHeightForWidth())
        self.subgoalScrollArea_nw.setSizePolicy(sizePolicy)
        self.subgoalScrollArea_nw.setMinimumSize(QtCore.QSize(0, 301))
        self.subgoalScrollArea_nw.setWidgetResizable(True)
        self.subgoalScrollArea_nw.setObjectName("subgoalScrollArea_nw")
        self.scrollAreaWidgetContents_200 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_200.setGeometry(QtCore.QRect(0, 0, 429, 299))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_200.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_200.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_200.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_200.setObjectName("scrollAreaWidgetContents_200")
        self.subgoalScrollArea_nw.setWidget(self.scrollAreaWidgetContents_200)
        self.subgoalScrollArea = QtWidgets.QScrollArea(self.subgoalWidget)
        self.subgoalScrollArea.setEnabled(True)
        self.subgoalScrollArea.setGeometry(QtCore.QRect(0, 0, 451, 321))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subgoalScrollArea.sizePolicy().hasHeightForWidth())
        self.subgoalScrollArea.setSizePolicy(sizePolicy)
        self.subgoalScrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.subgoalScrollArea.setAcceptDrops(False)
        self.subgoalScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.subgoalScrollArea.setWidgetResizable(True)
        self.subgoalScrollArea.setObjectName("subgoalScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 451, 321))
        self.scrollAreaWidgetContents_2.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.subgoals = QtWidgets.QVBoxLayout()
        self.subgoals.setSpacing(25)
        self.subgoals.setObjectName("subgoals")
        self.verticalLayout_2.addLayout(self.subgoals)
        self.subgoalScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.descriptionWidget = QtWidgets.QWidget(self.centralwidget)
        self.descriptionWidget.setGeometry(QtCore.QRect(520, 420, 461, 131))
        self.descriptionWidget.setObjectName("descriptionWidget")
        self.descriptionScrollArea = QtWidgets.QScrollArea(self.descriptionWidget)
        self.descriptionScrollArea.setEnabled(True)
        self.descriptionScrollArea.setGeometry(QtCore.QRect(10, 0, 451, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.descriptionScrollArea.sizePolicy().hasHeightForWidth())
        self.descriptionScrollArea.setSizePolicy(sizePolicy)
        self.descriptionScrollArea.setMinimumSize(QtCore.QSize(0, 100))
        self.descriptionScrollArea.setAcceptDrops(False)
        self.descriptionScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.descriptionScrollArea.setWidgetResizable(True)
        self.descriptionScrollArea.setObjectName("descriptionScrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 451, 131))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.goalDescription = QtWidgets.QVBoxLayout()
        self.goalDescription.setObjectName("goalDescription")
        self.verticalLayout_3.addLayout(self.goalDescription)
        self.descriptionScrollArea.setWidget(self.scrollAreaWidgetContents_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Simple Goals"))
        self.newGoal.setText(_translate("MainWindow", "+"))
        self.overviewButton.setText(_translate("MainWindow", "Overview"))
        self.todayButton.setText(_translate("MainWindow", "Today"))
        self.weeklyButton.setText(_translate("MainWindow", "Weekly"))
        self.newSubgoal.setText(_translate("MainWindow", "+"))
