from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


with open('auth.json', 'r') as file:
    login, password = json.load(file).values()


def test_auth(login, password):
    driver = webdriver.Edge()
    driver.get('https://passport.yandex.ru/auth')
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//input[@data-t="field:input-login"]') is not None, 'Окно логина не найдено'
    login_win = driver.find_element(By.XPATH, '//input[@data-t="field:input-login"]')
    login_win.send_keys(login)
    assert driver.find_element(By.XPATH, '//button[@data-t="button:action:passp:sign-in"]').click() is None, 'Кнопка ввода логина не найдена'
    time.sleep(3)
    assert driver.find_element(By.XPATH, '//input[@data-t="field:input-passwd"]') is not None, 'Окно пароля не найдено'
    password_win = driver.find_element(By.XPATH, '//input[@data-t="field:input-passwd"]')
    password_win.send_keys(password)
    assert driver.find_element(By.XPATH, '//button[@data-t="button:action:passp:sign-in"]').click() is None, 'Кнопка ввода пароля не найдена'
    time.sleep(60)
    driver.close()
