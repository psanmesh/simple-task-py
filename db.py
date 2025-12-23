import sqlite3
import os
from utils import get_app_dir

DB_PATH = os.path.join(get_app_dir(), "poc_app.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            value TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def insert_item(value):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (value) VALUES (?)", (value,))
    conn.commit()
    conn.close()

def fetch_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM items ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return [r[0] for r in rows]
