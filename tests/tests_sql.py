import pytest
import sqlite3


def test_sql_schema():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchone()
    assert result == (1, 'Alice', 30)
    conn.close()
