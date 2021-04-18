import tkinter as gui
from tkinter import ttk
from client import projectio

class HomePage(gui.Frame):

    # Primary HomePage constructor
    def __init__(self, parent, controller):
        gui.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        # Simple label for testing
        self.simple_label = ttk.Label(self, text="Hello, world!")
        self.simple_label.grid(row=0, column=0)

        # Add-new-goal button
        self.new_goal = ttk.Button(self, text="New Goal", command=self.controller.new_goal)
        self.new_goal.grid(row=10, column=0)

        # TODO: Only make subgoal button visible/press-able when a goal is selected.
        # Subgoal Button
        self.new_subgoal = ttk.Button(self, text="New Subgoal", command=self.controller.new_subgoal)
        self.new_subgoal.grid(row=10, column=2)

        # Listbox for Goals table
        self.goals_listbox = gui.Listbox(self, height=15, width=25, selectmode=gui.SINGLE)
        self.goals_listbox.grid(row=5, column=0)
        self.goals_listbox.bind('<<ListboxSelect>>', self.retrieve_subgoals)

        # Scrollbar for goals Listbox
        self.goals_v_scrollbar = gui.Scrollbar(self, orient='vertical', command=self.goals_listbox.yview)
        self.goals_v_scrollbar.grid(row=5, column=1, sticky='ns')
        self.goals_listbox.config(yscrollcommand=self.goals_v_scrollbar.set)

        # Populate goals Listbox on startup
        self.update_goals_listbox()

    # Should be called when adding, editing, and removing goals from the Listbox
    def update_goals_listbox(self):
        # Clear existing goals.
        self.goals_listbox.delete(0, gui.END)

        # Retrieve list of goals and add to Listbox
        goals = projectio.make_object_list()

        for goal in goals:
            self.goals_listbox.insert(gui.END, goal.get_goal_name())

    def retrieve_subgoals(self, event):
        index = self.goals_listbox.curselection()
        goals = projectio.make_object_list()
        subgoals = goals[index[0]].get_subgoals()
        for subgoal in subgoals:
            print(subgoal[1])

    def get_selected_goal_id(self):
        index = self.goals_listbox.curselection()
        goals = projectio.make_object_list()
        return goals[index[0]].get_goal_id()
