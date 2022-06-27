from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class ChangeLanguagePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._language_list = (MobileBy.ID, f'{ENV}:id/languagesRecyclerView')

    def check_languages_list(self):
        with allure.step('Обнаружить список доступных языков для смены языка интерфейса'):
            self.assert_element_located(*self._language_list)
            allure_screenshot(self.driver)