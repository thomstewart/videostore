#!/usr/bin/python3

#import necessary libraries
import sqlite3
import csv

#create database connection and cursor
connection = sqlite3.connect('videostore.db')
cursor = connection.cursor()

#drop any existing inventory table to prevent errors
cursor.execute("DROP TABLE inventory")

#create new inventory table
cursor.execute("CREATE TABLE inventory (item_id integer PRIMARY KEY, item_barcode text,item_title text,item_subtitle text,release_date text)")

#create inventory id sequence to ensure there are no duplicates in the primary key
inventory_id_s = 0

#read the csv file into the database
with open('inventory.csv') as inv:
    csv_reader = csv.reader(inv, delimiter=',')
    line_count = 1
    for row in csv_reader:
        cursor.execute("INSERT INTO inventory VALUES (?,?,?,?,?)", row)
        connection.commit()
        inventory_id_s = int(row[0])
        
inp = None

#print out the menu
while inp != "q":
    print("display) Display inventory")
    print("  add  ) Add to inventory")
    print(" update) Update item title")
    print(" delete) Delete from inventory")
    print("  man  ) manually input statement")
    print("   q   ) Quit")
    #get user choice
    inp = input("$ ")
    print()

    if inp == "display":
        # Display inventory
        cursor.execute("SELECT * FROM inventory")
        print("{:<18}  {:<45}  {:<40}  {:<12}".format("Barcode", "Title", "Subtitle", "Release Date"))
        #format the output as it is displayed
        for record in cursor.fetchall():
            print("{:<18}  {:<45}  {:<40}  {:<12}".format(record[1], record[2], record[3], record[4]))
    
    elif inp == "add":
        # Add New movie
        barcode = input("Barcode: ")
        title = input("Title: ")
        sub = input("Subtitle: ")
        release_date = input("Release Date: ")
        inventory_id_s += 1
        #set values for update statement
        values = (str(inventory_id), str(barcode), title, str(sub), str(release_date))
        #insert new row
        cursor.execute("INSERT INTO inventory VALUES (?,?,?,?,?)", values)
        #save changes
        connection.commit()
    
    elif inp == "update":
        # Update movie info
        barcode = input("Barcode: ")
        title = input("Title: ")
        subtitle = input("Subtitle: ")

        #set values for update statement
        values1 = (title, barcode)
        values2 = (subtitle, barcode)
        #update the row
        cursor.execute("UPDATE inventory SET item_title = ? WHERE item_barcode = ?", values1)
        cursor.execute("UPDATE inventory SET item_subtitle = ? WHERE item_barcode = ?", values2)
        #save changes
        connection.commit()

    elif inp == "delete":
        # Delete item
        title = input("Title: ")
        #set values for update statement
        values = (title, )
        #delete title from inventory
        cursor.execute("DELETE FROM inventory WHERE item_title = ?", values)
        #save changes
        connection.commit()
    
    elif inp == "man":
        stmt = input("query/statement: ")
        cursor.execute(stmt)
        connection.commit()
        #display results of input
        for record in cursor.fetchall():
            print(record[0])
    print()

# Close the database connection before exiting
connection.close()
