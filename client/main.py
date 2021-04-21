import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

from client import projectio
from client.screen.home import Ui_MainWindow as HomeWindow
from client.screen.new_goal import Ui_NewGoalWindow as NewGoalWindow
from client.widget.entry_widget import EntryWidget

APPLICATION = QApplication(sys.argv)
ROOT = QMainWindow()
HOME = HomeWindow()


def open_home():
    """
    Opens the "Home" window.
    This window instance is global, so state will persist between screen changes.
    """
    HOME.setupUi(ROOT)

    # Load goals from the local database
    vbox = HOME.goals

    elements = projectio.make_object_list()
    for entry in elements:
        button = EntryWidget(entry, open_home)
        vbox.addWidget(button)

    vbox.addStretch()

    # Click handlers
    HOME.newGoal.clicked.connect(open_new_goal)


def new_goal(name, description, date):
    projectio.new_goal(name, description, date)
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

    # Click handlers
    window.cancelButton.clicked.connect(open_home)
    window.createGoalButton.clicked.connect(lambda: new_goal(title.text(), description.toPlainText(), ""))


if __name__ == '__main__':
    open_home()

    # Display the root window.
    ROOT.show()
    sys.exit(APPLICATION.exec_())
