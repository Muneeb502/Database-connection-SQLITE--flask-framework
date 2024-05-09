import sqlite3 

conn = sqlite3.Connection("mydatabase.db")

print("opend database")

conn.execute("CREATE TABLE student (name TEXT , email TEXT )")


print("table has been created")

conn.close()
