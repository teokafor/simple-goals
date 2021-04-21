import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from client.screen.home import Ui_MainWindow as HomeWindow
from client.screen.new_goal import Ui_NewGoalWindow as NewGoalWindow

APPLICATION = QApplication(sys.argv)
ROOT = QMainWindow()
HOME = HomeWindow()


def home():
    """
    Opens the "Home" window.
    This window instance is global, so state will persist between screen changes.
    """
    HOME.setupUi(ROOT)

    # Click handlers
    HOME.newGoal.clicked.connect(new_goal)


def new_goal():
    """
    Opens a new "Add Goal" window.
    A new instance is created each time this method is called, which means user-entered values will not persist.
    """
    new_goal_window = NewGoalWindow()
    new_goal_window.setupUi(ROOT)

    # Click handlers
    new_goal_window.cancelButton.clicked.connect(home)


if __name__ == '__main__':
    home()

    # Display the root window.
    ROOT.show()
    sys.exit(APPLICATION.exec_())
