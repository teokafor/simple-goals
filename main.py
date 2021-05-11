import os
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont, QCursor, QPainterPath, QRegion, QIcon, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QCheckBox, QCalendarWidget, QMessageBox, QSizePolicy, QLayout

import projectio
from screen.home import Ui_MainWindow as HomeWindow
from screen.new_goal import Ui_NewGoalWindow as NewGoalWindow
from screen.edit_goal import Ui_NewGoalWindow as EditGoalWindow
from screen.new_subgoal import Ui_NewGoalWindow as NewSubGoalWindow
from screen.edit_subgoal import Ui_NewGoalWindow as EditSubGoalWindow
#from widget.entry_widget import EntryWidget
#from widget.subgoal_widget import SubgoalWidget
from datetime import datetime

from projectio import Row, SubRow

APPLICATION = QApplication(sys.argv)
ROOT = QMainWindow()
HOME = HomeWindow()

# Global variable keeps track of what date tab was last open
date_tab = 1

# Global variable keeps track of what goal was last selected
last_goal_id = -1

# Constants
DUE_TODAY = 1
DUE_WEEKLY = 2
DUE_ANY = 3
DUE_PAST = 4


# CLASSES:

# A widget representation of a row from the Goals table.
class EntryWidget(QtWidgets.QPushButton):
    def __init__(self, entry: Row, callback, *args, **kwargs):
        super(EntryWidget, self).__init__(*args, **kwargs)
        self.entry = entry
        self.callback = callback
        self.latest_selection = False  # Determines whether the widget should darkened or not
        self.percentage = update_completion(self.entry.get_goal_id())
        self.qss = """
        [accessibleName="entryWidget"] {
            border-radius: 15px 15px 0px 0px;
        }

        [accessibleName="editButton"] {
            border-radius: 15px 15px 0px 0px;
            background-color: rgba(255, 255, 255, 0);
        }

        QWidget {
            background-color: white;
        }

        QWidget[selected = "0"] {
            background-color: white;
        }

        QWidget[selected = "1"] {
            background-color: #E8E4EF;
        }

        QLabel {
            background-color: rgba(255, 255, 255, 0);
        }

        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 10px;
            border: 1px solid blue;
            margin-left: 10px;
            margin-right: 5px;
        }

        QCheckBox::indicator::checked {
            background-color: #35B29D;
            background-image: url(resources/checked.png);
        }

        QCheckBox {
            background-color: rgba(255, 255, 255, 0);
        }
        """

        self.setAccessibleName("entryWidget")
        self.setMinimumHeight(60)
        self.setMinimumWidth(410)
        self.setStyleSheet(self.qss)

        # Define the base layout as an HBox.
        layout = QtWidgets.QHBoxLayout()

        # The left-hand side (everything but the delete button) is an inner HBox.
        left = QtWidgets.QHBoxLayout()
        done = QtWidgets.QCheckBox()
        checkbox_state = self.entry.get_completion()
        done.setCheckState(checkbox_state)
        done.clicked.connect(lambda: self.on_check(done.checkState()))
        label = QtWidgets.QLabel(entry.get_goal_name())
        self.percent_label = QtWidgets.QLabel(f'{self.percentage * 100:.2f}%')
        edit = QtWidgets.QPushButton("")
        edit.setAccessibleName("editButton")
        edit.setIcon(QIcon("resources/edit.png"))
        edit.clicked.connect(self.edit)
        left.addWidget(done)
        left.addWidget(label)
        left.addWidget(self.percent_label)
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

# EntryWidget methods:

    # Called when the delete button is clicked.
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

    # Called when the checkbox is toggled.
    def on_check(self, state):
        self.entry.set_completion(state)

    # Called when the edit button is pressed.
    def edit(self):
        entry = self.entry
        open_edit_goal(entry.get_goal_id())

    # Called when a subgoal of this goal has its checkbox toggled.
    def update_percent_label(self, percentage):
        self.percent_label.clear()
        self.percentage = percentage
        self.percent_label.setText(f'{percentage * 100:.2f}%')

    # Called when the body of the widget is pressed. It will update subgoals, description, and highlights.
    def select(self):
        entry = self.entry
        goal_id = entry.get_goal_id()
        on_goal_click(goal_id)



# A widget representation of an individual subgoal from the SubGoals table.
class SubgoalWidget(QtWidgets.QPushButton):
    def __init__(self, subgoal: SubRow, callback, *args, **kwargs):
        super(SubgoalWidget, self).__init__(*args, **kwargs)

        self.subgoal = subgoal
        self.callback = callback
        self.state = self.subgoal.get_sub_completion()
        self.setAccessibleName("entryWidget")
        self.setMinimumHeight(60)
        self.setMinimumWidth(410)
        self.setStyleSheet("""
                [accessibleName="entryWidget"] {
            border-radius: 15px 15px 0px 0px;
        }

        [accessibleName="editButton"] {
            border-radius: 15px 15px 0px 0px;
            background-color: rgba(255, 255, 255, 0);
        }

        QWidget {
            background-color: white;
        }

        QWidget[selected = "0"] {
            background-color: white;
        }

        QWidget[selected = "1"] {
            background-color: #E8E4EF;
        }

        QLabel {
            background-color: rgba(255, 255, 255, 0);
        }

        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 10px;
            border: 1px solid blue;
            margin-left: 10px;
            margin-right: 5px;
        }

        QCheckBox::indicator::checked {
            background-color: #35B29D;
            background-image: url(resources/checked.png);
        }

        QCheckBox {
            background-color: rgba(255, 255, 255, 0);
        }
                """)

        layout = QtWidgets.QHBoxLayout()

        # Checkbox
        database_state = subgoal.get_sub_completion()
        done = QtWidgets.QCheckBox()
        done.setCheckState(database_state)  # Activate the checkbox if it's flagged in the database
        done.clicked.connect(lambda: self.on_check(done.checkState()))

        # Subgoal name
        label = QtWidgets.QLabel(subgoal.get_sub_name())

        # Edit button
        edit = QtWidgets.QPushButton('')
        edit.setAccessibleName("editButton")
        edit.setIcon(QIcon("resources/edit.png"))
        edit.setFixedWidth(30)
        edit.clicked.connect(self.edit)

        # Delete button
        delete = QtWidgets.QPushButton('')
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

        layout.addWidget(done)
        layout.addWidget(label)
        layout.addStretch()
        layout.addWidget(edit)
        layout.addWidget(delete)
        self.setLayout(layout)

# SubgoalWidget methods:

    # This method updates the completion rate of this subgoal in the database. It also calls the corresponding EntryWidget to update its label.
    def on_check(self, state):
        self.state = state
        self.subgoal.set_sub_completion(state)
        goal_id = self.subgoal.get_goal_id()

        # Only manipulate the currently selected goal. The old system would re-instance all goals.
        index = HOME.goals.count()
        while index >= 2:
            child = HOME.goals.itemAt(index - 2)
            if child.widget():
                child = child.widget()
                if child.entry.get_goal_id() == goal_id:
                    correct_entry = child
            index -= 1
        correct_entry.update_percent_label(update_completion(goal_id))

    # This method is called when the edit button is pressed.
    def edit(self):
        open_edit_subgoal(self.subgoal.get_sub_id(), self.subgoal.get_goal_id())

    # This method is called when the delete button is pressed.
    def remove(self):
        projectio.delete_subgoal(self.subgoal.get_sub_id(), self.subgoal.get_goal_id())
        on_goal_click(self.subgoal.get_goal_id())
        self.on_check(self.state)


# Objects of this class are only created if inputs are invalid. Displays a warning message on creation.
class InvalidWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(InvalidWidget, self).__init__(*args, **kwargs)
        QMessageBox.warning(self, 'Error!', f'Input fields cannot be left blank.\nPlease try again.')


# Objects of this class are instantiated from the delete method in EntryWidget.
class DeleteWidget(QtWidgets.QWidget):
    def __init__(self, goal_name, *args, **kwargs):
        super(DeleteWidget, self).__init__(*args, **kwargs)
        self.goal_name = goal_name
        self.delete_flag = False

        message_box = QMessageBox.question(self, f'Delete {self.goal_name}?', f'Are you sure you want to delete {self.goal_name}?')
        if message_box == QMessageBox.Yes:
            self.delete_flag = True


# SCREENS:

# This screen displays the main window.
def open_home():
    """
    Opens the "Home" window.
    This window instance is global, so state will persist between screen changes.
    """
    HOME.setupUi(ROOT)

    # Button sizes
    HOME.todayButton.setMinimumHeight(50)
    HOME.todayButton.setMinimumWidth(125)
    HOME.weeklyButton.setMinimumHeight(50)
    HOME.weeklyButton.setMinimumWidth(125)
    HOME.overviewButton.setMinimumHeight(50)
    HOME.overviewButton.setMinimumWidth(125)

    HOME.pastButton.setMinimumHeight(50)
    HOME.pastButton.setMinimumWidth(125)
    HOME.filler.setStyleSheet("""QWidget {background-color: white;}""")

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
    HOME.todayButton.clicked.connect(lambda: update_goal_list(DUE_TODAY))
    HOME.weeklyButton.clicked.connect(lambda: update_goal_list(DUE_WEEKLY))
    HOME.overviewButton.clicked.connect(lambda: update_goal_list(DUE_ANY))
    HOME.pastButton.clicked.connect(lambda: update_goal_list(DUE_PAST))

    HOME.todayButton.setCheckable(True)
    HOME.todayButton.setChecked(True)
    HOME.todayButton.setStyleSheet("""
    QWidget {
        background-color: white;
        border: none;
        padding: 10px;
    }
        
    QWidget:checked {
        border-bottom: 2px solid purple;
    }
    """)

    HOME.weeklyButton.setCheckable(True)
    HOME.weeklyButton.setStyleSheet("""
        QWidget {
            background-color: white;
            border: none;
            padding: 10px;
        }
        
        QWidget:checked {
            border-bottom: 2px solid purple;
        }
        """)

    HOME.overviewButton.setCheckable(True)
    HOME.overviewButton.setStyleSheet("""
        QWidget {
            background-color: white;
            border: none;
            padding: 10px;
        }
        
        QWidget:checked {
            border-bottom: 2px solid purple;
        }
        """)

    HOME.pastButton.setCheckable(True)
    HOME.pastButton.setStyleSheet("""
        QWidget {
            background-color: white;
            border: none;
            padding: 10px;
        }
        
        QWidget:checked {
            border-bottom: 2px solid purple;
        }
        """)

    date_tab_style()


# This function displays the new goal screen.
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


# This function opens the edit goal screen.
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


# This function calls the new subgoal screen.
def open_new_subgoal(goal_id):
    window = NewSubGoalWindow()
    window.setupUi(ROOT)
    cursor_hover()

    title = window.titleEdit

    # Click handlers
    window.cancelButton.clicked.connect(open_home)
    window.cancelButton.clicked.connect(lambda: on_goal_click(last_goal_id))
    window.createSubgoalButton.clicked.connect(lambda: new_subgoal(goal_id, title.text()))


# This function calls the edit subgoal screen.
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


# Functions related to screens:

# This function is run each time a goal is selected. It will update description and fetch subgoals.
def on_goal_click(goal_id):
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
        # Re-show the new subgoal button
        HOME.newSubgoal.show()
        HOME.newSubgoal.clicked.connect(lambda: open_new_subgoal(goal_id))

        # Container widgets
        widget = HOME.subgoalWidget
        desc_widget = HOME.descriptionWidget

        # Create references to the GUI layouts
        description_layout = HOME.goalDescription
        description_layout.setContentsMargins(-2,-2,-2,-2)
        subgoals_layout = HOME.subgoals

        # Set the end date
        end_date_layout = HOME.endDateLayout
        clear_layout(end_date_layout)
        end_date = QtWidgets.QLabel(f'Due: {projectio.Row(goal_id).get_end_date()}')
        end_date_layout.addWidget(end_date)

        # Allow for equal subgoal spacing
        subgoals_layout.setSizeConstraint(QLayout.SetFixedSize)

        # Populate the subgoals layout
        clear_layout(subgoals_layout)
        subgoals = projectio.make_subgoal_list(goal_id)
        for subgoal in subgoals:
            button = SubgoalWidget(subgoal, open_home)
            subgoals_layout.addWidget(button)

        # Add spacers for top-alignment
        subgoals_layout.addStretch()

        # Set up the scroll area for subgoals
        widget.setLayout(subgoals_layout)
        scroll_area = HOME.subgoalScrollArea
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(ROOT.parentWidget())

        description = projectio.Row(goal_id).get_goal_desc()

        clear_layout(description_layout)
        desc_label = QtWidgets.QLabel(description)
        desc_label.setWordWrap(True)
        description_layout.addWidget(desc_label)

        # Add spacers for top-alignment
        description_layout.addStretch()

        # Scroll area for description
        desc_widget.setLayout(description_layout)
        desc_scroll_area = HOME.descriptionScrollArea
        desc_scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        desc_scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        desc_scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(ROOT.parentWidget())

        # Find this goal's EntryWidget object
        entry_widgets = get_entry_widget(goal_id)

        # If it exists, unpaint the last selected item
        if entry_widgets[1]:
            entry_widgets[1].setStyleSheet(entry_widgets[1].qss)
            entry_widgets[1].setProperty("selected", 0)
            entry_widgets[1].style().unpolish(entry_widgets[1])
            entry_widgets[1].style().polish(entry_widgets[1])
            entry_widgets[1].latest_selection = False

        # Set the clicked button to dark grey
        if entry_widgets[0]:
            entry_widgets[0].setStyleSheet(entry_widgets[0].qss)
            entry_widgets[0].setProperty("selected", 1)
            entry_widgets[0].style().unpolish(entry_widgets[0])
            entry_widgets[0].style().polish(entry_widgets[0])
            entry_widgets[0].latest_selection = True

        cursor_hover()


# This function will highlight the currently selected date tab. Called when the home screen is displayed and on tab selection.
def date_tab_style():
    # Update button selection status
    if date_tab == DUE_TODAY:
        HOME.todayButton.setChecked(True)
        HOME.weeklyButton.setChecked(False)
        HOME.overviewButton.setChecked(False)
        HOME.pastButton.setChecked(False)
    elif date_tab == DUE_WEEKLY:
        HOME.todayButton.setChecked(False)
        HOME.weeklyButton.setChecked(True)
        HOME.overviewButton.setChecked(False)
        HOME.pastButton.setChecked(False)
    elif date_tab == DUE_ANY:
        HOME.todayButton.setChecked(False)
        HOME.weeklyButton.setChecked(False)
        HOME.overviewButton.setChecked(True)
        HOME.pastButton.setChecked(False)
    elif date_tab == DUE_PAST:
        HOME.todayButton.setChecked(False)
        HOME.weeklyButton.setChecked(False)
        HOME.overviewButton.setChecked(False)
        HOME.pastButton.setChecked(True)


# This function will find any relevant elements in the current window and change the cursor style appropriately.
def cursor_hover():
    elements = []
    buttons = ROOT.findChildren(QPushButton)
    checkboxes = ROOT.findChildren(QCheckBox)
    calendar = ROOT.findChildren(QCalendarWidget)
    elements += buttons + checkboxes + calendar

    for element in elements:
        element.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


# When called (by selecting a date tab) this function will reload the current goals in the frame
def update_goal_list(date_limit):
    # Set the date tab to whatever tab was selected last
    global date_tab
    date_tab = date_limit

    # Container widget
    widget = HOME.widgetTest

    # Load goals from the local database
    vbox = HOME.goals
    vbox.setSizeConstraint(QLayout.SetFixedSize)

    # Clear the current goals before re-instantiating them
    clear_layout(vbox)

    # Populate the goals list
    elements = projectio.make_goal_list()
    for entry in elements:
        today_date = datetime.today()
        end_date = datetime.strptime(entry.get_end_date(), "%Y-%m-%d")
        date_difference = (end_date-today_date).days

        if date_limit == DUE_TODAY:  # Due today
            if date_difference == -1:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == DUE_WEEKLY:  # Due this week
            if -1 <= date_difference <= 6:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == DUE_ANY:  # Due anytime
            if -1 <= date_difference <= 999999:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)
        elif date_limit == DUE_PAST:  # Due date has passed
            if date_difference < -1:
                button = EntryWidget(entry, open_home)
                vbox.addWidget(button)

    widget.setLayout(vbox)
    scroll_area = HOME.scrollArea
    scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
    scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
    scroll_area.setWidgetResizable(True)
    scroll_area.setWidget(ROOT.parentWidget())

    date_tab_style()
    vbox.addStretch()
    on_goal_click(last_goal_id)
    cursor_hover()


# Called by open_new_goal()
def new_goal(name, description, start, end):
    error_exists = invalid_input([name, description])

    if not error_exists:
        projectio.new_goal(name, description, start, end)
        open_home()
        on_goal_click(last_goal_id)


# Called by open_new_subgoal()
def new_subgoal(goal_id, name):
    error_exists = invalid_input([name])

    if not error_exists:
        projectio.new_subgoal(goal_id, name)
        open_home()
        on_goal_click(last_goal_id)


# Called by open_edit_goal()
def modify_goal(goal_id, name, description, end):
    error_exists = invalid_input([name, description])

    if not error_exists:
        modified = Row(goal_id)
        modified.set_goal_name(name)
        modified.set_goal_desc(description)
        modified.set_end_date(end)
        open_home()
        on_goal_click(last_goal_id)


# Called by open_edit_subgoal()
def modify_subgoal(sub_id, goal_id, name):
    error_exists = invalid_input([name])

    if not error_exists:
        subgoal = SubRow(sub_id, goal_id)
        subgoal.set_sub_name(name)
        open_home()
        on_goal_click(last_goal_id)


# When called (by trying to create/modify a goal/subgoal) this function will determine if string inputs are valid.
def invalid_input(input_list):
    error_flag = False
    for item in input_list:
        if item == '':
            error_flag = True
    if error_flag:
        InvalidWidget()
        return error_flag


# This function will remove all widgets from any given layout. Usually followed by re-instancing the layout widgets.
def clear_layout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()


# This function updates the completion percentage for each goal.
def update_completion(goal_id):
    subgoals = projectio.make_subgoal_list(goal_id)

    sum = total = 0
    for subgoal in subgoals:
        if subgoal.get_sub_completion() == 2:
            sum += 1
        total += 1

    if total > 0:
        goal_completion = sum / total
    else:
        goal_completion = 0

    return goal_completion


# This function finds an EntryWidget object in the goals layout.
def get_entry_widget(goal_id):
    index = HOME.goals.count()
    current_last_list = [None, None]  # Retrieves the currently selected widget and the last selected widget.
    while index >= 2:
        child = HOME.goals.itemAt(index - 2)
        if child.widget():
            child = child.widget()
            if child.entry.get_goal_id() == goal_id:
                current_last_list[0] = child
            elif child.latest_selection:
                current_last_list[1] = child

        index -= 1
    return current_last_list


# Close the database before quitting.
def quit_program():
    APPLICATION.exec_()
    projectio.close_database()


if __name__ == '__main__':
    # Ensure the /db/ folder exists, then initialize the db file.
    try:
        os.mkdir("db")
    except FileExistsError:
        pass

    projectio.initialize()

    # Set custom font.
    font_id = QFontDatabase.addApplicationFont('resources/roboto-light.ttf')
    font_db = QFontDatabase()
    font_styles = font_db.styles('Roboto')
    font_families = QFontDatabase.applicationFontFamilies(font_id)
    font = font_db.font(font_families[0], font_styles[0], 12)
    APPLICATION.setFont(font)

    open_home()

    # Display the root window.
    ROOT.setFixedSize(1000, 708)
    ROOT.show()
    sys.exit(quit_program())
