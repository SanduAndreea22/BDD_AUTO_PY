from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class HomePage(BasePage):
    # Selectori
    BOOK_STORE_APPLICATION_CARD = '//h5[text()="Book Store Application"]'

    # Acțiuni
    def navigate_to_home_page(self):
        self.driver.get('https://demoqa.com/')

    def click_book_store_application_card(self):
        self.wait_for_elem(self.BOOK_STORE_APPLICATION_CARD)
        element = self.driver.find_element(By.XPATH, self.BOOK_STORE_APPLICATION_CARD)

        # Derulează până la element
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Așteaptă ca elementul să fie clicabil
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.BOOK_STORE_APPLICATION_CARD)))

        element.click()





