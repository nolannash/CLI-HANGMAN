import sqlite3

def create_tables():
    CONN = sqlite3.connect('.database.db')
    CURSOR = CONN.cursor()
    
#create table
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS players(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            games
        )
        ''')