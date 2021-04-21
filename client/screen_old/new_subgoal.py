import tkinter as gui
from tkinter import ttk
import client.projectio

class NewSubGoalPage(gui.Frame):

    # Primary HomePage constructor
    def __init__(self, parent, controller):
        gui.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller

        # Simple label for testing
        simple_label = ttk.Label(self, text="Hello, world!")
        simple_label.grid(row=0, column=0)

        # Entry widget for the title of this goal w/ label
        title_label = ttk.Label(self, text="Title")
        title_label.grid(row=1, column=0)
        title_entry = ttk.Entry(self)
        title_entry.grid(row=2, column=0)
        self.title_entry = title_entry

        # Cancel button in the lower-left hand corner of the screen_old
        cancel = ttk.Button(self, text="Cancel", command=self.cancel)
        cancel.grid(row=10, column=0)

        # Submit button in the lower-right hand corner of the screen_old
        submit = ttk.Button(self, text="Submit", command=self.submit)
        submit.grid(row=10, column=3)

    def cancel(self):
        self.controller.open_home()

    def submit(self):
        self.controller.add_subgoal(self.title_entry.get())
        self.cancel()

