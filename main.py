# Expense tracker

# Import SQL to Python
import sqlite3
import datetime

# Create and connect to the database

conn = sqlite3.connect('expensetracker.db')

# Create a cursor to interact with database
mycursor = conn.cursor()

# Import other module functions
import add
import delete
import options
import update
import read
import welcome

# Main function
def main():
    welcome.welcome_user()

    while True:
        options.show_options()
        user_choice = int(input('Please enter a choice (1 - 5): '))

        if user_choice == 1:
            add.add_expense()
        elif user_choice == 2:
            read.show_expenses()
        elif user_choice == 3:
            update.update_expense()
        elif user_choice == 4:
            delete.delete_expense()
        elif user_choice == 5:
            print('Thank you for using the Expense Tracker app')
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()
