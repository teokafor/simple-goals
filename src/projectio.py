import sqlite3

con = None
cur = None


def initialize(database_location):
    global con
    global cur

    # Create the database file, if it does not already exist.
    con = sqlite3.connect(database_location)  # Create and connect to the main database file
    cur = con.cursor()  # Create a cursor object
    cur.execute(
        "CREATE TABLE IF NOT EXISTS Goal ('GoalID' INTEGER NOT NULL, 'GoalName' TEXT NOT NULL, 'GoalDesc' TEXT,'StartDate'	TEXT NOT NULL, 'EndDate' TEXT, 'TimeSpent' NUMERIC, 'Completion' NUMERIC, PRIMARY KEY('GoalID'))")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS SubGoal ('SubID' INTEGER NOT NULL, 'GoalID' INTEGER NOT NULL, 'SubName' TEXT NOT NULL, 'Completion' INTEGER NOT NULL, FOREIGN KEY('GoalID') REFERENCES 'Goal' ('GoalID'), PRIMARY KEY('SubID'))")
    con.commit()

    # Initial connection to database
    cur.execute("SELECT * FROM Goal")
    cur.execute('PRAGMA foreign_keys=ON')  # Enforce foreign keys. Needed to link subgoals to goals table.


# Objects of this class will represent an individual row present in the Goals table.
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

    # This method is called each time a variable is set.
    def update_row(self):
        insert = "UPDATE Goal SET GoalName = ?, GoalDesc = ?, StartDate = ?, EndDate = ?, TimeSpent = ?, Completion = ? WHERE GoalID = ? ;"
        data_tuple = (self.__goal_name, self.__goal_desc, self.__start_date, self.__end_date, self.__time_spent, self.__completion, self.__goal_id)
        cur.execute(insert, data_tuple)  # Modify the row linked to GoalID.
        con.commit()


# Objects of this class represent a row present in the SubGoals table. A matching goal id is required.
class SubRow:
    def __init__(self, sub_id, goal_id):
        self.__sub_id = sub_id
        self.__goal_id = goal_id
        cur.execute("SELECT * FROM Subgoal WHERE SubID = ? AND GoalID = ?", (self.__sub_id, self.__goal_id))
        row = cur.fetchone()
        self.__sub_name = row[2]
        self.__sub_completion = row[3]

    # Setters
    def set_sub_name(self, name):
        self.__sub_name = name
        self.update_subrow()

    def set_sub_completion(self, state):
        self.__sub_completion = state
        self.update_subrow()

    # Getters
    def get_sub_id(self): return self.__sub_id
    def get_goal_id(self): return self.__goal_id
    def get_sub_name(self): return self.__sub_name
    def get_sub_completion(self): return self.__sub_completion

    # Write setters changes to Subgoal table
    def update_subrow(self):
        insert = "UPDATE Subgoal SET SubName = ?, Completion = ? WHERE GoalID = ? AND SubID = ?"
        tuple = (self.__sub_name, self.__sub_completion, self.__goal_id, self.__sub_id)
        cur.execute(insert, tuple)
        con.commit()


# General functions not tied to either class:

# This adds a goal to the Goals table.
def new_goal(goal_name, goal_desc, start_date, end_date):
    cur.execute("SELECT * FROM Goal")
    # Create and commit new row.
    insert = "INSERT INTO Goal (GoalName, GoalDesc, StartDate, EndDate, TimeSpent, Completion) VALUES (?, ?, ?, ?, ?, ?);"
    data_tuple = (goal_name, goal_desc, start_date, end_date, 0, 0)
    cur.execute(insert, data_tuple)  # Create a row with the given information
    con.commit()  # Insert the new row


# Add a new subgoal to the SubGoals table.
def new_subgoal(goal_id, subgoal_name):
    insert = "INSERT INTO SubGoal (GoalID, SubName, Completion) VALUES (?, ?, ?);"
    tuple = (goal_id, subgoal_name, 0)
    cur.execute(insert, tuple)
    con.commit()


# Deletes a goal (and its potential subgoals) from the Goals (and SubGoals) table
def delete_goal(goal_id):
    # Delete subgoals first
    cur.execute("DELETE FROM Subgoal WHERE GoalID = ?", (goal_id,))
    # Now we can safely delete the goal itself
    cur.execute("DELETE FROM Goal WHERE GoalID = ?", (goal_id,))
    con.commit()


# Deletes a single subgoal from the SubGoals table.
def delete_subgoal(sub_id, goal_id):
    cur.execute("DELETE FROM Subgoal WHERE SubID = ? AND GoalID = ?", (sub_id, goal_id))
    con.commit()


# This function will return a list of goal objects that are created from each row in the Goals table.
def make_goal_list() -> 'list[Row]':
    cur.execute("SELECT * FROM Goal")
    rows = cur.fetchall()
    goals = []
    for row in rows:
        goal_id = row[0]
        goals.append(Row(goal_id))
    return goals


# This function will return a list of subgoal objects that are created from each row in the Subgoals table, with the specified goal id.
def make_subgoal_list(goal_id) -> 'list[SubRow]':
    cur.execute("SELECT * FROM Subgoal WHERE GoalID = ?", (goal_id,))
    rows = cur.fetchall()
    subgoals = []
    for row in rows:
        sub_id = row[0]
        subgoals.append(SubRow(sub_id, goal_id))
    return subgoals


# This function is called from main.py right before the application is about to close.
def close_database():
    con.close()
    print('Database connection closed.')
