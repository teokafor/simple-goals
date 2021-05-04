import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QCursor, QPainterPath, QRegion, QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QCalendarWidget, QMessageBox

import projectio
from screen.home import Ui_MainWindow as HomeWindow
from screen.new_goal import Ui_NewGoalWindow as NewGoalWindow
from screen.edit_goal import Ui_NewGoalWindow as EditGoalWindow
from screen.new_subgoal import Ui_NewGoalWindow as NewSubGoalWindow
from screen.edit_subgoal import Ui_NewGoalWindow as EditSubGoalWindow
#from widget.entry_widget import EntryWidget
#from widget.subgoal_widget import SubgoalWidget  # Maybe merge this into entry_widget later?
from datetime import datetime

from projectio import Row, SubRow

APPLICATION = QApplication(sys.argv)
ROOT = QMainWindow()
HOME = HomeWindow()

# Global variable keeps track of what date tab was last open
date_tab = 0

# Global variable keeps track of what goal was last selected
last_goal_id = -1

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

    # Load whatever tab was selected last (if a goal has been selected yet)
    global date_tab
    if date_tab != 0:
        update_goal_list(date_tab)
    else:  # If no goal has been selected yet, load today's goals.
        update_goal_list(1)

    # Make widgets on home screen react to cursor hover
    cursor_hover()

    # Hide the new subgoals button by default.
    HOME.newSubgoal.hide()

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
    # Set the date tab to whatever tab was selected last
    global date_tab
    date_tab = date_limit

    # Load goals from the local database
    vbox = HOME.goals

    # Clear the current goals before re-instantiating them
    clear_layout(vbox)

    # Populate the goals list
    elements = projectio.make_goal_list()
    for entry in elements:
        today_date = datetime.today()
        end_date = datetime.strptime(entry.get_end_date(), "%Y-%m-%d")
        date_difference = (end_date-today_date).days

        if date_limit == 1:  # Due today
            if date_difference == -1:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == 2:  # Due this week
            if -1 <= date_difference <= 7:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == 3:  # Due anytime
            if -1 <= date_difference <= 999999:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)

    vbox.addStretch()
    cursor_hover()


def new_goal(name, description, start, end):
    projectio.new_goal(name, description, start, end)
    open_home()
    on_goal_click(last_goal_id)


def new_subgoal(goal_id, name):
    projectio.new_subgoal(goal_id, name)
    open_home()
    on_goal_click(last_goal_id)


def modify_goal(goal_id, name, description, end):
    modified = Row(goal_id)
    modified.set_goal_name(name)
    modified.set_goal_desc(description)
    modified.set_end_date(end)
    open_home()
    on_goal_click(last_goal_id)


def modify_subgoal(sub_id, goal_id, name):
    subgoal = SubRow(sub_id, goal_id)
    subgoal.set_sub_name(name)
    open_home()
    on_goal_click(last_goal_id)


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
    window.cancelButton.clicked.connect(lambda: on_goal_click(last_goal_id))
    window.createGoalButton.clicked.connect(lambda: new_goal(title.text(), description.toPlainText(), min_date.toPyDate(), calendar.selectedDate().toPyDate()))


def open_edit_goal(goal_id):
    window = EditGoalWindow()
    window.setupUi(ROOT)

    cursor_hover()
    current_row = Row(goal_id)

    # Obtain elements for reference
    title = window.titleEdit
    title.setText(current_row.get_goal_name())
    description = window.descriptionEdit
    description.setText(current_row.get_goal_desc())
    calendar = window.calendarWidget
    datetime.strptime(current_row.get_end_date(), "%Y-%m-%d")
    min_date = calendar.selectedDate()
    calendar.setSelectedDate(datetime.strptime(current_row.get_end_date(), "%Y-%m-%d"))
    title.setMinimumWidth(400)
    description.setMinimumWidth(400)
    description.setMaximumHeight(50)
    title.adjustSize()
    description.adjustSize()

    # Set minimum and maximum date range
    max_date = calendar.maximumDate()
    calendar.setDateRange(min_date, max_date)

    # Click handlers
    window.cancelButton.clicked.connect(open_home)
    window.cancelButton.clicked.connect(lambda: on_goal_click(last_goal_id))
    window.modifyGoalButton.clicked.connect(lambda: modify_goal(goal_id, title.text(), description.toPlainText(), calendar.selectedDate().toPyDate()))


def open_new_subgoal(goal_id):
    window = NewSubGoalWindow()
    window.setupUi(ROOT)
    cursor_hover()

    title = window.titleEdit

    # Click handlers
    window.cancelButton.clicked.connect(open_home)
    window.cancelButton.clicked.connect(lambda: on_goal_click(last_goal_id))
    window.createSubgoalButton.clicked.connect(lambda: new_subgoal(goal_id, title.text()))


def open_edit_subgoal(sub_id, goal_id):
    window = EditSubGoalWindow()
    window.setupUi(ROOT)
    cursor_hover()

    current_subgoal = SubRow(sub_id, goal_id)

    title = window.titleEdit

    title.setText(current_subgoal.get_sub_name())

    window.cancelButton.clicked.connect(open_home)
    window.cancelButton.clicked.connect(lambda: on_goal_click(last_goal_id))
    window.modifySubgoalButton.clicked.connect(lambda: modify_subgoal(sub_id, goal_id, title.text()))


# This function is run each time a goal is selected. It will update description and fetch subgoals.
def on_goal_click(goal_id):

    # Re-show the new subgoal button
    HOME.newSubgoal.show()
    HOME.newSubgoal.clicked.connect(lambda: open_new_subgoal(goal_id))

    # Set the global to the selected goal.
    global last_goal_id
    last_goal_id = goal_id

    # Don't run the rest of the function if no goal is currently selected.
    goals = projectio.make_goal_list()
    goal_exists = False
    for goal in goals:
        if last_goal_id == goal.get_goal_id():
            goal_exists = True
            last_goal_id = goal.get_goal_id()

    if goal_exists:
        # Create references to the GUI layouts
        description_layout = HOME.goalDescription
        subgoals_layout = HOME.subgoals

        # Populate the subgoals layout
        clear_layout(subgoals_layout)
        subgoals = projectio.make_subgoal_list(goal_id)
        for subgoal in subgoals:
            button = SubgoalWidget(subgoal, open_home)
            subgoals_layout.addWidget(button)

        description = projectio.Row(goal_id).get_goal_desc()

        clear_layout(description_layout)
        desc_label = QtWidgets.QLabel(description)
        description_layout.addWidget(desc_label)

        cursor_hover()



# This function will remove all widgets from any given layout.
def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


# TODO: SHOULD BE MOVED BACK INTO entry_widget.py!
class EntryWidget(QtWidgets.QPushButton):

    def remove(self):
        entry = self.entry
        message = DeleteWidget(entry.get_goal_name())
        if message.delete_flag:
            goal_id = entry.get_goal_id()
            projectio.delete_goal(goal_id)
            self.callback()
            # Prevents the program from attempting to load a non-existent goal, thus causing it to crash.
            if goal_id != last_goal_id:
                on_goal_click(last_goal_id)


    def edit(self):
        entry = self.entry
        open_edit_goal(entry.get_goal_id())

    # On activation, pass this goal's goal id to main.py. This is so we can easily manipulate the GUI.
    def select(self):
        entry = self.entry
        goal_id = entry.get_goal_id()
        on_goal_click(goal_id)

    def __init__(self, entry: Row, callback, *args, **kwargs):
        super(EntryWidget, self).__init__(*args, **kwargs)
        self.entry = entry
        self.callback = callback

        self.setAccessibleName("entryWidget")
        self.setMinimumHeight(65)
        self.setStyleSheet("""
        [accessibleName="entryWidget"] {
            border-radius: 15px 15px 0px 0px;
            border-bottom: 1px solid gray;
        }

        [accessibleName="editButton"] {
            border-radius: 15px 15px 0px 0px;
        }

        QWidget {
            background-color: #E8E8E8;
        }

        QCheckBox::indicator {
            width: 30px;
            height: 30px;
            background-color: white;
            border-radius: 5px;
        }

        QCheckBox::indicator::checked {
            background-color: green;
        }
        """)

        # Define the base layout as an HBox.
        layout = QtWidgets.QHBoxLayout()

        # The left-hand side (everything but the delete button) is an inner HBox.
        left = QtWidgets.QHBoxLayout()
        done = QtWidgets.QCheckBox()
        label = QtWidgets.QLabel(entry.get_goal_name())
        edit = QtWidgets.QPushButton("")
        edit.setAccessibleName("editButton")
        edit.setIcon(QIcon("resources/edit.png"))
        edit.clicked.connect(self.edit)
        left.addWidget(done)
        left.addWidget(label)
        left.addStretch()
        left.addWidget(edit)

        self.clicked.connect(self.select)

        # Delete button on the right-hand side
        delete = QtWidgets.QPushButton("")
        delete.clicked.connect(self.remove)
        delete.setIcon(QIcon("resources/delete.png"))
        delete.setMaximumWidth(38)
        delete.setMinimumWidth(38)
        delete.setMaximumHeight(38)
        delete.setMinimumHeight(38)
        delete.setStyleSheet("""
        QWidget {
            background-color: #B23535;
            border-radius: 5px;
        }
        """)

        layout.addLayout(left)
        layout.addWidget(delete)
        self.setLayout(layout)


# TODO: SHOULD BE MOVED BACK INTO subgoal_widget.py!
class SubgoalWidget(QtWidgets.QWidget):

    def on_check(self, state):
        self.subgoal.set_sub_completion(state)
        # TODO: Update this goal's completion rate

    def edit(self):
        open_edit_subgoal(self.subgoal.get_sub_id(), self.subgoal.get_goal_id())

    def remove(self):
        projectio.delete_subgoal(self.subgoal.get_sub_id(), self.subgoal.get_goal_id())
        on_goal_click(self.subgoal.get_goal_id())

    def __init__(self, subgoal: SubRow, callback, *args, **kwargs):
        super(SubgoalWidget, self).__init__(*args, **kwargs)

        self.subgoal = subgoal
        self.callback = callback

        layout = QtWidgets.QHBoxLayout()

        # Checkbox
        database_state = subgoal.get_sub_completion()
        done = QtWidgets.QCheckBox()
        done.setCheckState(database_state)  # Activate the checkbox if it's flagged in the database
        done.clicked.connect(lambda: self.on_check(done.checkState()))

        # Subgoal name
        label = QtWidgets.QLabel(subgoal.get_sub_name())

        # Edit button
        edit = QtWidgets.QPushButton('O')
        edit.setFixedWidth(30)
        edit.clicked.connect(self.edit)

        # Delete button
        delete = QtWidgets.QPushButton("X")
        delete.setFixedWidth(30)
        delete.clicked.connect(self.remove)

        # Add widgets to layout
        layout.addWidget(done)
        layout.addWidget(label)
        layout.addWidget(edit)
        layout.addWidget(delete)
        self.setLayout(layout)

# TODO: SHOULD BE MOVED INTO A SCRIPT OF ITS OWN!
class DeleteWidget(QtWidgets.QWidget):
    def __init__(self, goal_name, *args, **kwargs):
        super(DeleteWidget, self).__init__(*args, **kwargs)
        self.goal_name = goal_name
        self.delete_flag = False

        message_box = QMessageBox.question(self, f'Delete {self.goal_name}?', f'Are you sure you want to delete {self.goal_name}?')
        if message_box == QMessageBox.Yes:
            # TODO: Add extra condition here that will set proper goal id's if selections are off.
            self.delete_flag = True
        else:  # Probably not necessary.
            self.delete_flag = False


if __name__ == '__main__':
    open_home()

    # Display the root window.
    ROOT.show()
    sys.exit(APPLICATION.exec_())
