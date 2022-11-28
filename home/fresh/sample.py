import sqlite3
import hashlib

conn = sqlite3.connect('userdata.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(225) NOT NULL,
    password VARCHAR(225) NOT NULL
)
""")
