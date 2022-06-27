import allure

from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class StorePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._service_item = (MobileBy.ID, f'{ENV}:id/serviceItemView')
        self._group_shops = (MobileBy.ID, f'{ENV}:id/mainGroupView')
        self._continue_button = (MobileBy.ID, f'{ENV}:id/button')
        self._yes_button_city = (By.XPATH, '//*[@class="css-18v40m9 e1rym3c70" and text()="Да"]')
        self._find_your_number_title = (By.XPATH, '//*[@class="css-12jigj6 e1r1ca9c3"]')
        self._move_number_title = (By.XPATH, '//*[@class="css-t4gtqo e1r1ca9c6"]')
        self._smartphones_title = (By.XPATH, '//*[@class="css-1634i9q e1r1ca9c6"]')
        self._my_orders_title = (By.XPATH, '//*[@class="css-3ekbkc e1r1ca9c1"]')
        self._cart_title = (By.XPATH, '//*[@class="mr-2 css-11fuxef e1r1ca9c6"]')

    def check_store_services_opened(self):
        with allure.step('Обнаружить подразделы Магазина'):
            self.assert_element_located(*self._group_shops)
            allure_screenshot(self.driver)

    def click_buy_new_number(self):
        with allure.step('Нажать на "Купить новый номер"'):
            self.click(*self._service_item, unique=False, index=0)

    def click_move_number(self):
        with allure.step('Нажать на "Перенести свой номер"'):
            self.click(*self._service_item, unique=False, index=1)

    def click_smartphones(self):
        with allure.step('Нажать на "Смартфоны"'):
            self.click(*self._service_item, unique=False, index=2)

    def click_order_history(self):
        with allure.step('Нажать на "История заказов"'):
            self.click(*self._service_item, unique=False, index=3)

    def click_order_cart(self):
        with allure.step('Нажать на "Корзину"'):
            self.click(*self._service_item, unique=False, index=4)

    def click_continue(self):
        with allure.step('Нажать на "Продолжить"'):
            self.click(*self._continue_button)

    def check_buy_new_number_opened(self):
        with allure.step('Обнаружить страницу покупки новых номеров'):
            self.switch_to_webview()
            self.click(*self._yes_button_city)
            self.assert_element_located(*self._find_your_number_title)
            allure_screenshot(self.driver)

    def check_move_number_opened(self):
        with allure.step('Обнаружить страницу переноса номеров'):
            self.switch_to_webview()
            self.click(*self._yes_button_city)
            self.assert_element_located(*self._move_number_title)
            allure_screenshot(self.driver)

    def check_smartphones_page_landing(self):
        with allure.step('Обнаружить лэндинг страницу контрактных смартфонов'):
            self.switch_to_webview()
            self.assert_element_located(*self._smartphones_title)
            allure_screenshot(self.driver)

    def check_order_history_page(self):
        with allure.step('Обнаружить страницу моих заказов'):
            self.switch_to_webview()
            self.click(*self._yes_button_city)
            self.assert_element_located(*self._my_orders_title)
            allure_screenshot(self.driver)

    def check_cart_page(self):
        with allure.step('Обнаружить страницу моих заказов'):
            self.switch_to_webview()
            self.click(*self._yes_button_city)
            self.assert_element_located(*self._cart_title)
            allure_screenshot(self.driver)


