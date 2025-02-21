from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import expected_conditions as EC
import random
import string
import time
import pytest


@pytest.fixture()
# делаем режимбез открытия окна браузера
def browser():
    options = Options()
    options.add_argument('--headless')
    chrome_browser = webdriver.Chrome(options=options)
    return chrome_browser


# Генерация случайного Email
def g_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.com"


# в этом тесте проверяем генерацию емайла и кнопку join us
def test_join_us(browser):
    browser.get("https://odds69.in/en")
    browser.implicitly_wait(5)
    join_us_button = browser.find_element(By.XPATH, './/*[@data-testid="joinUs"]')
    join_us_button.click()
    tab_email = browser.find_element(By.XPATH, './/*[@data-testid="Tab EMAIL"]')
    tab_email.click()
    email_text = browser.find_element(By.XPATH, './/*[@placeholder="Email"]')
    email_text.click()
    random_email = g_random_email()
    time.sleep(5)
    email_text.send_keys(random_email)
    time.sleep(5)
    assert join_us_button is not None, "Кнопка не найдена"
    assert join_us_button.text == "Join Us", f"Неверный текст на кнопке: {join_us_button.text}"


# в этом тесте проходим авторизацию и делаем проверку регистрации емайла
def test_join_us_9(browser):
    browser.get("https://odds69.in/en")
    browser.implicitly_wait(5)
    join_us_button = browser.find_element(By.XPATH, './/*[@data-testid="joinUs"]')
    join_us_button.click()
    tab_email = browser.find_element(By.XPATH, './/*[@data-testid="Tab EMAIL"]')
    tab_email.click()
    email_text = browser.find_element(By.XPATH, './/*[@placeholder="Email"]')
    email_text.click()
    random_email = g_random_email()
    email_text.send_keys(random_email)
    time.sleep(5)
    get_code = browser.find_element(By.XPATH, './/*[@data-testid="Button getCode active"]')
    time.sleep(3)
    get_code.click()
    browser.implicitly_wait(5)
    code_pass= browser.find_element(By.XPATH, './/*[@autocomplete="nope"]')
    code_pass.send_keys('55555')
    password_get = browser.find_element(By.XPATH, './/*[@placeholder="Password"]')
    password_get.send_keys('123456Qw')
    currency = browser.find_element(By.XPATH, './/*[@data-testid="Select CurrencySelection"]')
    currency.click()
    currency_inr = browser.find_element(By.XPATH, './/*[@data-testid="DropdownPart INR"]')
    currency_inr.click()
    get_join_us = browser.find_element(By.XPATH, './/*[@data-testid="Button doJoinUs"]')
    get_join_us.click()
    time.sleep(15)
    get_user_menu = browser.find_element(By.XPATH, './/*[@data-testid="UserMenuDropdown"]')
    get_user_menu.click()
    browser.implicitly_wait(10)
    get_user_menu = browser.find_element(By.XPATH, './/*[@data-testid="AccountPageLink"]')
    get_user_menu.click()
    browser.implicitly_wait(5)
    email_element = browser.find_element(By.XPATH, './/*[@data-testid="emailContactSection"]//*[@data-testid="value"]')
    expected_email = random_email
    actual_email = email_element.text

    assert actual_email == expected_email, f"Expected '{expected_email}', but got '{actual_email}'"
