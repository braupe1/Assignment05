# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# BRaupe,2023.05.13,Created started script
# BRaupe,2023.05.14,Added Try-Except and With functions
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try: # Try to open file if exists
    with open(objFile, "r") as readfile: # Use with to open and read in file data
        for line in readfile:
            task, priority = line.strip().split(",") # Buckets the task and priority by stripping the comma
            dicRow = {"Task": task, "Priority": priority} # Adds line data to dictionary
            lstTable.append(dicRow) # Adds dictionary data to list table
except FileNotFoundError: # Provide a clear message to indicate the text file does not exist
    print("No existing data found. Starting with an empty list.")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        # TODO: Add Code Here
        if len(lstTable) == 0: # Checks the list table to see if any data is available
            print("No data available.")
        else:
            print("Current Data:")
            for row in lstTable: # Prints the List table data with the dictionary header names
                print("Task:", row["Task"], "Priority:", row["Priority"])
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        # TODO: Add Code Here
        task = input("Enter the task: ") # User entry of the task
        priority = input("Enter the priority: ") # User entry of the priority
        dicRow = {"Task": task, "Priority": priority} # Task and priority entries place in dictionary row
        lstTable.append(dicRow) # Simple list table append of the new dictionary row entered
        print("Task added.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        # TODO: Add Code Here
        if len(lstTable) == 0: # Checks the list table to see if any data is available
            print("No data available to remove.")
        else:
            task = input("Enter the task to remove: ") # User entry of task to remove
            for row in lstTable:
                if row["Task"].lower() == task.lower(): # Converts task to lowercase
                    lstTable.remove(row) # Removes selected task row
                    print("Task removed.")
                    break # Breaks the for and if statement
        continue

    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        # TODO: Add Code Here
        with open(objFile, "w") as file: # Use with to open and write in file data
            for row in lstTable: # Converts list table to row data with task and priority with new line
                file.write(row["Task"] + "," + row["Priority"] + "\n")
        print("Data saved to file.")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        # TODO: Add Code Here
        print("Program successfully ended.") # Simple print statement indicating the user is exiting program
        break  #
