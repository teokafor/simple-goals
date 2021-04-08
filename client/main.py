# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

import tkinter as gui
from tkinter import ttk
from screen.home import HomePage
from screen.new_goal import NewGoalPage

class Application(gui.Tk):

    # Primary constructor for the root application window
    def __init__(self, *args, **kwargs):
        gui.Tk.__init__(self, *args, **kwargs)

        # Create our base container
        container = gui.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # Create an array of frames, each of which represents a window in our application.
        self.frames = {}

        # Iterate over our pages.
        # For each page, initialize it, and add it as a frame.
        for Entry in (HomePage, NewGoalPage):
            instance = Entry(container, self)
            self.frames[Entry] = instance
            instance.grid(row=0, column=0, sticky="nsew")

        # Show the home frame.
        self.show_frame(NewGoalPage)

    def show_frame(self, entry):
        frame = self.frames[entry]
        frame.tkraise()

    def home(self):
        frame = self.frames[HomePage]
        frame.tkraise()

    def new_goal(self):
        frame = self.frames[NewGoalPage]
        frame.tkraise()

# Main entrypoint
app = Application()
app.geometry("500x400")
app.mainloop()