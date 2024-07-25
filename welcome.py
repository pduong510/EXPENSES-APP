# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Welcome user
def welcome_user():
    print('\n')
    print('------ Welcome to the Expense Tracker App ------')