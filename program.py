# ==================================================================================
# Savings Program
# Benjamin Princen
# ==================================================================================
# Purpose: Allow the user to easily see how much they spent
# this month, and how much money they have left to spend
# based on how much they want to save.
# ==================================================================================
# Pseudocode:
# Enter how many categories
# Enter first category
# Enter item under first category
# Enter date
# Repeat until number of loops matches number of categories
# Store information in a 2D array
# Access .csv file in directed location
# If the .csv file already has information, then append new information
# Save the .csv file
# ==================================================================================

# ==================================================================================
# Imports
# ==================================================================================
import datetime
import os
import constants

# ==================================================================================
# Constants
# ==================================================================================
CSV_PATH = 'information/money.csv'

# ==================================================================================
# Function Definitions
# ==================================================================================



# ==================================================================================
# Main
# ==================================================================================
def main():
    # object responsible for detecting time
    now = datetime.datetime.now()

    create_file = False
    # variables represent the category, amount of money, date
    cat_spent = input("Enter what you spent money on: \n") # cat is an abbreviation for category
    amount_spent = "$" + input("Enter how much money you spent: \n")
    date_spent = str(now.month) + "/" + str(now.day) + "/" + str(now.year)

    if(not os.path.exists(CSV_PATH)):
        create_file = True

    csv_file = open(CSV_PATH, 'w+') if create_file else open(CSV_PATH, 'a+')
    if csv_file.mode == 'w+':
        print("CATEGORY,AMOUNT SPENT,DATE SPENT", file = csv_file)
    print(str(cat_spent) + ',' + str(amount_spent) + ',' + date_spent, file = csv_file)
    csv_file.close()

if __name__ == '__main__':
    main()