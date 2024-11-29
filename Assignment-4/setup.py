import sqlite3
from pymongo import MongoClient

def setup_sqlite():
    conn = sqlite3.connect("assignment4.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    """)
    cursor.execute("""
    INSERT OR IGNORE INTO users (id, name, email)
    VALUES
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob', 'bob@example.com')
    """)
    conn.commit()
    conn.close()
    print("Sqlite3 setup complete")

def setup_mongodb():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["assignment4"]
    users = db["users"]
    users.insert_many([
        {"name": "Charlie", "email": "charlie@example.com"},
        {"name": "Dave", "email": "dave@example.com"}
    ])
    print("MongoDB setup complete")

if __name__ == "__main__":
    setup_sqlite()
    setup_mongodb()
