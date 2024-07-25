# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Ask user for options
def show_options():
    print('------------------------------------------------')
    print('Please select from one of the following options:')
    print('------------------------------------------------')
    print('1. Add a new expense')
    print('2. Display summary of expenses')
    print('3. Update an existing expense')
    print('4. Delete an expense')
    print('5. Exit')