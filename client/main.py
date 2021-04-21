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


def new_goal():
    """
    Opens a new "Add Goal" window.
    A new instance is created each time this method is called, which means user-entered values will not persist.
    """
    new_goal_window = NewGoalWindow()
    new_goal_window.setupUi(ROOT)


if __name__ == '__main__':
    # Create an instance of our home window and assign button-click events.
    HOME.setupUi(ROOT)
    HOME.newGoal.clicked.connect(new_goal)

    # Display the root window.
    ROOT.show()
    sys.exit(APPLICATION.exec_())
