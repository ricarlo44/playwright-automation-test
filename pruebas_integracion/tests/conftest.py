import pytest
import sqlite3

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')  # Create an in-memory database
    conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT)")
    yield conn
    conn.close()