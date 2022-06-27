from src.pages.tele2.auth_page import AuthPage, SetPin
from src.pages.tele2.main_page import MainPage
import allure
from common_imports import *

TEST_USER = user_for_test()['USER_WITH_CORRECT_AUTH_DATA']


class TestAuthPositive:

    @allure.title("Авторизация с номером телефона (без использования Touch ID)")
    @allure.feature("Авторизация")
    def test_auth_phone_without_touch_id(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        pin = SetPin(driver_fixture)
        main = MainPage(driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В появившемся окне выбрать вход по номеру (по умолчанию)'):
            auth.click_login_with_phone()
        with allure.step('Ввести телефонный номер'):
            auth.input_phone(TEST_USER['NUMBER'])
        with allure.step('Нажать на кнопку "Продолжить"'):
            auth.resume_button_click()
        with allure.step('Ввести пароль'):
            auth.input_pass(TEST_USER['PASSWORD'])
        with allure.step('Нажать на кнопку "Продолжить"'):
            auth.login_button_click()
        with allure.step('Установить ПИН-код для входа в приложение'):
            pin.pin_desk_located()
            pin.close_pin_click()

        with allure.step('Открыта главная страница, в верхней части страницы '
                         'указан ваш телефонный номер и отображается баланс'):
            main.check_user_authored(TEST_USER['NUMBER'])

    @allure.title("Авторизация с e-mail (без использования Touch ID)")
    @allure.feature("Авторизация")
    def test_auth_mail_without_touch_id(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        pin = SetPin(driver_fixture)
        main = MainPage(driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В появившемся окне выбрать вход по e-mail'):
            auth.click_login_with_mail()
        with allure.step('Ввести e-mail'):
            auth.input_mail(TEST_USER['EMAIL'])
        with allure.step('Нажать на кнопку "Продолжить"'):
            auth.resume_button_click_mail()
        with allure.step('Ввести пароль'):
            auth.input_pass(TEST_USER['PASSWORD'])
        with allure.step('Нажать на кнопку "Продолжить"'):
            auth.login_button_click()
        with allure.step('Установить ПИН-код для входа в приложение'):
            pin.pin_desk_located()
            pin.close_pin_click()
        with allure.step('Открыта главная страница, в верхней части страницы '
                         'указан ваш телефонный номер и отображается баланс'):
            main.check_user_authored(TEST_USER['NUMBER'])

