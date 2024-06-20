from pages.books_page import BooksPage
from behave import *

books_page = BooksPage()

@when('books: I click login button')
def step_impl(context):
    books_page.click_login_button()

@then('books: I should land om books page')
def step_impl(context):
    books_page.validate_correct_url()
