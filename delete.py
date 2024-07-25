# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Delete an expense depending on ID field
def delete_expense():

    mycursor.execute('SELECT * FROM expenses')
# Fetches rows from the last executed statement
    view_expense = mycursor.fetchall()

    print('Your current expenses:')
    print('| ID | Amount | Description | Date |')

# Displays current expenses. If none found, exits and returns to main function
    if view_expense:
        for view in view_expense:
            print(view)
        
    else:
        print('No expenses found')
        return

    expense_id = int(input('Enter the ID number of the expense you wish to delete: '))

    try:
        mycursor.execute(f'DELETE FROM expenses WHERE id = {expense_id}')
        conn.commit()
        
        if mycursor.rowcount == 0:
            print('Enter a valid ID number. Please try again')
            return
        else:
            print('Expense deleted successfully')

    except ValueError:
        print('Enter a valid input')

# Closes connection with database
        conn.close()