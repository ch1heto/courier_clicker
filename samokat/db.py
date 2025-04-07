import sqlite3

def init_db():
    with sqlite3.connect("courier.db") as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                money INTEGER DEFAULT 0,
                speed INTEGER DEFAULT 1,
                assistants INTEGER DEFAULT 0,
                assistant_cost INTEGER DEFAULT 10
            )
        ''')

def get_user(user_id):
    with sqlite3.connect("courier.db") as conn:
        cursor = conn.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
        return cursor.fetchone()

def create_user(user_id):
    with sqlite3.connect("courier.db") as conn:
        conn.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))

def update_user(user_id, money, speed, assistants, assistant_cost):
    with sqlite3.connect("courier.db") as conn:
        conn.execute('''
            UPDATE users
            SET money = ?, speed = ?, assistants = ?, assistant_cost = ?
            WHERE user_id = ?
        ''', (money, speed, assistants, assistant_cost, user_id))
