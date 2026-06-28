import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS books(
            book_id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            quantity INTEGER,
            available INTEGER
        )
        """)

        self.conn.commit()

    def execute(self, query, values=()):
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetchall(self, query, values=()):
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()