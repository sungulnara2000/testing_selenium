import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = 'http://127.0.0.1:8000/accounts/signup/'
url_activated = 'http://127.0.0.1:8000/accounts/activate_account/'

username_selector = '#id_username'
email_selector = '#id_email'
first_name_selector = '#id_first_name'
lastname_selector = '#id_last_name'
password_selector = '#id_password'
repeat_password_selector = '#id_repeat_password'
register_selector = '[value="Заристироваться"]'

used_username = "gulnara__sun"
username = "great_username"
email = "email@mail.ru"
name = "name"
password = "very_good_password"

@pytest.fixture(scope='session')
def chrome_driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()


def test_empty_input(chrome_driver):
    register_element = chrome_driver.find_element(By.CSS_SELECTOR, register_selector)
    register_element.click()
    time.sleep(2)

    assert chrome_driver.current_url == url

def test_register(chrome_driver):
    chrome_driver.get(url)
    
    username_element = chrome_driver.find_element(By.CSS_SELECTOR, username_selector)
    username_element.send_keys(used_username)

    name_element = chrome_driver.find_element(By.CSS_SELECTOR, first_name_selector)
    name_element.send_keys(name)
    
    lastname_element = chrome_driver.find_element(By.CSS_SELECTOR, lastname_selector)
    lastname_element.send_keys(name)

    email_element = chrome_driver.find_element(By.CSS_SELECTOR, email_selector)
    email_element.send_keys(email)

    pass_element = chrome_driver.find_element(By.CSS_SELECTOR, password_selector)
    pass_element.send_keys(password)

    rep_pass_element = chrome_driver.find_element(By.CSS_SELECTOR, repeat_password_selector)
    rep_pass_element.send_keys(password)

    register_element = chrome_driver.find_element(By.CSS_SELECTOR, register_selector)
    register_element.click()
    time.sleep(2)

    chrome_driver.get(url_activated)
    assert chrome_driver.current_url == url_activated


def test_used_username(chrome_driver):
    chrome_driver.get(url)

    username_element = chrome_driver.find_element(By.CSS_SELECTOR, username_selector)
    username_element.send_keys(used_username)

    name_element = chrome_driver.find_element(By.CSS_SELECTOR, first_name_selector)
    name_element.send_keys(name)

    lastname_element = chrome_driver.find_element(By.CSS_SELECTOR, lastname_selector)
    lastname_element.send_keys(name)

    email_element = chrome_driver.find_element(By.CSS_SELECTOR, email_selector)
    email_element.send_keys(email)

    pass_element = chrome_driver.find_element(By.CSS_SELECTOR, password_selector)
    pass_element.send_keys(password)

    rep_pass_element = chrome_driver.find_element(By.CSS_SELECTOR, repeat_password_selector)
    rep_pass_element.send_keys(password)

    register_element = chrome_driver.find_element(By.CSS_SELECTOR, register_selector)
    register_element.click()
    time.sleep(2)

    assert chrome_driver.current_url == url

def test_wrong_repeat_password(chrome_driver):
    chrome_driver.get(url)

    username_element = chrome_driver.find_element(By.CSS_SELECTOR, username_selector)
    username_element.send_keys(username)

    name_element = chrome_driver.find_element(By.CSS_SELECTOR, first_name_selector)
    name_element.send_keys(name)

    lastname_element = chrome_driver.find_element(By.CSS_SELECTOR, lastname_selector)
    lastname_element.send_keys(name)

    email_element = chrome_driver.find_element(By.CSS_SELECTOR, email_selector)
    email_element.send_keys(email)

    pass_element = chrome_driver.find_element(By.CSS_SELECTOR, password_selector)
    pass_element.send_keys(password)

    rep_pass_element = chrome_driver.find_element(By.CSS_SELECTOR, repeat_password_selector)
    rep_pass_element.send_keys("wrong_password" + password)

    register_element = chrome_driver.find_element(By.CSS_SELECTOR, register_selector)
    register_element.click()
    time.sleep(2)
    assert chrome_driver.current_url == url