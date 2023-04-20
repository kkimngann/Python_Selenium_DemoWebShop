# Scenarios
import allure
from pytest_bdd import when, then, parsers
from pytest_bdd.scenario import scenarios

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.utils import *

scenarios('../features/login.feature')


@when('User go to login screen')
def step_def(driver):
    homepage: HomePage = HomePage(driver)
    homepage.select_login()


@when(parsers.re(r"User input email (?P<email>.+@.+[a-z]) and password (?P<password>.+) and submit"))
def step_def(driver, email, password):
    login_page: LoginPage = LoginPage(driver)
    login_page.login_flow(email, password)


@then(parsers.re(r'Error message show correctly (?P<message>.+)'))
def step_def(driver, message):
    login_page: LoginPage = LoginPage(driver)
    actual_message = login_page.login_form.get_error_message()
    expected_message = message
    assert remove_string_break(actual_message) == remove_string_break(expected_message)


@then(parsers.re(r'Show correct user email (?P<email>.+@.+[a-z]) after login'))
def step_def(driver, email):
    homepage: HomePage = HomePage(driver)
    actual_user = homepage.top_menu.get_current_login_user_email()
    expected_user = email
    assert actual_user == expected_user


@then('Show button log out correctly')
def step_def(driver):
    homepage: HomePage = HomePage(driver)
    assert homepage.top_menu.check_button_logout_exist() is True
