from src.pages.tele2.auth_page import AuthPage
from common_imports import *

TEST_USER = user_for_test()['USER_WITH_WRONG_AUTH_DATA']


@allure.id("52")
@allure.title("Авторизация с неверным mail аддресом")
@allure.label("suite", "Функционал авторизации")
@allure.feature("Авторизация")
def test_auth_wrong_mail_and_correct_password(driver_fixture):
    pass


@allure.title("Авторизация с неверным номером телефона")
@allure.label("suite", "Функционал авторизации")
@allure.feature("Авторизация")
def test_auth_wrong_phone(driver_fixture):
    auth_page = AuthPage(driver_fixture)
    with allure.step('Запустить приложение Теле2 Казахстан'):
        pass
    with allure.step('В появившемся окне выбрать вход по номеру (по умолчанию)'):
        auth_page.click_login_with_phone()

    with allure.step('Ввести некорректный телефонный номер'):
        auth_page.input_phone(TEST_USER['INCORRECT_NUMBER'])

    with allure.step('Нажать на кнопку "Продолжить"'):
        auth_page.resume_button_click()

    with allure.step('Ввести пароль'):
        auth_page.input_pass(TEST_USER['CORRECT_PASSWORD'])

    with allure.step('Нажать на кнопку "Продолжить"'):
        auth_page.login_button_click()

    with allure.step('Появляется ошибка о том что, номер либо пароль неверный'):
        auth_page.check_push_wrong_password_or_login()


@allure.title("Авторизация с валидным номером и неверным паролем")
@allure.label("suite", "Функционал авторизации")
@allure.feature("Авторизация")
def test_auth_wrong_password(driver_fixture):
    auth_page = AuthPage(driver_fixture)
    with allure.step('Запустить приложение Теле2 Казахстан'):
        pass
    with allure.step('В появившемся окне выбрать вход по номеру (по умолчанию)'):
        auth_page.click_login_with_phone()

    with allure.step('Ввести корректный телефонный номер'):
        auth_page.input_phone(TEST_USER['CORRECT_NUMBER'])

    with allure.step('Нажать на кнопку "Продолжить"'):
        auth_page.resume_button_click()

    with allure.step('Ввести некорректный пароль'):
        auth_page.input_pass(TEST_USER['INCORRECT_PASSWORD'])

    with allure.step('Нажать на кнопку "Продолжить"'):
        auth_page.login_button_click()

    with allure.step('Появляется ошибка о том что, номер либо пароль неверный'):
        auth_page.check_push_wrong_password_or_login()
