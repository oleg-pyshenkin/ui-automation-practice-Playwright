import sqlite3
import pytest
from faker import Faker
import allure

faker = Faker()

@allure.feature("Database Integration")
def test_user_registration_db_checl():
    user_name = faker.name()
    user_email = faker.email()

    with allure.step(f"Generate fake user: {user_name}"):
        print(f"Generated User: {user_name}, Email: {user_email}")

    connection = sqlite3.connect("test_automation.db")
    cursor = connection.cursor()

    with allure.step("Create users table if not exists"):
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY, name TEXT, email TEXT)
        ''')

    with allure.step("Insert user into Database"):
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user_name, user_email))
        connection.commit()

    with allure.step("Verify user in Database"):
        cursor.execute("SELECT name FROM users WHERE email=?", (user_email,))
        result = cursor.fetchone()

        assert result is not None, "User was not found in DB"
        assert result[0] == user_name
        print(f"Database verification successful for: {result[0]}")

    connection.close()