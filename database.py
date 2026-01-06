import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    role TEXT,
    status TEXT,
    last_login TEXT
)
""")

conn.commit()
conn.close()
