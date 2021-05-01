from PyQt5 import QtWidgets


class SubgoalWidget(QtWidgets.QWidget):
    def __init__(self, subgoal, callback, *args, **kwargs):
        super(SubgoalWidget, self).__init__(*args, **kwargs)

        self.subgoal = subgoal
        self.callback = callback

        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel(self.subgoal[1])
        layout.addWidget(label)

        delete = QtWidgets.QPushButton("X")
        delete.setFixedWidth(30)
        print(self.subgoal[1])
        layout.addWidget(delete)
        self.setLayout(layout)
