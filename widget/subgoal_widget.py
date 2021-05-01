#from PyQt5 import QtWidgets
#
#
#class SubgoalWidget(QtWidgets.QWidget):
#    def __init__(self, subgoal, callback, *args, **kwargs):
#        super(SubgoalWidget, self).__init__(*args, **kwargs)
#
#        self.subgoal = subgoal
#        self.callback = callback
#
#        layout = QtWidgets.QHBoxLayout()
#        label = QtWidgets.QLabel(self.subgoal[1])
#        layout.addWidget(label)
#
#        done = QtWidgets.QCheckBox()
#
#        edit = QtWidgets.QPushButton('O')
#        edit.setFixedWidth(30)
#
#        delete = QtWidgets.QPushButton("X")
#        delete.setFixedWidth(30)
#
#        layout.addWidget(done)
#        layout.addWidget(edit)
#        layout.addWidget(delete)
#        self.setLayout(layout)
#