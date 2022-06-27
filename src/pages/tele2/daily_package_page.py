from src.helpers.constants import ENVIRONMENT as ENV
from common_imports import *


class DailyPackagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._daily_package_info_text = (MobileBy.ID, f'{ENV}:id/descriptionTv')

    def check_daily_package_info(self):
        with allure.step('Обнаружить информационный текст ежедневных пакетов'):
            self.assert_element_located(*self._daily_package_info_text)
            allure_screenshot(self.driver)
