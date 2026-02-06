import sqlite3
import pytest
from faker import Faker
import allure

faker = Faker()

@allure.feature("Database Integration")
def test_user_registration_db_check(db_connection):
    user_name = faker.name()
    user_email = faker.email()
    cursor = db_connection.cursor()

    with allure.step(f"Insert {user_name} into DB"):
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user_name, user_email))
        db_connection.commit()

    with allure.step("Verify user presence in DB"):
        cursor.execute("SELECT name FROM users WHERE email=?", (user_email,))
        result = cursor.fetchone()

        assert result is not None, "User not found!"
        assert result[0] == user_name