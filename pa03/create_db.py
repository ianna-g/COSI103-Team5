import sqlite3

# Connect to database
conn = sqlite3.connect('tracker.db')

# Create a cursor

c = conn.cursor()

# Create a table
# DATATYPES: NULL, INTEGER, REAL, TEXT, BLOB
c.execute("""CREATE TABLE transactions (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          amount REAL,
          category TEXT,
          date TEXT,
          description TEXT
    )""")

# Commit command
conn.commit()

# Close the connection
conn.close()