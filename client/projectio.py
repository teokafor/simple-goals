import sqlite3

# Initial connection to database
con = sqlite3.connect('db/main.db')  # Connect to the main database file
cur = con.cursor()  # Create a cursor object
cur.execute("SELECT * FROM Goal")
rows = cur.fetchall()  # Get the rows from the table


class Row:
    def __init__(self, goal_id):
        self.__goal_id = goal_id
        cur.execute("SELECT * FROM Goal WHERE GoalID = ?", (self.__goal_id,))
        row = cur.fetchone()

        # Assign variables from row data
        self.__goal_name = row[1]
        self.__goal_desc = row[2]
        self.__start_date = row[3]
        self.__end_date = row[4]
        self.__time_spent = row[5]
        self.__completion = row[6]

    # Apparently, you cannot edit primary keys with sqlite. Oops!
   # def set_goal_id(self, new_goal_id):
       # self.__goal_id = new_goal_id
       # self.update_row()

    # Setters
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

    # Getters
    def get_goal_id(self): return self.__goal_id
    def get_goal_name(self): return self.__goal_name
    def get_goal_desc(self): return self.__goal_desc
    def get_start_date(self): return self.__start_date
    def get_end_date(self): return self.__end_date
    def get_time_spent(self): return self.__time_spent
    def get_completion(self): return self.__completion

    def update_row(self):
        sqlite_insert_with_param = "UPDATE Goal SET GoalName = ?, GoalDesc = ?, StartDate = ?, EndDate = ?, TimeSpent = ?, Completion = ? WHERE GoalID = ? ;"
        data_tuple = (self.__goal_name, self.__goal_desc, self.__start_date, self.__end_date, self.__time_spent, self.__completion, self.__goal_id)
        cur.execute(sqlite_insert_with_param, data_tuple)  # Modify the row linked to GoalID.
        con.commit()


# TODO: close connection to db at some point!
# For the Goal table:
# This creates an empty goal with an automatically generated ID.
def new_goal(goal_name, goal_desc):
    cur.execute("SELECT * FROM Goal")

    # Goal ID generation. The new ID will be the largest in the table + 1.
    largest = 0
    for row in rows:
        if row[0] > largest:
            largest = row[0]
    goal_id = (largest + 1)

    # Create and commit new row.
    sqlite_insert_with_param = "INSERT INTO Goal (GoalID, GoalName, GoalDesc, StartDate, EndDate, TimeSpent, Completion) VALUES (?, ?, ?, ?, ?, ?, ?);"
    data_tuple = (goal_id, goal_name, goal_desc, 'N/A', 'N/A', 0, 0)
    cur.execute(sqlite_insert_with_param, data_tuple)  # Create a row with the given information
    con.commit()  # Insert the new row


# Bare-bones delete function.
def delete_goal(goal_id):
    cur.execute("DELETE FROM Goal WHERE GOALID = ?", (goal_id,))
    con.commit()


# For the SubGoal table:
