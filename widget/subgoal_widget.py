from PyQt5 import QtWidgets


class SubgoalWidget(QtWidgets.QWidget):
    def __init__(self, subgoal, *args, **kwargs):
        super(SubgoalWidget, self).__init__(*args, **kwargs)
        self.subgoal = subgoal

        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(self.subgoal[1])
        layout.addWidget(label)

        delete = QtWidgets.QPushButton("Delete")
        delete.setFixedWidth(30)
        layout.addWidget(delete)

        self.setLayout(layout)
        print(self.subgoal[1])
