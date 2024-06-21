from pages.login_page import LoginPage
from behave import *

login_page = LoginPage()

@when('login: I login with valid credentials')
def step_impl(context):
  login_page.fill_user_input('proms2023')
  login_page.fill_pass_input('Betuna22@')
  login_page.click_login_button()

@when('login: I login with user "{user}" and pasword "{pasword}"')
def step_impl(context, user, pasword):
  login_page.fill_user_input(user)
  login_page.fill_pass_input(pasword)
  login_page.click_login_button()

@then('login: I validate that error mesage is displayed')
def step_impl(context):
  login_page.validate_invalid_credentials_error()
