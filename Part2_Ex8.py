'''
Program Name: Part2_Ex8.py
Prgram Description: This program reads data from the practice database. 
Programmer: Ray, Stephen
Date: 04/10/2022
Course: CSC233-1L1
'''

import sqlite3

# Open the database and cursor
conn = sqlite3.connect('Practice.db')
cur = conn.cursor()


print("Three highest average freight charges by country:")
# Get data of the ShipCountry and the average freight from the Orders table
cur.execute('Select ShipCountry, AVG(Freight) AS AverageFreight from Orders Group By ShipCountry Order By AverageFreight DESC LIMIT 3')

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