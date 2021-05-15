import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url_start = 'http://127.0.0.1:8000/'
url_cart = 'http://127.0.0.1:8000/user_cart_page'
url_history = 'http://127.0.0.1:8000/history_orders'

username_selector = '#id_username'
password_selector = '#id_password'
login_selector = '[value="Log in"]'

username = 'gulnara__sun'
password = 'very_good_password'


@pytest.fixture(scope='session')
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_access_after_login(chrome_driver):
    chrome_driver.get('http://127.0.0.1:8000/admin')

    username_element = chrome_driver.find_element(By.CSS_SELECTOR, username_selector)
    username_element.send_keys(username)

    pass_element = chrome_driver.find_element(By.CSS_SELECTOR, password_selector)
    pass_element.send_keys(password)

    login_element = chrome_driver.find_element(By.CSS_SELECTOR, login_selector)
    login_element.click()
    time.sleep(2)

    chrome_driver.get('http://127.0.0.1:8000/accounts/signup/')
    time.sleep(2)
    assert chrome_driver.current_url == url_start

    chrome_driver.get('http://127.0.0.1:8000/accounts/login/')
    time.sleep(2)
    assert chrome_driver.current_url == url_start

    chrome_driver.get(url_history)
    time.sleep(2)
    assert chrome_driver.current_url == url_history

    chrome_driver.get(url_cart)
    time.sleep(2)
    assert chrome_driver.current_url == url_cart


def test_access_without_login(chrome_driver):
    chrome_driver.get(url_cart)
    time.sleep(2)
    assert chrome_driver.current_url == url_start

    chrome_driver.get(url_history)
    time.sleep(2)
    assert chrome_driver.current_url == url_start


