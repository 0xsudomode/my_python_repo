import sqlite3

# Connect to a database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data into the table
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))
conn.commit()

# Fetch data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print(rows)

# Close the connection
conn.close()
