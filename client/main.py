# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

import tkinter as gui
from tkinter import ttk
from screen.home import HomePage
from screen.new_goal import NewGoalPage
from goal import Goal
import projectio

# Collection of goals stored on the client
goals = []


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
        self.show_frame(HomePage)

    def show_frame(self, entry):
        frame = self.frames[entry]
        frame.tkraise()

    def home(self):
        frame = self.frames[HomePage]
        frame.tkraise()

    def new_goal(self):
        frame = self.frames[NewGoalPage]
        frame.tkraise()

    def add_goal(self, title, description, date):
        """Adds a new goal to the local application.

        Args:
            goal (Goal): the new Goal to add
        """
        print("New goal has been added: " + title)
        projectio.new_goal(title, description, date)  # Create a new row entry.
        self.frames[HomePage].update_goals_listbox(projectio)

    def push(self):
        """Pushes local changes to the server.
        """

    def pull(self):
        """Pulls new changes from the server.
        """    


# Main entrypoint
app = Application()
app.geometry("500x400")
app.mainloop()
