'''
Program Name: Part2_Ex2.py
Prgram Description: This program reads data from the practice database. 
Programmer: Ray, Stephen
Date: 04/10/2022
Course: CSC233-1L1
'''

import sqlite3

# Open the database and cursor
conn = sqlite3.connect('Practice.db')
cur = conn.cursor()


print("Orders shipped by Federal Shipping:")
# Get data of the Order id, date, and shipper company name from the Orders and Shippers tables
cur.execute('Select OrderID, OrderDate, CompanyName from Orders ord JOIN Shippers shi ON ord.ShipVia = shi.ShipperID Where ShipperID = 3')

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