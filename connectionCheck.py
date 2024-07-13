import sqlite3

def check_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        conn.execute("SELECT 1")
        conn.close()
        return "Connection is open and closed successfully."
    except sqlite3.Error as e:
        return f"An error occurred: {e}"

db_path = 'shift5.db'  # path to SQLite db file
print(check_connection(db_path))
