# TODO: close connection to db at some point!
import sqlite3

# Initial connection to database
con = sqlite3.connect('db/main.db')  # Connect to the main database file
cur = con.cursor()  # Create a cursor object
cur.execute("SELECT * FROM Goal")
rows = cur.fetchall()  # Get the rows from the table
cur.execute('PRAGMA foreign_keys=ON')  # Enforce foreign keys. Needed to link subgoals to goals table.

class Row:
    def __init__(self, goal_id):
        self.__goal_id = goal_id
        cur.execute("SELECT * FROM Goal WHERE GoalID = ?", (self.__goal_id,))
        row = cur.fetchone()

        # Assign goal table variables from row data
        self.__goal_name = row[1]
        self.__goal_desc = row[2]
        self.__start_date = row[3]
        self.__end_date = row[4]
        self.__time_spent = row[5]
        self.__completion = row[6]

    # Setters for goal table
    def set_goal_name(self, goal_name):
        self.__goal_name = goal_name
        self.update_row()

    def set_goal_desc(self, goal_desc):
        self.__goal_desc = goal_desc
        self.update_row()

    def set_start_date(self, start_date):
        self.__start_date = start_date
        self.update_row()

    def set_end_date(self, end_date):
        self.__end_date = end_date
        self.update_row()

    def set_time_spent(self, time_spent):
        self.__time_spent = time_spent
        self.update_row()

    def set_completion(self, completion):
        self.__completion = completion
        self.update_row()

    # Getters for goal table
    def get_goal_id(self): return self.__goal_id
    def get_goal_name(self): return self.__goal_name
    def get_goal_desc(self): return self.__goal_desc
    def get_start_date(self): return self.__start_date
    def get_end_date(self): return self.__end_date
    def get_time_spent(self): return self.__time_spent
    def get_completion(self): return self.__completion

    def update_row(self):
        insert = "UPDATE Goal SET GoalName = ?, GoalDesc = ?, StartDate = ?, EndDate = ?, TimeSpent = ?, Completion = ? WHERE GoalID = ? ;"
        data_tuple = (self.__goal_name, self.__goal_desc, self.__start_date, self.__end_date, self.__time_spent, self.__completion, self.__goal_id)
        cur.execute(insert, data_tuple)  # Modify the row linked to GoalID.
        con.commit()

    # Subgoal-related functions:
    # Retrieve all subgoals associated with this goal.
    def get_subgoals(self):
        insert = "SELECT * FROM Subgoal WHERE GoalID = ?"
        data_tuple = (self.__goal_id,)
        cur.execute(insert, data_tuple)
        subgoals = cur.fetchall()
        return subgoals


# General functions not tied to the Row class:
# This creates an empty goal with an automatically generated ID.
def new_goal(goal_name, goal_desc, end_date):
    cur.execute("SELECT * FROM Goal")
    # Create and commit new row.
    insert = "INSERT INTO Goal (GoalName, GoalDesc, StartDate, EndDate, TimeSpent, Completion) VALUES (?, ?, ?, ?, ?, ?);"
    data_tuple = (goal_name, goal_desc, 'N/A', end_date, 0, 0)
    cur.execute(insert, data_tuple)  # Create a row with the given information
    con.commit()  # Insert the new row


# Create a new subgoal.
def new_subgoal(goal_id, subgoal_name):
    insert = "INSERT INTO SubGoal (GoalID, SubName, Completion) VALUES (?, ?, ?);"
    tuple = (goal_id, subgoal_name, 0)
    cur.execute(insert, tuple)
    con.commit()


# Delete function.
def delete_goal(goal_id):
    # Delete subgoals first
    cur.execute("DELETE FROM Subgoal WHERE GoalID = ?", (goal_id,))
    # Now we can safely delete the goal itself
    cur.execute("DELETE FROM Goal WHERE GoalID = ?", (goal_id,))
    con.commit()


# This function will return a list of objects that are created from each row in the database.
def make_object_list():
    cur.execute("SELECT * FROM Goal")
    rows = cur.fetchall()
    goals = []
    for row in rows:
        goal_id = row[0]
        goals.append(Row(goal_id))
    return goals
