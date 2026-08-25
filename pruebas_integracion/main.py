class Database:
    def __init__(self, connection):
        self.connection = connection

    def save_user(self, username, email):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
        self.connection.commit()

    def get_user_by_username(self, username):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        return cursor.fetchone()
