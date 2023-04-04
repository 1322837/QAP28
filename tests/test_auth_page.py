import pytest
from pages.auth_page import AuthPage
from settings import *

# Автотестов всего 10, т.к. не представляется возможным проверить работоспособность тестов на восстановление пароля и регистрацию


class TestsRostelekom:
    # проверка на соответствие внешнего вида страницы требованиям предоставленным в документе
    @pytest.mark.UI
    def test_find_requirements_on_login_page(self, web_browser):

        page = AuthPage(web_browser)
        # Система отображает форму «Авторизация», разделенную вертикально на два блока
        assert page.left_part.is_visible()
        assert page.right_part.is_visible()

        # Проверка правой части
        # Тут должен быть код, но элементы требуемые в документе на сайте отсутствуют

        # Проверка левой части
        # Таб выбора аутентификации по номеру, "Номер"
        assert page.btn_phone.is_visible()
        # Таб выбора аутентификации по логину и паролю, "Почта"
        assert page.btn_mail.is_visible()
        # Таб выбора аутентификации по почте и паролю, "Логин"
        assert page.btn_login.is_visible()
        # Таб выбора аутентификации по лицевому счету и паролю, “Лицевой счет”
        assert page.btn_account.is_visible()
        # Форма ввода "Номер" или "Логин" или "Почта" или “Лицевой счет”
        assert page.login.is_visible()
        # Форма ввода "Пароль"
        assert page.password.is_visible()

    # При вводе номера телефона/почты/логина/лицевого счета - таб выбора аутентификации меняется автоматически.
    @pytest.mark.UI
    def test_tabs_change_with_text(self, web_browser):
        page = AuthPage(web_browser)
        page.login.send_keys(valid_mail)
        page.password.click()
        assert page.btn_mail.get_attribute("CLASS") == 'rt-tab rt-tab--small rt-tab--active'
        page.refresh()
        page.login.send_keys(valid_phone)
        page.password.click()
        assert page.btn_phone.get_attribute("CLASS") == 'rt-tab rt-tab--small rt-tab--active'
        page.refresh()
        page.login.send_keys(valid_login)
        page.password.click()
        assert page.btn_login.get_attribute("CLASS") == 'rt-tab rt-tab--small rt-tab--active'
        page.refresh()
        page.login.send_keys(valid_account)
        page.password.click()
        assert page.btn_account.get_attribute("CLASS") == 'rt-tab rt-tab--small rt-tab--active'

    # Авторизация по номеру телефона, позитивная и негативная
    @pytest.mark.login
    @pytest.mark.positive
    def test_auth_with_phone_positive(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_phone.click()

        page.login.send_keys(valid_phone)

        page.password.send_keys(valid_password)

        page.btn.click()

        assert page.positive.wait_to_be_clickable()

    @pytest.mark.login
    @pytest.mark.negative
    def test_auth_with_phone_negative(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_phone.click()

        page.login.send_keys(valid_phone)

        page.password.send_keys(invalid_password)

        page.btn.click()

        assert page.negative.is_visible()

    # Авторизация по электронной почте, позитивная и негативная
    @pytest.mark.login
    @pytest.mark.positive
    def test_auth_with_mail_positive(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_mail.click()

        page.login.send_keys(valid_mail)

        page.password.send_keys(valid_password)

        page.btn.click()

        assert page.positive.wait_to_be_clickable()

    @pytest.mark.login
    @pytest.mark.negative
    def test_auth_with_mail_negative(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_mail.click()

        page.login.send_keys(valid_enmail)

        page.password.send_keys(invalid_password)

        page.btn.click()

        assert page.negative.is_visible()

    # Авторизация по логину, позитивная и негативная. Не работает т.к. у меня он отсутствует
    @pytest.mark.login
    @pytest.mark.positive
    def test_auth_with_login_positive(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_login.click()

        page.login.send_keys(valid_login)

        page.password.send_keys(valid_password)

        page.btn.click()

        assert page.positive.wait_to_be_clickable()

    @pytest.mark.login
    @pytest.mark.negative
    def test_auth_with_login_negative(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_login.click()

        page.login.send_keys(valid_login)

        page.password.send_keys(invalid_password)

        page.btn.click()

        assert page.negative.is_visible()

    # Авторизация по номеру ЛС, позитивная и негативная. Не работает т.к. у меня он отсутствует
    @pytest.mark.login
    @pytest.mark.positive
    def test_auth_with_account_positive(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_account.click()

        page.login.send_keys(valid_account)

        page.password.send_keys(valid_password)

        page.btn.click()

        assert page.positive.wait_to_be_clickable()

    @pytest.mark.login
    @pytest.mark.negative
    def test_auth_with_account_negative(self,web_browser):

        page = AuthPage(web_browser)

        # если есть капча тест автоматом проваливается, не разобрался как сделать нормальное распознавание картинки
        assert page.captcha.is_not_presented()

        page.btn_account.click()

        page.login.send_keys(valid_account)

        page.password.send_keys(invalid_password)

        page.btn.click()

        assert page.negative.is_visible()




