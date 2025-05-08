import sqlite3
import os

# Path to the database file
db_path = 'instance/employees.db'

# Check if the database file exists
if not os.path.exists(db_path):
    print(f"Database file {db_path} not found.")
    exit(1)

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Check if update_request table exists
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='update_request'")
if cursor.fetchone():
    # Check if admin_notes column exists in update_request table
    cursor.execute("PRAGMA table_info(update_request)")
    columns = cursor.fetchall()
    column_names = [column[1] for column in columns]

    if 'admin_notes' not in column_names:
        print("Adding admin_notes column to update_request table...")
        cursor.execute("ALTER TABLE update_request ADD COLUMN admin_notes TEXT")
        conn.commit()
        print("admin_notes column added successfully.")
    else:
        print("admin_notes column already exists in update_request table.")
else:
    print("update_request table does not exist. It will be created when the application runs.")

# Close the connection
conn.close()
print("Database migration completed.")