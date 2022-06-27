from src.helpers.constants import ENVIRONMENT as ENV
from common_imports import *


class AuthPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._login_with_number = (MobileBy.ACCESSIBILITY_ID, 'По номеру')
        self._login_with_mail = (MobileBy.ACCESSIBILITY_ID, 'По e-mail')
        self._input_phone = (MobileBy.ID, f'{env}:id/phoneEditTextView')
        self._input_mail = (MobileBy.ID, f'{env}:id/emailEditTextView')
        self._resume_button = (MobileBy.ID, f'{env}:id/loginButtonView')
        self._resume_button_mail = (MobileBy.ID, f'{env}:id/loginEmailButtonView')
        self._input_password = (MobileBy.ID, f'{env}:id/passEditTextView')
        self._login_button = (MobileBy.ID, f'{env}:id/loginButton')
        self._push_text = (MobileBy.ID, f'{env}:id/messageTextView')
        self._become_caller = (MobileBy.ID, f'{env}:id/eshopRelativeView')
        self._offices_and_card = (MobileBy.ID, f'{env}:id/locationRelativeView')
        self._move_to_tele2 = (MobileBy.ID, f'{env}:id/changeSimRelativeView')
        self._help = (MobileBy.ID, f'{env}:id/chatRelativeView')
        self._apply_number = (MobileBy.ID, f'{env}:id/newNumberRelativeView')
        self._language_change = (MobileBy.ID, f'{env}:id/languageRelativeView')
        self._back_icon = (MobileBy.ID, f'{env}:id/rightIconBv')
        self._yes = (By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div/div/button[2]/span')

    def click_to_become_caller(self):
        with allure.step('Нажать на "Стать абонентом"'):
            self.click(*self._become_caller)

    def click_to_offices_and_location(self):
        with allure.step('Нажать на "Офисы и карта покрытия"'):
            self.click(*self._offices_and_card)

    def click_to_move_number(self):
        with allure.step('Нажать на "Перейти в Tele2"'):
            self.click(*self._move_to_tele2)

    def click_to_help(self):
        with allure.step('Нажать на "Помощь"'):
            self.click(*self._help)

    def click_to_apply_number(self):
        with allure.step('Нажать на "Помощь"'):
            self.click(*self._apply_number)

    def click_to_interface_language(self):
        with allure.step('Нажать на "Язык интерфейса"'):
            self.click(*self._language_change)

    def click_yes(self):
        self.click(*self._yes)

    def click_close_icon(self):
        self.click(*self._back_icon)

    def click_login_with_phone(self):
        with allure.step('Клик на "Авторизация по номеру"'):
            self.click(*self._login_with_number)

    def click_login_with_mail(self):
        with allure.step('Клик на "Авторизация по mail"'):
            self.click(*self._login_with_mail)

    def input_phone(self, phone):
        with allure.step(f'Ввод номера: {str(phone)} в поле ввода номера телефона'):
            self.input(*self._input_phone, text=str(phone))
            allure_screenshot(self.driver)

    def input_mail(self, mail):
        with allure.step(f'Ввод email: {mail} в поле ввода логина'):
            self.input(*self._input_mail, text=mail)
            allure_screenshot(self.driver)

    def resume_button_click(self):
        with allure.step('Клик на продолжить авторизацию'):
            self.click(*self._resume_button)

    def resume_button_click_mail(self):
        with allure.step('Клик на продолжить авторизацию'):
            self.click(*self._resume_button_mail)

    def input_pass(self, password):
        with allure.step('Ввод пароля'):
            self.input(*self._input_password, text=str(password))

    def login_button_click(self):
        with allure.step('Клик на "Авторизоваться"'):
            self.click(*self._login_button)

    def check_push_wrong_password_or_login(self):
        with allure.step('Обнаружить пуш уведомление о неверном номере или пароле'):
            self.assert_text_inside_element(*self._push_text, text='Неверный номер или пароль. Попробуйте еще раз.')
            allure_screenshot(self.driver)


class SetPin(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._pin_desk = (MobileBy.ID, f'{ENV}:id/pinDescTv')
        self._repeat_pin_text = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/pinDescTv" and @text="Повторите '
                                                 'ПИН-код"]')
        self._close_pin_input = (MobileBy.ID, f'{ENV}:id/backImageView')

    def pin_desk_located(self):
        with allure.step('Обнаружить страницу задания ПИН'):
            self.assert_element_located(*self._pin_desk)
            allure_screenshot(self.driver)

    def set_pin(self, pin1, pin2, pin3, pin4):
        # Передаем 4 цифры для пина
        pin_numbers = [pin1, pin2, pin3, pin4]
        with allure.step(f'Задать ПИН для входа: {str(pin1), str(pin2), str(pin3), str(pin4)}'):
            for x in pin_numbers:
                _pin_number = (
                    MobileBy.XPATH, f'//*[@resource-id="{env}:id/keyboardButtonTv" and @text="{str(x)}"]')
                self.click(*_pin_number)

    def check_repeat_pin_text_located(self):
        with allure.step('Обнаружить страницу повтора пин'):
            self.assert_element_located(*self._repeat_pin_text)
            allure_screenshot(self.driver)

    def close_pin_click(self):
        with allure.step('Кликнуть на иконку закрытия страницы ввода ПИН'):
            self.click(*self._close_pin_input)
