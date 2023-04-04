from pages.base import WebPage
from pages.elements import WebElement

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://b2c.passport.rt.ru'
        super().__init__(web_driver, url)

    login = WebElement(id='username')

    password = WebElement(id='password')

    btn = WebElement(id='kc-login')

    btn_phone = WebElement(id='t-btn-tab-phone')

    btn_mail = WebElement(id='t-btn-tab-mail')

    btn_login = WebElement(id='t-btn-tab-login')

    btn_account = WebElement(id='t-btn-tab-ls')

    slogan = WebElement(id='page-left')

    left_part = WebElement(id='page-left')

    right_part = WebElement(id='page-right')

    captcha = WebElement(id='captcha')

    # Кнопка логаута
    positive = WebElement(id='logout-btn')

    # Надпись о неверном логине/пароле/етс
    negative = WebElement(id='form-error-message')
