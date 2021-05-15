import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username_selector = '#id_username'
email_selector = '#id_email'
firstname_selector = '#id_first_name'
lastname_selector = '#id_last_name'
password_selector = '#id_password'
repeat_password_selector = '#id_repeat_password'
register_selector = '[value="Заристироваться"]'
old_password_selector = '#id_old_password'
new_password_selector = '#new_password'
reset_selector = '.btn-primary'


url = 'http://127.0.0.1:8000/accounts/password_reset/'
url_reset = 'http://127.0.0.1:8000/accounts/password_reset/done/'
url_signup = 'http://127.0.0.1:8000/accounts/signup/'
url_login = 'http://127.0.0.1:8000/accounts/login/'


username = "great_username"
not_existing_email = "not_existing_email@mail.ru"
name = "James"
lastname = "Bond"
password = "very_good_password"
user_email = "myemail@mail.ru"
old_password = "very_good_password"


@pytest.fixture(scope='session')
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_reset(chrome_driver):
    chrome_driver.get(url)

    email_element = chrome_driver.find_element(By.CSS_SELECTOR, email_selector)
    email_element.send_keys(user_email)

    reset_element = chrome_driver.find_element(By.CSS_SELECTOR, reset_selector)
    reset_element.click()
    time.sleep(2)

    assert chrome_driver.current_url == url_reset

    reset_element = chrome_driver.find_element(By.CSS_SELECTOR, reset_selector)
    reset_element.click()
    time.sleep(2)

    assert chrome_driver.current_url == url_login


def test_reset_with_wrong_email(chrome_driver):
    chrome_driver.get(url)

    email_element = chrome_driver.find_element(By.CSS_SELECTOR, email_selector)
    email_element.send_keys(not_existing_email)

    reset_element = chrome_driver.find_element(By.CSS_SELECTOR, reset_selector)
    reset_element.click()
    time.sleep(2)

    assert chrome_driver.current_url == url