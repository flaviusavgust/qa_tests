from src.pages.tele2.auth_page import AuthPage, SetPin
from src.pages.tele2.main_page import MainPage
import allure


def login_wia_phone(driver_fixture, phone: str, password: str):
    auth = AuthPage(driver_fixture)
    pin = SetPin(driver_fixture)

    # auth.click_to_become_caller()
    # auth.switch_to_webview()
    # auth.back_to_native_after_switch_wv()
    # auth.back()

    with allure.step(f'Setup Авторизация с номером{str(phone)}'):
        with allure.step(f'Ввод номера:{phone} в поле ввода номера'):
            auth.input_phone(str(phone))
        with allure.step('Клик на "Продолжить"'):
            auth.resume_button_click()
        with allure.step('Ввод пароля'):
            auth.input_pass(str(password))
        with allure.step('Клик на кнопку "Войти"'):
            auth.login_button_click()
        with allure.step('Клик на иконку "Закрыть" на странице задания ПИН'):
            pin.close_pin_click()


def logout_from_account(driver_fixture):
    main = MainPage(driver_fixture)

    with allure.step('Setup или Teardown по выходу из аккаунта'):
        main.click_my_number()
        main.click_logout()
        main.sure_logout_click()
