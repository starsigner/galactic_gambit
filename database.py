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
            password TEXT,
            astrobucks INT
        )
    ''')
    c.commit()

def user_exists(c, username):
    cursor = c.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ?
    ''', (username,))
    return cursor.fetchone() is not None

def add_user(c, username, password, astrobucks):
    cursor = c.cursor()
    cursor.execute('''
        INSERT INTO users (username, password, astrobucks) VALUES (?, ?, ?)
    ''', (username, password, astrobucks))
    c.commit()

def check_credentials(c, username, password):
    cursor = c.cursor()
    cursor.execute('''
        SELECT * FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    return cursor.fetchone() is not None

def update_user_astrobucks(c, username, new_astrobucks):
    cursor = c.cursor()
    cursor.execute('''
        UPDATE users SET astrobucks = ? WHERE username = ?
    ''', (new_astrobucks, username))
    c.commit()

def get_user_astrobucks(c, username):
    cursor = c.cursor()
    cursor.execute('''
        SELECT astrobucks FROM users WHERE username = ?
    ''', (username,))
    result = cursor.fetchone()
    return result[0] if result is not None else None

def clear_database(c):
    cursor = c.cursor()
    cursor.execute('''
        DELETE FROM users
    ''')
    c.commit()

