import allure

from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class MoreTab(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._more_tab = (MobileBy.ID, f'{ENV}:id/moreTabContainer')
        self._offices_and_coverage_area = (MobileBy.ID, f'{ENV}:id/officesView')
        self._change_sim = (MobileBy.ID, f'{ENV}:id/changeSimView')
        self._news = (MobileBy.ID, f'{ENV}:id/newsView')
        self._about = (MobileBy.ID, f'{ENV}:id/aboutView')
        self._settings = (MobileBy.ID, f'{ENV}:id/settingsView')

    def check_more_tab(self):
        with allure.step('Проверить что открылось меню с дополнительными вкладками'):
            self.assert_element_located(*self._more_tab)
            allure_screenshot(self.driver)

    def click_offices_and_coverage_area(self):
        with allure.step('Нажать на "Офисы и карта покрытия"'):
            self.click(*self._offices_and_coverage_area)

    def click_change_sim(self):
        with allure.step('Нажать на "Заменить SIM"'):
            self.click(*self._change_sim)

    def click_news(self):
        with allure.step('Нажать на "Новости"'):
            self.click(*self._news)

    def click_about_company(self):
        with allure.step('Нажать на "О компании"'):
            self.click(*self._about)

    def click_settings(self):
        with allure.step('Нажать на "Настройки"'):
            self.click(*self._settings)


class OfficesAndAre(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._city_input = (By.XPATH, '//*[@class="p-3 css-of5cst e1vq31dk0"]')

    def check_offices_and_area_page_opened(self):
        self.switch_to_webview(timeout=10)
        with allure.step('Проверить что открылась страница офисов и покрытия'):
            self.assert_element_located(*self._city_input)
            allure_screenshot(self.driver)
        self.back_to_native_after_switch_wv()


class ChangeSimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._yes_almaty = (By.XPATH, '//*[@class="css-18v40m9 e1rym3c70"]')
        self._change_sim_title = (By.XPATH, '//*[@class="mb-4 css-w8ceuc e1r1ca9c2"]')

    def check_change_sim_page_opened(self):
        self.switch_to_webview(timeout=10)
        self.click(*self._yes_almaty)
        with allure.step('Проверить что открылась страница "Заменить SIM"'):
            self.assert_element_located(*self._change_sim_title)
            allure_screenshot(self.driver)
        self.back_to_native_after_switch_wv()


class NewsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._news_categories = (By.XPATH, '//*[@class="flex-wrap d-flex"]')
        self._news_title = (By.XPATH, '//*[@class="pt-0 pt-md-4 mb-5 css-12jigj6 e1r1ca9c3"]')

    def check_news_page_opened(self):
        self.switch_to_webview(timeout=10)
        with allure.step('Проверить что открылась страница "Новости"'):
            self.assert_element_located(*self._news_title)
            self.assert_element_located(*self._news_categories)
            allure_screenshot(self.driver)
        self.back_to_native_after_switch_wv()


class AboutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._title_work_at_tele2 = (By.XPATH, '//*[@class="d-flex d-md-none css-w8ceuc e1r1ca9c2"]')

    def check_about_company_page_opened(self):
        self.switch_to_webview(timeout=10)
        with allure.step('Проверить что открылась страница "О компании"'):
            self.assert_element_located(*self._title_work_at_tele2)
            allure_screenshot(self.driver)
        self.back_to_native_after_switch_wv()


class SettingsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self._title = (MobileBy.ID, f'{ENV}:id/titleTv')
        self._setting_list = (MobileBy.ID, f'{ENV}:id/settingsRv')

    def check_setting_page_opened(self):
        with allure.step('Проверить что открылась страница "Настройки"'):
            self.assert_text_inside_element(*self._title, text='Настройки')
            self.assert_element_located(*self._setting_list)
            allure_screenshot(self.driver)