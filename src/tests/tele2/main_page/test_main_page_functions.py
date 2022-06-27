from src.pages.tele2.main_page import MainPage
from src.pages.tele2.my_tarif import TarrifPage
from src.pages.tele2.qr_page import QrPayPage
from src.pages.tele2.shares_page import SharesPage
from src.pages.tele2.group_discount_page import GroupDiscount
from src.pages.tele2.auto_payments import AutoPaymentsPage
from src.pages.tele2.daily_package_page import DailyPackagePage
from src.pages.tele2.store import StorePage
from src.pages.tele2.swap_resources import SwapResources
from common_imports import *
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone

TEST_USER = user_for_test()['AUTOPAYMENT_FIRST_USER']


class TestMainFunc:

    @allure.id("318")
    @allure.title('Проверка наличия раздела "QR оплата в транспорте"')
    @allure.label("owner", "admin")
    @allure.feature("Главная страница - Разделы")
    def test_qa_pay_chapter(self, driver_fixture):
        main = MainPage(driver_fixture)
        qr_pay = QrPayPage(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step('Нажать на раздел "QR оплата в транспорте"'):
            main.click_qr_pay()
        with allure.step("Обнаружить страницу отправки смс-кода для верификации"):
            qr_pay.check_sms_info_located()

    @allure.id("320")
    @allure.title('Проверка наличия раздела "Акции Tele2"')
    @allure.label("owner", "admin")
    @allure.feature("Главная страница - Разделы")
    def test_share_chapter(self, driver_fixture):
        main = MainPage(driver_fixture)
        shares = SharesPage(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step('Нажать на раздел "Акции Tele2"'):
            main.click_share_tele2()
        with allure.step('Обнаружить страницу с подразделами "Актуальные" и "Архивные"'):
            shares.check_share_card()

    @allure.id("328")
    @allure.title('Проверка наличия раздела "Выгодно вместе"')
    @allure.label("owner", "admin")
    @allure.feature("Главная страница - Разделы")
    def test_group_discount_chapter(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_disc = GroupDiscount(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step('Нажать на раздел "Выгодно вместе"'):
            main.click_group_discounts()
        with allure.step("Обнаружить страницу Выгодно вместе"):
            group_disc.check_group_discounts_loaded()

    @allure.title("Проверка наличия раздела “Автоплатеж”")
    @allure.feature("Автоплатежи")
    def test_check_visibility_auto_payments(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('Открывается страница автоплатежа '):
            auto_p.check_autopayment_page_empty()

    @allure.id("319")
    @allure.title('Проверка наличия раздела "Ежедневный пакет"')
    @allure.label("owner", "admin")
    @allure.feature("Главная страница - Разделы")
    def test_daily_packet_chapter(self, driver_fixture):
        main = MainPage(driver_fixture)
        daily_pack = DailyPackagePage(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step('Нажать на раздел "Ежедневный пакет"'):
            main.click_daily_package()
        with allure.step("Обнаружить страницу с информацией и функционалом ежедневных пакетов: \"Отключить\", "
                         "\"Пополнить баланс\""):
            daily_pack.check_daily_package_info()

    @allure.title("Проверка наличия раздела “Мой тариф”")
    @allure.feature("Тариф")
    def test_check_visibility_my_tarrif_page(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        # 7076422303

        with allure.step('Авторизоваться в приложении '):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])

        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()
        with allure.step('Появляются данные раздела “Мой тариф”'):
            tarrif.check_tarrif_components()

    @allure.id("316")
    @allure.title('Проверка наличия раздела "Магазин"')
    @allure.label("owner", "admin")
    @allure.feature("Главная страница - Разделы")
    def test_shop_chapter(self, driver_fixture):
        main = MainPage(driver_fixture)
        shop = StorePage(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step("Нажать на раздел \"Магазин\""):
            main.click_store()
        with allure.step("Обнаружить страницу с подразделами раздела \"Магазин\""):
            shop.check_store_services_opened()

    @allure.id("321")
    @allure.title('Проверка наличия раздела "Перевод ресурсов"')
    @allure.label("owner", "admin")
    @allure.feature("Главная страница - Разделы")
    def test_share_resources(self, driver_fixture):
        main = MainPage(driver_fixture)
        swap = SwapResources(driver_fixture)

        with allure.step("Авторизоваться в приложении Tele2"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step("Нажать на раздел \"Перевод ресурсов\""):
            main.click_swap_resources()
        with allure.step("Обнаружить страницу с информацией и подразделами \"Гигабайты\" и \"Минуты\""):
            swap.check_swap_resources_page_opened()

