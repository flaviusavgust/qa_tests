import allure

from common_imports import *


class SwapResources(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._phone_input = (MobileBy.ID, f'{env}:id/phoneEditTextView')
        self._down_icon_gb = (MobileBy.ID, f'{env}:id/arrowDownIconView')
        self._gbs = (MobileBy.ID, f'{env}:id/itemViewGroup')
        self._give_resources_button = (MobileBy.ID, f'{env}:id/giveResourcesButton')
        self.sure_give = (MobileBy.ID, 'android:id/button1')
        self._push_notification = (MobileBy.ID, f'{env}:id/iconImageView')
        self._title_text = (MobileBy.ID, f'{env}:id/titleTextView')

    def check_swap_resources_page_opened(self):
        with allure.step('Обнаружить страницу передачи ресурсов'):
            self.assert_text_inside_element(*self._title_text, text='Передать гигабайты')
            self.assert_element_located(*self._give_resources_button)
            allure_screenshot(self.driver)

    def input_phone(self, phone):
        with allure.step(f'Ввести номер телефона:{str(phone)} в поле ввода телефона'):
            self.input(*self._phone_input, text=phone)

    def click_down_icon(self):
        with allure.step('Кликнуть на вывести список кол-во ГБ для передачи'):
            self.click(*self._down_icon_gb)

    def click_select_one_gb(self):
        with allure.step('Кликнуть на выбрать один GB'):
            self.click(*self._gbs, unique=False, index=1)

    def click_give_resources_button(self):
        with allure.step('Кликнуть на передать ресурсы'):
            self.click(*self._give_resources_button)

    def sure_give_click(self):
        with allure.step('Подтвердить передачу ресурсов'):
            self.click(*self.sure_give)

    def wait_disappear_push(self):
        with allure.step('Подождать пока не исчезнет пуш уведомление'):
            self.wait_until_disappear(*self._push_notification, timeout=6)

    def check_push_ok(self):
        with allure.step('Обнаружить пуш уведомление о том что передача ресурсов успешно'):
            self.assert_element_located(*self._push_notification, timeout=10)
            allure_screenshot(self.driver)
