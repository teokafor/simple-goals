import tkinter as gui
from tkinter import ttk

class HomePage(gui.Frame):

    # Primary HomePage constructor
    def __init__(self, parent, controller):
        gui.Frame.__init__(self, parent)

        # Simple label for testing
        simple_label = ttk.Label(self, text="Hello, world!")
        simple_label.grid(row=0, column=0)

        # Add-new-goal button
        cancel = ttk.Button(self, text="Cancel", command=controller.new_goal)
        cancel.grid(row=10, column=0)