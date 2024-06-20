# importam selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# initializam chrome
chrome = webdriver.Chrome()

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login')

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(3)

# completam username in f de atribut valoare
chrome.find_element(By.XPATH, '//input[@id="username"]').send_keys('tomsmith')
sleep(3)

# completam parola in f de atribut valoare
chrome.find_element(By.XPATH, '//input[@id="password"]').send_keys('SuperSecretPassword!')
sleep(3)

# dam click pe elemenal login in functie de textul elementului
chrome.find_element(By.XPATH, '//i[text()=" Login"]').click()
sleep(3)

# dam click pe elemenal selenium in functie de textul elementului
chrome.find_element(By.XPATH, '//*[text()="Elemental Selenium"]').click()
sleep(3)

# verificam ca am ajuns pe pagina corecta
expected = 'https://the-internet.herokuapp.com/secure'
actual = chrome.current_url
assert  expected == actual, 'incorect url'

# inchidem chrome
chrome.quit()

# daca a trecut testul, printam in consola un mesaj de succes
print('SUCCESS - TEST PASSED')