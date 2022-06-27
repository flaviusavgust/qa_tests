from src.pages.tele2.main_page import RoamingPopUp, MainPage, RoamingMainPage
from src.pages.tele2.main_page import Chapters
from src.pages.tele2.roaming_page import RoamingPage
from src.pages.tele2.services_page import ServicesPage
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone
from common_imports import *

TEST_USER = user_for_test()['ROAMING_USER']
TEST_DATA = data_for_test()['ROAMING_DATA']


# TO:D0 Добавить ассерт страницы добавления карты

class TestRoamingCases:

    @allure.id("249")
    @allure.title("Активация Pop-up с уведомлением роуминга")
    @allure.label("owner", "admin")
    @allure.feature("Роуминг")
    def test_pop_up_check_roaming_main(self, driver_fixture):
        roaming_popup = RoamingPopUp(driver_fixture)

        with allure.step("Войти в приложение с подключенным роумингом"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step("Открывается pop-up с приветсвием в какой-либо стране "):
            roaming_popup.check_welcome_text_located(TEST_DATA['ROAMING_COUNTRY'])

    @allure.id("159")
    @allure.title("Открытие страницы роуминга")
    @allure.label("owner", "admin")
    @allure.feature("Роуминг")
    def test_check_roaming_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        roaming = RoamingPage(driver_fixture)

        with allure.step("Войти в приложение с подключенным роумингом"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step("Нажать на Роуминг на главной странице"):
            main.click_roaming()
        with allure.step("Открывается страница базовой тарификации услуг"):
            roaming.check_roaming_info_located()

    @allure.id("137")
    @allure.title("Вход в приложение с подключенным роумингом")
    @allure.label("owner", "admin")
    @allure.feature("Роуминг")
    def test_main_menu_roaming_page(self, driver_fixture):
        roaming_main_page = RoamingMainPage(driver_fixture)

        with allure.step("Войти в приложение с подключенным роумингом"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step("Открывается главная страница с меню роуминга, где отображается информация о роуминге"):
            roaming_main_page.check_user_in_roaming_main_page(TEST_DATA['ROAMING_COUNTRY'])

    @allure.id("160")
    @allure.title('Открытие страницы роуминга через "Услуги" через пользователя который находится в роуминге')
    @allure.label("owner", "admin")
    @allure.feature("Роуминг")
    def test_open_roaming_page_from_services(self, driver_fixture):
        chapters = Chapters(driver_fixture)
        services = ServicesPage(driver_fixture)
        roaming = RoamingPage(driver_fixture)

        with allure.step("Войти в приложение с подключенным роумингом"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
        with allure.step('Перейти в раздел "Услуги"'):
            chapters.click_services()
        with allure.step("Нажать на \"Роуминг\""):
            services.click_roaming()
        with allure.step("Открывается страница базовой тарификации услуг роуминга "):
            roaming.check_roaming_info_located()

    @allure.id("158")
    @allure.title('Включение роуминга через вкладку "Роуминг" в главной странице')
    @allure.label("owner", "admin")
    @allure.feature("Роуминг")
    def test_turn_on_roaming(self, driver_fixture):
        roaming = RoamingPage(driver_fixture)
        main = MainPage(driver_fixture)
        roaming_main_page = RoamingMainPage(driver_fixture)

        with allure.step("Войти в приложение с подключенным роумингом"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
            roaming_main_page.check_roaming_deactivated()
        with allure.step('Нажать на раздел "Роуминг" в главной странице'):
            main.click_roaming()
        with allure.step("Нажать на индикатор включения роуминга"):
            roaming.check_roaming_deactivated()
            roaming.click_switcher_roaming()
            roaming.click_ok_activate_roaming()
        with allure.step(
                "Появляется уведомление об успешном включении услуги. Через некоторое время услуга включается"):
            roaming.check_push_roaming_activated_located()
            roaming.back()
            main.update_page()
            main.update_page()
            main.update_page()
            main.update_page()
            roaming_main_page.check_roaming_activated()
            main.click_roaming()
            roaming.check_roaming_activated()

    @allure.id("157")
    @allure.title('Отключение роуминга через вкладку "Роуминг" в главной странице')
    @allure.label("owner", "admin")
    @allure.feature("Роуминг")
    def test_turn_off_roaming(self, driver_fixture):
        roaming = RoamingPage(driver_fixture)
        main = MainPage(driver_fixture)
        roaming_main_page = RoamingMainPage(driver_fixture)

        with allure.step("Войти в приложение с подключенным роумингом"):
            login_wia_phone(driver_fixture, phone=TEST_USER['PHONE_NUMBER'], password=TEST_USER['PASSWORD'])
            roaming_main_page.check_roaming_activated()
        with allure.step("Нажать на раздел \"Роуминг\" в главной странице"):
            main.click_roaming()
        with allure.step("Нажать на индикатор включения роуминга"):
            roaming.check_roaming_activated()
            roaming.click_switcher_roaming()
            roaming.click_ok_activate_roaming()

        with allure.step("Появляется уведомление об успешном отключении услуги. Через некоторое время услуга "
                         "отключается"):
            roaming.check_push_roaming_deactivated_located()
            roaming.back()
            main.update_page()
            main.update_page()
            main.update_page()
            main.update_page()
            roaming_main_page.check_roaming_deactivated()
            main.click_roaming()
            roaming.check_roaming_deactivated()
