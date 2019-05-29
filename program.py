import datetime
import csv


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

csvLoc = "C:\Users\princ\OneDrive\Desktop\Savings\Savings.csv"

# object responsible for detecting time
now = datetime.datetime.now()

# variables represent the category, amount of money, date
spenton = raw_input("Enter what you spent money on: \n")
howmuch = "$" + raw_input("Enter how much money you spent: \n")
date = str(now.month) + "/" + str(now.day) + "/" + str(now.year) + "\n"

# array that contains the above information
sprdshtinput = [howmuch, spenton, date]

# prints each of the elements in the array for testing purposes
for x in sprdshtinput:
    print(x)


with open(csvLoc, "wb") as Savings:
    filewriter = csv.writer(Savings, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(sprdshtinput[1])
    filewriter.writerow(sprdshtinput[0])
    filewriter.writerow(sprdshtinput[2])