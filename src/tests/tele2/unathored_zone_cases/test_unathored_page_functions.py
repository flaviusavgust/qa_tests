import allure
from src.pages.tele2.apply_number_page import ApplyNumberPage
from src.pages.tele2.change_language_page import ChangeLanguagePage
from src.pages.tele2.help_page import HelpPage
from src.pages.tele2.more_tab import OfficesAndAre
from common_imports import *
from src.pages.tele2.auth_page import AuthPage
from src.pages.tele2.store import StorePage


# TO:D0 Добавить ассерт страницы добавления карты


class TestUnathoredFunc:

    @allure.id("333")
    @allure.title('Проверка наличия раздела "Офисы и карта покрытия"')
    @allure.label("owner", "admin")
    @allure.feature("Страница авторизации")
    def test_offices_page(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        office_and_are = OfficesAndAre(driver_fixture)

        with allure.step("Запустить приложение Tele2 Kazakhstan"):
            pass
        with allure.step('Нажать на раздел "Офисы и карты покрытия"'):
            auth.click_to_offices_and_location()
        with allure.step('Обнаружить страницу с картой и подразделами "Салоны связи" и "Карта покрытия"'):
            office_and_are.check_offices_and_area_page_opened()

    @allure.id("336")
    @allure.title('Проверка наличия раздела "Оформить номер"')
    @allure.label("owner", "admin")
    @allure.feature("Страница авторизации")
    def test_become_caller(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Запустить приложение Tele2 Kazakhstan"):
            pass
        with allure.step('Нажать на раздел "Оформить номер"'):
            auth.click_to_become_caller()
        with allure.step("Обнаружить открытие страницы оформления номера"):
            store.check_buy_new_number_opened()

    @allure.id("335")
    @allure.title('Проверка наличия раздела "Перейти в Tele2"')
    @allure.label("owner", "admin")
    @allure.feature("Страница авторизации")
    def test_move_number(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Запустить приложение Tele2 Kazakhstan"):
            pass
        with allure.step('Нажать на раздел "Перейти в Tele2"'):
            auth.click_to_move_number()
        with allure.step("Обнаружить открытие webview с запросом номера для переноса и информацией текущей услуги"):
            store.check_move_number_opened()

    @allure.id("337")
    @allure.title('Проверка наличия раздела "Помощь"')
    @allure.label("owner", "admin")
    @allure.feature("Страница авторизации")
    def test_help(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        help_page = HelpPage(driver_fixture)

        with allure.step("Запустить приложение Tele2 Kazakhstan"):
            pass
        with allure.step('Нажать на раздел "Помощь"'):
            auth.click_to_help()
        with allure.step("Обнаружить страницу со списком вопросов и поле поиска"):
            help_page.check_help_page_opened()

    @allure.id("336")
    @allure.title('Проверка наличия раздела "Оформить номер"')
    @allure.label("owner", "admin")
    @allure.feature("Страница авторизации")
    def test_apply_number(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        apply_number = ApplyNumberPage(driver_fixture)

        with allure.step("Запустить приложение Tele2 Kazakhstan"):
            pass
        with allure.step('Нажать на раздел "Оформить номер"'):
            auth.click_to_apply_number()
        with allure.step("Обнаружить открытие страницы оформления номера"):
            apply_number.check_alert_located()

    @allure.id("334")
    @allure.title("Проверка наличия раздела \"Язык интерфейса\"")
    @allure.label("owner", "admin")
    @allure.feature("Страница авторизации")
    def test_change_language(self, driver_fixture):
        auth = AuthPage(driver_fixture)
        language = ChangeLanguagePage(driver_fixture)

        with allure.step("Запустить приложение Tele2 Kazakhstan"):
            pass
        with allure.step("Нажать на раздел \"Язык интерфейса\""):
            auth.click_to_interface_language()
        with allure.step("Обнаружить страницу со списком языков интерфейса"):
            language.check_languages_list()


