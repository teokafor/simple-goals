import sqlite3

# Initial connection to database
con = sqlite3.connect('db/main.db')  # Connect to the main database file
cur = con.cursor()  # Create a cursor object


# TODO: close connection to db at some point!
# For the Goal table:
# This creates an empty goal with an automatically generated ID
def new_goal(goal_name):
    cur.execute("SELECT * FROM Goal")
    rows = cur.fetchall()  # Get the rows from the table
    goal_id = len(rows)  # The primary key GoalID is simply the index of the new row
    sqlite_insert_with_param = "INSERT INTO Goal (GoalID, GoalName, StartDate, EndDate, TimeSpent, Completion) VALUES (?, ?, ?, ?, ?, ?);"
    data_tuple = (goal_id, goal_name, 'N/A', 'N/A', 0, 0)
    cur.execute(sqlite_insert_with_param, data_tuple)  # Create a row with the given information
    con.commit()  # Insert the new row


# Modify any existing goal. I might break this up into several smaller functions so you don't need to pass every column.
def modify_goal(goal_name, start_date, end_date, time_spent, completion, goal_id):
    sqlite_insert_with_param = "UPDATE Goal SET GoalName = ?, StartDate = ?, EndDate = ?, TimeSpent = ?, Completion = ? WHERE GoalID = ? ;"
    data_tuple = (goal_name, start_date, end_date, time_spent, completion, goal_id)
    cur.execute(sqlite_insert_with_param, data_tuple)  # Modify the row linked to GoalID.
    con.commit()


# Barebones delete function.
def delete_goal(goal_id):
    cur.execute("DELETE FROM Goal WHERE GOALID = ?", (goal_id,))
    con.commit()

# For the SubGoal table:
