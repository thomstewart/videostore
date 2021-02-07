#!/usr/bin/python3
import sqlite3
import csv

connection = sqlite3.connect('videostore.db')
cursor = connection.cursor()
cursor.execute("DROP TABLE inventory")
cursor.execute("CREATE TABLE inventory (item_id integer PRIMARY KEY, item_barcode text,item_title text,item_subtitle text,release_date text)")
inventory_id = 0

with open('inventory.csv') as inv:
    csv_reader = csv.reader(inv, delimiter=',')
    line_count = 1
    for row in csv_reader:
        cursor.execute("INSERT INTO inventory VALUES (?,?,?,?,?)", row)
        connection.commit()
        inventory_id = int(row[0])
        
inp = None
while inp != "q":
    print("display) Display inventory")
    print("  add  ) Add to inventory")
    print(" update) Update item title")
    print(" delete) Delete from inventory")
    print("  man  ) manually input statement")
    print("   q   ) Quit")
    inp = input("$ ")
    print()
    if inp == "display":
        # Display inventory
        cursor.execute("SELECT * FROM inventory")
        print("{:<18}  {:<45}  {:<40}  {:<12}".format("Barcode", "Title", "Subtitle", "Release Date"))
        for record in cursor.fetchall():
            print("{:<18}  {:<45}  {:<40}  {:<12}".format(record[1], record[2], record[3], record[4]))
    elif inp == "add":
        # Add New movie
        barcode = input("Barcode: ")
        title = input("Title: ")
        sub = input("Subtitle: ")
        release_date = input("Release Date: ")
        inventory_id += 1
        values = (str(inventory_id), str(barcode), title, str(sub), str(release_date))
        cursor.execute("INSERT INTO inventory VALUES (?,?,?,?,?)", values)
        connection.commit()
    elif inp == "update":
        # Update movie inf
        barcode = input("Barcode: ")
        title = input("Title: ")
        subtitle = input("Subtitle: ")
        values1 = (title, barcode)
        values2 = (subtitle, barcode)
        cursor.execute("UPDATE inventory SET item_title = ? WHERE item_barcode = ?", values1)
        cursor.execute("UPDATE inventory SET item_subtitle = ? WHERE item_barcode = ?", values2)
        connection.commit()
    elif inp == "delete":
        # Delete item
        title = input("Title: ")
        values = (title, )
        cursor.execute("DELETE FROM inventory WHERE item_title = ?", values)
        connection.commit()
    elif inp == "man":
        stmt = input("query/statement: ")
        cursor.execute(stmt)
        connection.commit()
        for record in cursor.fetchall():
            print(record[0])
    print()
# Close the database connection before exiting
connection.close()
