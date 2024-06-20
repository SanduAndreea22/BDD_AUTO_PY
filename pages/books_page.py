from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class BooksPage(BasePage):
    # Selectors
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_OF_BOOK = "//xpath/to/book/elements"

    # actions
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    # validations
    def validate_correct_url(self):
        sleep(5)
        expected = 'https://demoqa.com/books'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'url incorrect')
