import tkinter as gui
from tkinter import ttk
from tkcalendar import Calendar

class NewGoalPage(gui.Frame):

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

        # Entry widget for a general description of this goal w/ label.
        description_label = ttk.Label(self, text="Description")
        description_label.grid(row=3, column=0)
        description_entry = ttk.Entry(self)
        description_entry.grid(row=4, column=0)

        # Due-date selector
        calendar = Calendar(self)
        calendar.grid(row=7, column=0)

        # Cancel button in the lower-left hand corner of the screen
        cancel = ttk.Button(self, text="Cancel", command=self.cancel)
        cancel.grid(row=10, column=0)

        # Submit button in the lower-right hand corner of the screen
        submit = ttk.Button(self, text="Submit")
        submit.grid(row=10, column=3)

    def cancel(self):
        self.controller.home()
        