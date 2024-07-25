# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Display summary of expense
def show_expenses():

    mycursor.execute('SELECT * FROM expenses')
# Fetches rows from the last executed statement
    view_expense = mycursor.fetchall()

    print('Your current expenses:')
    print('| ID | Amount | Description | Date |')

    if view_expense:
        for view in view_expense:
            print(view)

    else:
        print('No expenses found')