from src.pages.tele2.main_page import Chapters
from common_imports import *
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone
from src.pages.tele2.more_tab import MoreTab, OfficesAndAre, ChangeSimPage, NewsPage, AboutPage, SettingsPage

AUTOPAYMENT_USER = user_for_test()['AUTOPAYMENT_FIRST_USER']


class TestMoreTab:

    @allure.id("99")
    @allure.title("Проверка наличия подраздела “Офисы и карта покрытия”")
    @allure.label("suite", "Главная страница")
    @allure.label("owner", "admin")
    @allure.feature("Проверка наличия разделов")
    def test_check_offices_and_area(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        more_tab = MoreTab(driver_fixture)
        offices_and_are = OfficesAndAre(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step("В главной странице нажать на раздел “Еще” в нижней части страницы."):
            chapters.click_more()
        with allure.step("В появившейся вкладке нажать на подраздел “Офисы и карта покрытия”"):
            more_tab.click_offices_and_coverage_area()
        with allure.step("Ожидаемый результат: Появляются данные подраздела “Офисы и карта покрытия”"):
            offices_and_are.check_offices_and_area_page_opened()

    @allure.id("100")
    @allure.title("Проверка наличия подраздела “Заменить SIM”")
    @allure.label("suite", "Главная страница")
    @allure.label("owner", "admin")
    @allure.feature("Проверка наличия разделов")
    def test_check_change_sim(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        more_tab = MoreTab(driver_fixture)
        change_sim = ChangeSimPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step("В главной странице нажать на раздел “Заменить SIM” в нижней части страницы."):
            chapters.click_more()
            more_tab.click_change_sim()
        with allure.step("Ожидаемый результат: Появляются дополнительные подразделы раздела “Заменить SIM”"):
            change_sim.check_change_sim_page_opened()

    @allure.id("101")
    @allure.title("Проверка наличия подраздела “Новости”")
    @allure.label("suite", "Главная страница")
    @allure.label("owner", "admin")
    @allure.feature("Проверка наличия разделов")
    def test_check_news(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        more_tab = MoreTab(driver_fixture)
        news = NewsPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step("В главной странице нажать на раздел “Еще” в нижней части страницы."):
            chapters.click_more()
        with allure.step("В появившейся вкладке нажать на подраздел “Новости”"):
            more_tab.click_news()
        with allure.step("Ожидаемый результат: Появляются данные подраздела “Новости”"):
            news.check_news_page_opened()

    @allure.id("102")
    @allure.title("Проверка наличия подраздела “О компании”")
    @allure.label("suite", "Главная страница")
    @allure.label("owner", "admin")
    @allure.feature("Проверка наличия разделов")
    def test_about_company(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        more_tab = MoreTab(driver_fixture)
        about = AboutPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step("В главной странице нажать на раздел “Еще” в нижней части страницы."):
            chapters.click_more()
        with allure.step("В появившейся вкладке нажать на подраздел “О компании”"):
            more_tab.click_about_company()
        with allure.step("Ожидаемый результат: Появляются данные подраздела “О компании”"):
            about.check_about_company_page_opened()

    @allure.id("103")
    @allure.title("Проверка наличия подраздела “Настройки”")
    @allure.label("suite", "Главная страница")
    @allure.label("owner", "admin")
    @allure.feature("Проверка наличия разделов")
    def test_check_settings(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        more_tab = MoreTab(driver_fixture)
        settings = SettingsPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step("В главной странице нажать на раздел “Еще” в нижней части страницы"):
            chapters.click_more()
        with allure.step("В появившейся вкладке нажать на подраздел “Настройки”"):
            more_tab.click_settings()
        with allure.step("Ожидаемый результат: Появляются данные подраздела “Настройки”"):
            settings.check_setting_page_opened()
