from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class HelpPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._page_title = (MobileBy.ID, f'{ENV}:id/titleTv')
        self._help_page = (MobileBy.ID, f'{ENV}:id/helpTab')
        self._help_list = (MobileBy.ID, f'{ENV}:id/categoriesRv')

    def check_help_page_opened(self):
        with allure.step('Проверить что заглавие страницы "Помощь и частые вопросы"'):
            self.assert_text_inside_element(*self._page_title, text='Помощь и частые вопросы')

        with allure.step('Проверить что отображается список с помощью для пользователя'):
            self.assert_element_located(*self._help_list)
            allure_screenshot(self.driver)
