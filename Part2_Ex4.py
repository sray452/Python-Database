'''
Program Name: Part2_Ex4.py
Prgram Description: This program reads data from the practice database. 
Programmer: Ray, Stephen
Date: 04/10/2022
Course: CSC233-1L1
'''

import sqlite3

# Open the database and cursor
conn = sqlite3.connect('Practice.db')
cur = conn.cursor()


print("Total number of customers per Country and City:")
# Get data of the Country, City, and CustomerID count from the Customers table
cur.execute('Select Country, City, COUNT(CustomerID) AS TotalCustomer from Customers GROUP BY Country, City Order by TotalCustomer DESC')

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