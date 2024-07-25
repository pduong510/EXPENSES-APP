# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Update expense depending on ID field chosen by user
def update_expense():

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

    expense_id = int(input('Enter the ID number of the expense you wish to update: '))
    change_field = input('Which field would you like to change? (amount, description, date): ')
    new_value = input('Enter a new value for the field: ')

# '???' added into VALUES to prevent SQL injection
    try:
        if change_field == 'amount':
            mycursor.execute('UPDATE expenses SET amount = ? WHERE id = ?', (new_value, expense_id))
        elif change_field == 'description':
            mycursor.execute('UPDATE expenses SET description = ? WHERE id = ?', (new_value, expense_id))
        elif change_field == 'date':
            mycursor.execute('UPDATE expenses SET date = ? WHERE id = ?', (new_value, expense_id))
        else:
            print('Field name does not exist. Please try again.')

# Saves changes
        conn.commit()

        if mycursor.rowcount == 0:
            print('Enter a valid ID number. Please try again')
            return
        else:
            print('Expense updated successfully')
        
    except:
        print('Enter a valid input')

# Closes connection with database
        conn.close()
    
    