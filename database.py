import sqlite3 

conn = sqlite3.connect("mydatabase.db")

print("Opened database successfully")

conn.execute("CREATE TABLE IF NOT EXISTS student (name TEXT, email TEXT)")

print("Table has been created")

conn.close()
