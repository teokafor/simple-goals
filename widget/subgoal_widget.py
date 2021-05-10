from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon

from projectio import SubRow


class SubgoalWidget(QtWidgets.QPushButton):
    """
    A widget representation of an individual subgoal from the SubGoals table.
    """
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
                    background-color: #35B29D;
                    background-image: url(resources/checked.png);
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
        from main import HOME
        index = HOME.goals.count()
        while index >= 2:
            child = HOME.goals.itemAt(index - 2)
            if child.widget():
                child = child.widget()
                if child.entry.get_goal_id() == goal_id:
                    correct_entry = child
            index -= 1

        from main import update_completion
        correct_entry.update_percent_label(update_completion(goal_id))

    # This method is called when the edit button is pressed.
    def edit(self):
        from main import open_edit_subgoal
        open_edit_subgoal(self.subgoal.get_sub_id(), self.subgoal.get_goal_id())

    # This method is called when the delete button is pressed.
    def remove(self):
        import projectio
        projectio.delete_subgoal(self.subgoal.get_sub_id(), self.subgoal.get_goal_id())

        from main import on_goal_click
        on_goal_click(self.subgoal.get_goal_id())
        self.on_check(self.state)
