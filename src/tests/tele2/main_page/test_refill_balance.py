from src.pages.tele2.main_page import MainPage
from src.pages.tele2.refill_page import RefillPage
from common_imports import *
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone


tarrif_user = user_for_test()['TARRIF_USER']
autopayments_user = user_for_test()['AUTOPAYMENT_FIRST_USER']
int_package_user = user_for_test()['INTERNET_PACKAGE_USER']
send_package_user = user_for_test()['USER_FOR_SEND_INTERNET_PACKAGE']


class TestRefillBalance:

    @allure.id("74")
    @allure.title("Пополнение баланса картой (свой номер-привязанная карта)")
    @allure.label("suite", "Главная страница")
    @allure.label("owner", "admin")
    @allure.feature("Пополнение баланса")
    def test_refill_balance(self, driver_fixture):
        main = MainPage(driver_fixture)
        refill = RefillPage(driver_fixture)
        login_wia_phone(phone=tarrif_user['phone'], password=tarrif_user['password'], driver_fixture=driver_fixture)
        refill_test_sum = 10

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            pass
        with allure.step("В главной странице нажать на кнопку “+ пополнить” в верхней части страницы"):
            main.click_on_fill_balance()
        with allure.step("Ввести сумму в поле ввода суммы"):
            refill.input_refill_sum(refill_test_sum)
        with allure.step("Выбрать карту"):
            pass
        with allure.step("Нажать на поле выбора карты для оплаты"):
            pass
        with allure.step("Нажать на кнопку ”Пополнить"):
            pass
        with allure.step("Ожидаемый результат: Баланс был пополнен на указанную абонентом сумму"):
            pass
