import allure
from src.pages.tele2.main_page import Chapters
from common_imports import *
from src.pages.tele2.store import StorePage
from src.pages.tele2.main_page import MainPage
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone

TEST_USER = user_for_test()['AUTOPAYMENT_FIRST_USER']


class TestEshopSubsection:

    @allure.id("322")
    @allure.title('Проверка наличия подраздела "Купить новый номер"')
    def test_check_buy_new_number_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Авторизоваться а приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step('Нажать на раздел "Магазин"'):
            main.click_store()
        with allure.step('Нажать на подраздел "Купить новый номер"'):
            store.click_buy_new_number()
        with allure.step("Обнаружить открытие webview с предложенными номерами"):
            store.check_buy_new_number_opened()

    @allure.id("324")
    @allure.title('Проверка наличия подраздела "Перенести свой номер"')
    def test_move_number_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Авторизоваться а приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step('Нажать на раздел "Магазин"'):
            main.click_store()
        with allure.step('Нажать на подраздел "Перенести свой номер"'):
            store.click_move_number()
        with allure.step("Обнаружить открытие webview с запросом номера для переноса и информацией текущей услуги"):
            store.check_move_number_opened()

    @allure.id("323")
    @allure.title('Проверка наличия подраздела "Смартфоны"')
    def test_smartphones_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Авторизоваться а приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])

        with allure.step("Нажать на раздел \"Магазин\""):
            main.click_store()
        with allure.step('Нажать на подраздел "Смартфоны"'):
            store.click_smartphones()
        with allure.step("Обнаружить открытие webview каталогом предложенных  устройств"):
            store.check_smartphones_page_landing()

    @allure.id("325")
    @allure.title('Проверка наличия подраздела "История заказов"')
    def test_order_history_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Авторизоваться а приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])

        with allure.step('Нажать на раздел "Магазин"'):
            main.click_store()
        with allure.step('Нажать на подраздел "История заказов"'):
            store.click_order_history()
        with allure.step("Обнаружить открытие webview с историями заказов текущего пользователя"):
            store.check_order_history_page()

    @allure.id("326")
    @allure.title('Проверка наличия подраздела "Корзина"')
    def test_cart_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Авторизоваться а приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])

        with allure.step('Нажать на раздел "Магазин"'):
            main.click_store()
        with allure.step('Нажать на подраздел "Корзина"'):
            store.click_order_cart()
        with allure.step("Обнаружить открытие webview с товарами корзины"):
            store.check_cart_page()

    @allure.id("327")
    @allure.title("Кнопка продолжить")
    def test_continue_button(self, driver_fixture):
        main = MainPage(driver_fixture)
        store = StorePage(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])

        with allure.step('Нажать на раздел "Магазин"'):
            main.click_store()
        with allure.step('Нажать на кнопку "Продолжить"'):
            store.click_continue()
        with allure.step('Обнаружить webview с каталогом предложенных номеров "Найди свой номер"'):
            store.check_buy_new_number_opened()
