from main import Database

def test_save_user_integration(db_connection):
    db = Database(db_connection)
    db.save_user("ricardo", "ricardo@test.com")

    cursor = db_connection.cursor()
    cursor.execute("SELECT username FROM users WHERE username = 'ricardo'")
    result = cursor.fetchone()

    assert result is not None
    assert result[0] == "ricardo"

def test_user_persistence(db_connection):
    db = Database(db_connection)
    user_test = "ricardo"
    email_test = "ricardo@test.com"
    db.save_user(user_test, email_test)

    user_db = db.get_user_by_username(user_test)

    assert user_db is not None
    assert user_db[1] == user_test
    assert user_db[2] == email_test