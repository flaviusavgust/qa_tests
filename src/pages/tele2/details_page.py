import allure

from common_imports import *
import re
from src.helpers.constants import ENVIRONMENT as ENV


class DetailsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._page_title = (MobileBy.ID, f'{ENV}:id/titleTv')

    def check_details_page_opened(self):
        with allure.step('Проверить что заглавие страницы "Детализация"'):
            self.assert_text_inside_element(*self._page_title, text='Детализация')
            allure_screenshot(self.driver)
