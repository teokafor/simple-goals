# https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/

import tkinter as gui
from tkinter import messagebox
from tkinter import ttk
from screen.home import HomePage
from screen.new_goal import NewGoalPage
from screen.new_subgoal import NewSubGoalPage
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
        for Entry in (HomePage, NewGoalPage, NewSubGoalPage):
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

    def delete_goal(self):
        answer = messagebox.askokcancel('Delete goal?', f'Are you sure you want to delete this goal?')
        if answer:
            self.delete_goal_confirm()

    def delete_goal_confirm(self):
        goal_id = self.frames[HomePage].get_selected_goal_id()
        projectio.delete_goal(goal_id)
        self.frames[HomePage].update_goals_listbox()

    def new_subgoal(self):
        frame = self.frames[NewSubGoalPage]
        frame.tkraise()

    def add_goal(self, title, description, date):
        """Adds a new goal to the local application.

        Args:
            goal (Goal): the new Goal to add
        """
        projectio.new_goal(title, description, date)  # Create a new row entry.
        self.frames[HomePage].update_goals_listbox()

    def add_subgoal(self, title):
        goal_id = self.frames[HomePage].get_selected_goal_id()
        projectio.new_subgoal(goal_id, title)

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
