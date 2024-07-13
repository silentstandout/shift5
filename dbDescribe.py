import pandas as pd
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('shift5.db')

# List of table names
tables = ['acas', 'hirestraces', 'readsb', 'traces']

# Loop through each table and run describe
for table in tables:
    query = f'SELECT * FROM {table}'
    df = pd.read_sql_query(query, conn)
    description = df.describe()
    print(f'Descriptive statistics for table {table}:\n', description, '\n')

# Close the database connection
conn.close()
