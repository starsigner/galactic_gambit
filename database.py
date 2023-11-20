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

def user_exists(c, username):
    cursor = c.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ?
    ''', (username,))
    return cursor.fetchone() is not None

def add_user(c, username, password):
    cursor = c.cursor()
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?)
    ''', (username, password))
    c.commit()

def clear_database(c):
    cursor = c.cursor()
    cursor.execute('''
        DELETE FROM users
    ''')
    c.commit()

    