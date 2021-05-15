import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username_selector = '#id_username'
password_selector = '#id_password'
login_selector = '[value="Log in"]'
item_selector = "//div[@class='panel-heading']//a"
add_button_selector = "#add_to_cart"

username = 'my_username'
password = 'very_good_password'

@pytest.fixture(scope='session')
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_add_item(chrome_driver):
    chrome_driver.get('http://127.0.0.1:8000/')

    item = chrome_driver.find_element(By.XPATH,
                                       item_selector)[0].text

    button = chrome_driver.find_element(By.CSS_SELECTOR, add_button_selector)[0]
    button.click()
    time.sleep(1)

    chrome_driver.switch_to.alert.accept()
    chrome_driver.get('http://127.0.0.1:8000/user_cart_page')

    selected = chrome_driver.find_element(By.XPATH,
                                           "//p[@class='text-left']//a")[0].text

    assert item == selected