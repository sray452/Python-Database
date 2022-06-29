'''
Program Name: Ex5.py
Prgram Description: This program reads data from the practice database. 
Programmer: Ray, Stephen
Date: 04/03/2022
Course: CSC233-1L1
'''

import sqlite3

# Open the database and cursor
conn = sqlite3.connect('Practice.db')
cur = conn.cursor()

#Example 1: Display the orders placed by employee number 5
print("Employee 5 orders:")
# Get data of the CategoryName and Description columns of the Categories table
cur.execute('Select OrderId, OrderDate from Orders Where EmployeeID = 5')

#Print the column names
for col in cur.description: # cur.description contains the column names in the
                            # first element of each tuple in a list of tuples
    print(col[0], end=" ")

print()

# Print each row of data
for row in cur:
    print(row)

# Close the cursor and database
cur.close()
conn.close()