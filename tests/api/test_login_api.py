import requests
import pytest
import allure

@allure.feature("API Login")
def test_api_login_status_code():
    url = "https://the-internet.herokuapp.com/authenticate"
    payload = {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    }

    with allure.step("Send POST request with invalid password"):
        response = requests.post(url, data=payload)

    with allure.step("Verify status Code"):
        assert "secure" in response.url
        assert response.status_code == 200
        print(f"Recievied status code: {response.status_code}")



def test_api_login_wrong_password():
    url = "https://the-internet.herokuapp.com/authenticate"
    payload = {
        "username": "tomsmith",
        "password": "WrongPassword!"
    }

    with allure.step("Send POST request with invalid password"):
        response = requests.post(url, data=payload)

    with allure.step("Verify status Code"):
        assert "login" in response.url
        assert "Your password is invalid!" in response.text