import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from client.screen.home import Ui_MainWindow as HomeWindow


def new_goal():
    print("Opening new goal GUI.")


if __name__ == '__main__':
    # Initialize our application and create a root window.
    app = QApplication(sys.argv)
    root = QMainWindow()

    # Create an instance of our home window and assign button-click events.
    home = HomeWindow()
    home.setupUi(root)
    home.newGoal.clicked.connect(new_goal)

    # Display the root window.
    root.show()
    sys.exit(app.exec_())
