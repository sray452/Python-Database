'''
Program Name: Part2_Ex7.py
Prgram Description: This program reads data from the practice database. 
Programmer: Ray, Stephen
Date: 04/10/2022
Course: CSC233-1L1
'''

import sqlite3

# Open the database and cursor
conn = sqlite3.connect('Practice.db')
cur = conn.cursor()


print("Customers sorted alphabetically by region:")
# Get data of the CustomerID, CompanyName, and Region from the Customers table
cur.execute('Select CustomerID, CompanyName, Region from Customers Where Region IS NOT "" Order by CustomerID')

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