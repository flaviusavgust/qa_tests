import allure

from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class ServicesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._page_title = (MobileBy.ID, f'{ENV}:id/titleTv')
        self._services_page = (MobileBy.ID, f'{ENV}:id/servicesTabContainer')
        self._services_list = (MobileBy.ID, f'{ENV}:id/serviceViewPager')
        self._services_name_text = (MobileBy.ID, f'{ENV}:id/serviceName')
        self._services_description = (MobileBy.ID, f'{ENV}:id/serviceDescriptionTextView')
        self._services_text = (MobileBy.ID, f'{ENV}:id/serviceListItemView')

    def check_services_page_opened(self):
        with allure.step('Проверить что заглавие страницы "Услуги"'):
            self.assert_text_inside_element(*self._page_title, text='Услуги')
        with allure.step('Проверить что открылась страница "Услуги"'):
            self.assert_element_located(*self._services_page)
        with allure.step('Проверить что отображается список услуг'):
            self.assert_element_located(*self._services_list)

            allure_screenshot(self.driver)

    def check_group_discounts_services_page_opened(self):
        with allure.step('Проверить что заглавие страницы "Услуги"'):
            self.assert_text_inside_element(*self._page_title, text='Услуги')
        with allure.step('Проверить что открылась страница услуги выгодно вместе'):
            self.assert_text_inside_element(*self._services_name_text, text='Выгодно вместе')
        with allure.step('Проверить что появилось описание услуги "Выгодно вместе"'):
            self.assert_text_inside_element(*self._services_description, text='Создай группу с близкими друзьями и '
                                                                              'вместе ежемесячно получайте скидку на '
                                                                              'мобильную связь. При этом неважно, '
                                                                              'в каком городе Казахстана живут '
                                                                              'друзья.')
            allure_screenshot(self.driver)

    def click_roaming(self):
        with allure.step('Нажать на "Роуминг"'):
            self.click(*self._services_text, unique=False, index=1)