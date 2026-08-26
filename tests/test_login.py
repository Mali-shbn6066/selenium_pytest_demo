from pages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in login_page.get_message()


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login("wrong_user", "wrong_password")

    assert "Your username is invalid!" in login_page.get_message()
