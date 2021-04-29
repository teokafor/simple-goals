import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QCursor, QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QCalendarWidget

import projectio
from screen.home import Ui_MainWindow as HomeWindow
from screen.new_goal import Ui_NewGoalWindow as NewGoalWindow
from widget.entry_widget import EntryWidget
from widget.subgoal_widget import SubgoalWidget  # Maybe merge this into entry_widget later?
from datetime import datetime
from datetime import date

APPLICATION = QApplication(sys.argv)
ROOT = QMainWindow()
HOME = HomeWindow()


def open_home():
    """
    Opens the "Home" window.
    This window instance is global, so state will persist between screen changes.
    """
    HOME.setupUi(ROOT)

    # Button sizes
    HOME.todayButton.setMinimumHeight(50)
    HOME.todayButton.setMinimumWidth(100)
    HOME.weeklyButton.setMinimumHeight(50)
    HOME.weeklyButton.setMinimumWidth(100)
    HOME.overviewButton.setMinimumHeight(50)
    HOME.overviewButton.setMinimumWidth(100)

    # ROUND 
    # path = QPainterPath()
    # path.addRoundedRect(QtCore.QRectF(ROOT.rect()), 10, 10)
    # mask = QRegion(path.toFillPolygon().toPolygon())
    # ROOT.setMask(mask)

    # By default, show the goals due today.
    update_goal_list(-1)

    # Click handlers
    HOME.newGoal.clicked.connect(open_new_goal)
    HOME.todayButton.clicked.connect(lambda: update_goal_list(1))
    HOME.weeklyButton.clicked.connect(lambda: update_goal_list(2))
    HOME.overviewButton.clicked.connect(lambda: update_goal_list(3))


# This function will find any relevant elements in the current window and change the cursor style.
def cursor_hover():
    elements = []
    buttons = ROOT.findChildren(QPushButton)
    checkboxes = ROOT.findChildren(QCheckBox)
    calendar = ROOT.findChildren(QCalendarWidget)
    elements += buttons + checkboxes + calendar

    for element in elements:
        element.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


# The date limit will determine what goals are loaded.
def update_goal_list(date_limit):

    print(date_limit)

    # Load goals from the local database
    vbox = HOME.goals

    # Clear the current goals before re-instantiating them
    while HOME.goals.count():
        child = HOME.goals.takeAt(0)
        if child.widget():
            child.widget().deleteLater()

    # Populate the goals list
    elements = projectio.make_object_list()
    for entry in elements:
        today_date = datetime.today()
        end_date = datetime.strptime(entry.get_end_date(), "%Y-%m-%d")
        date_difference = (end_date-today_date).days

        if date_limit == 1:  # Due today
            if date_difference == -1:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == 2:  # Due this week
            if date_difference >= -1 & date_difference <= 7:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == 3:  # Due anytime
            if date_difference >= -1 & date_difference <= 999999:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)

    vbox.addStretch()
    cursor_hover()


# This function is run each time a goal is selected. It will update description and fetch subgoals.
def on_goal_click(goal_id):
    HOME.setupUi(ROOT)  # If this line isn't here, the program crashes.

    # Create references to the GUI layouts
    description_layout = HOME.goalDescription
    subgoals_layout = HOME.subgoals

    # Populate the subgoals layout
    subgoals = projectio.get_subgoals(goal_id)
    print('SUBGOALS:')
    for subgoal in subgoals:
        button = SubgoalWidget(subgoal)
        subgoals_layout.addWidget(button)

    print('\nDESCRIPTION:')
    description = projectio.Row(goal_id).get_goal_desc()
    print(description)


def new_goal(name, description, start, end):
    projectio.new_goal(name, description, start, end)
    open_home()


def open_new_goal():
    """
    Opens a new "Add Goal" window.
    A new instance is created each time this method is called, which means user-entered values will not persist.
    """
    window = NewGoalWindow()
    window.setupUi(ROOT)

    cursor_hover()

    # Obtain elements for reference
    title = window.titleEdit
    description = window.descriptionEdit
    calendar = window.calendarWidget
    title.setMinimumWidth(400)
    description.setMinimumWidth(400)
    description.setMaximumHeight(50)
    title.adjustSize()
    description.adjustSize()

    # Set minimum and maximum date range
    min_date = calendar.selectedDate()  # This will also be used for start_date
    max_date = calendar.maximumDate()
    calendar.setDateRange(min_date, max_date)

    # Click handlers
    window.cancelButton.clicked.connect(open_home)
    window.createGoalButton.clicked.connect(lambda: new_goal(title.text(), description.toPlainText(), min_date.toPyDate(), calendar.selectedDate().toPyDate()))


if __name__ == '__main__':
    open_home()

    # Display the root window.
    ROOT.show()
    sys.exit(APPLICATION.exec_())
