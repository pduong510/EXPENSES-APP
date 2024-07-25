# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Logging an expense
def add_expense():
    amount = float(input('Enter the expense amount: £'))
    description = input('Enter a description of the expense: ')
    date = input('Enter a date (YYYY-MM-DD): ')

# '???' added into VALUES to prevent SQL injection
    mycursor.execute('INSERT INTO expenses (amount, description, date) VALUES (?, ?, ?)', (amount, description, date))

    conn.commit()
    print('Expense added successfully')

# Closes connection with database
    conn.close()    