import sqlite3

def connect_to_db():
    c = sqlite3.connect('user_data.db')
    return c

def create_user_table(c):
    cursor = c.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')
    c.commit()

def add_user(c, username, password):
    cursor = c.cursor()
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password))
    c.commit()

