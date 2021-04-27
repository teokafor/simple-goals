import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QCursor, QPainterPath, QRegion
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

import projectio
from screen.home import Ui_MainWindow as HomeWindow
from screen.new_goal import Ui_NewGoalWindow as NewGoalWindow
from widget.entry_widget import EntryWidget
from widget.subgoal_widget import SubgoalWidget  # Maybe merge this into entry_widget later?

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
    path = QPainterPath()
    path.addRoundedRect(QtCore.QRectF(ROOT.rect()), 10, 10)
    mask = QRegion(path.toFillPolygon().toPolygon())
    ROOT.setMask(mask)

    # Hovering cursor styles
    children = ROOT.findChildren(QPushButton)
    for element in children:
        element.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

    # Load goals from the local database
    vbox = HOME.goals

    elements = projectio.make_object_list()
    for entry in elements:
        button = EntryWidget(entry, open_home)
        vbox.addWidget(button)

    vbox.addStretch()

    # Click handlers
    HOME.newGoal.clicked.connect(open_new_goal)


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

    # Obtain elements for reference
    title = window.titleEdit
    description = window.descriptionEdit
    end_date = window.calendarWidget
    title.setMinimumWidth(400)
    description.setMinimumWidth(400)
    description.setMaximumHeight(50)
    title.adjustSize()
    description.adjustSize()

    # Set minimum and maximum date range
    min_date = end_date.selectedDate()  # This will also be used for start_date
    max_date = end_date.maximumDate()
    end_date.setDateRange(min_date, max_date)

    # Click handlers
    window.cancelButton.clicked.connect(open_home)
    window.createGoalButton.clicked.connect(lambda: new_goal(title.text(), description.toPlainText(), min_date.toPyDate(), end_date.selectedDate().toPyDate()))


if __name__ == '__main__':
    open_home()

    # Display the root window.
    ROOT.show()
    sys.exit(APPLICATION.exec_())