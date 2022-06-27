from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class ApplyNumberPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._description_text = (MobileBy.ID, f'{ENV}:id/descriptionTv')

    def check_alert_located(self):
        with allure.step('Обнаружить текст с предупреждением'):
            self.assert_element_located(*self._description_text)
            allure_screenshot(self.driver)
