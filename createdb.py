# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Create a table

mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS expenses (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 amount REAL,
                 description TEXT,
                 date DATE
                 )
""")


conn.commit()

conn.close()