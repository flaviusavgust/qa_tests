from src.pages.tele2.main_page import Chapters
from src.pages.tele2.details_page import DetailsPage
from src.pages.tele2.services_page import ServicesPage
from src.pages.tele2.help_page import HelpPage
from src.pages.tele2.more_tab import MoreTab
from common_imports import *
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone

AUTOPAYMENT_USER = user_for_test()['AUTOPAYMENT_FIRST_USER']


class TestChaptersMain:

    @allure.id("95")
    @allure.title("Проверка наличия раздела “Детализация”")
    @allure.feature("Проверка наличия разделов")
    def test_check_details_chapter(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        details = DetailsPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

        with allure.step("В главной странице нажать на раздел “Детализация” в нижней части страницы."):
            chapters.click_details()
        with allure.step("Появляется страница раздела “Детализация” со всеми данными"):
            details.check_details_page_opened()

    @allure.id("96")
    @allure.title("Проверка наличия раздела “Услуги”")
    @allure.feature("Проверка наличия разделов")
    def test_check_services_chapter(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        services = ServicesPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

        with allure.step("В главной странице нажать на раздел “Услуги” в нижней части страницы"):
            chapters.click_services()

        with allure.step("Появляется страница раздела “Услуги” со всеми данными"):
            services.check_services_page_opened()

    @allure.id("97")
    @allure.title("Проверка наличия раздела “Помощь”")
    @allure.feature("Проверка наличия разделов")
    def test_check_help_chapter(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        help_page = HelpPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

        with allure.step("В главной странице нажать на раздел “Помощь” в нижней части страницы."):
            chapters.click_help()

        with allure.step("Появляется страница раздела “Помощь” со всеми данными"):
            help_page.check_help_page_opened()

    @allure.id("98")
    @allure.title("Проверка наличия раздела “Еще”")
    @allure.feature("Проверка наличия разделов")
    def test_more_tab(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        more_tab = MoreTab(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

        with allure.step("В главной странице нажать на раздел “Еще” в нижней части страницы."):
            chapters.click_more()

        with allure.step("Ожидаемый результат: Появляются дополнительные подразделы раздела “Еще”"):
            more_tab.check_more_tab()
