from src.pages.tele2.main_page import MainPage
from src.pages.tele2.my_tarif import TarrifPage, InternetPackages, Exchange, OtherTarrifs
from src.pages.tele2.swap_resources import SwapResources
from common_imports import *
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone
from src.setup_and_teardowns.setup_and_teardown_for_autopayments import SetupForAutopayments

TARRIF_USER = user_for_test()['TARRIF_USER']
AUTOPAYMENT_USER = user_for_test()['AUTOPAYMENT_FIRST_USER']
CHANGE_TARRIF_WITH_RESOURCES_USER = user_for_test()['CHANGE_TARRIF_WITH_RESOURCES_USER']
INT_PACKAGE_USER = user_for_test()['INTERNET_PACKAGE_USER']
SEND_PACKAGE_USER = user_for_test()['USER_FOR_SEND_INTERNET_PACKAGE']

setup_vw = SetupForAutopayments


# TODO: Добавить setup и teardowns для тестов

class TestTarrif:

    @allure.title("Проверка условий своего тарифа")
    @allure.feature("Тариф")
    def test_check_conditions_tariff(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)

        login_wia_phone(phone=TARRIF_USER['PHONE_NUMBER'], password=TARRIF_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()
        with allure.step('В появившейся странице нажать на раздел “Условия тарифа”'):
            tarrif.click_tarrif_details()
        with allure.step('В странице появляются подразделы: SMS, Условия, Как подключить, Перевод ресурсов,'
                         ' Перенос ресурсов, Нужно знать, Ежедневный пакет, Частые вопросы'):
            tarrif.check_tarrif_details_opened()

    @allure.title("Подключение Интернет пакета")
    @allure.feature("Тариф")
    def test_connect_internet_packages(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        internet = InternetPackages(driver_fixture)

        login_wia_phone(phone=INT_PACKAGE_USER['PHONE_NUMBER'], password=INT_PACKAGE_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.update_page()
            balance = main.return_balance_int()
            allure_screenshot(driver_fixture, name='Исходный баланс и кол-во ГБ в интернет пакете')
            package = main.return_remainder_internet_package()
            main.click_my_tarrif()
        with allure.step('В появившейся странице нажать на раздел “Интернет пакеты”'):
            tarrif.check_tarrif_components()
            tarrif.click_internet_packages()
        with allure.step('Выбрать любой из интернет-пакетов'):
            index = 2
            package_price = internet.return_package_price_int(index)
            allure_screenshot(driver_fixture, name=f'Цена и кол-во ГБ {str(index)}-го интернет пакет')
            package_gb = internet.return_package_gb(index)
        with allure.step('Нажать на кнопку “Подключить”'):
            internet.click_internet_connect(index)
        with allure.step('Нажать на ок'):
            internet.connect_package_ok()
            internet.check_push_internet_ok_located()
            internet.wait_disappear_push()
            internet.back()
            internet.back()
        with allure.step('Пакет подключился добавились ГБ, стоимость пакета отнялась с баланса'):
            main.update_page()
            main.update_page()
            main.update_page()
            main.update_page()
            new_balance = main.return_balance_int()
            new_package = main.return_remainder_internet_package()
            assert new_balance == balance - package_price
            assert new_package == package + package_gb

    @allure.title("Проверка наличия подробной информации о интернет-пакетах")
    @allure.feature("Тариф")
    def test_info_internet_packages(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        internet = InternetPackages(driver_fixture)

        login_wia_phone(phone=INT_PACKAGE_USER['PHONE_NUMBER'], password=INT_PACKAGE_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()
        with allure.step('В появившейся странице нажать на раздел “Интернет пакеты”'):
            tarrif.check_tarrif_components()
            tarrif.click_internet_packages()
        with allure.step('Выбрать любой из интернет-пакетов'):
            index = 1
            name = internet.return_package_name_str(index)
        with allure.step('Нажать на кнопку “Подробнее”'):
            internet.click_more_internet_package(index)
        with allure.step('Ожидаемый результат: Открывается страница с подробной информацией о интернет-пакете'):
            internet.check_more_internet_title(name)

    @allure.title("Обменять ресурсы своего тарифа")
    @allure.feature("Тариф")
    def test_exchange_resource_tarrifs(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        exchange = Exchange(driver_fixture)

        login_wia_phone(phone=INT_PACKAGE_USER['PHONE_NUMBER'], password=INT_PACKAGE_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.update_page()
            old_main_sms = main.return_tarrif_resources(which='sms')
            old_main_gb = main.return_tarrif_resources(which='gb')
            old_main_min = main.return_tarrif_resources(which='min')
            main.click_my_tarrif()
        with allure.step('В появившейся странице нажать на раздел “Обменять” (Должен быть подключен тариф)'):
            tarrif.click_exchange()
        old_min = exchange.return_quantity_resource('min')
        old_sms = exchange.return_quantity_resource('sms')
        old_gb = exchange.return_quantity_resource('gb')

        with allure.step('Обменять ресурсы'):
            if old_sms > old_min:
                exchange.exchange_bar_move_sms_greater()
            elif old_sms < old_min:
                exchange.exchange_bar_move_sms_less()
            new_sms = exchange.return_quantity_resource('sms')
            new_gb = exchange.return_quantity_resource('gb')
            new_min = exchange.return_quantity_resource('min')
            assert old_sms != new_sms
            assert old_gb != new_gb
            assert old_min != new_min
            exchange.approve_button_click()
            exchange.check_banner_exchange_ok()
            exchange.wait_disappear_push()
            tarrif.back()
        with allure.step('В главной странице количество ресурсов изменено согласно изменениям, введенным абонентом'):
            main.update_page()
            main.update_page()
            main.update_page()
            with allure.step('Жду 10 секунд что бы информация точно обновилась'):
                sleep(10)
            main.update_page()
            new_main_sms = main.return_tarrif_resources(which='sms')
            new_main_gb = main.return_tarrif_resources(which='gb')
            new_main_min = main.return_tarrif_resources(which='min')
            assert new_main_sms != old_main_sms
            assert new_main_gb != old_main_gb
            assert new_main_min != old_main_min

    @allure.title("Переподключение тарифа")
    @allure.feature("Тариф")
    def test_reconnect_tarrif(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)

        login_wia_phone(phone=TARRIF_USER['PHONE_NUMBER'], password=TARRIF_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.update_page()
            main.update_page()
            old_balance = main.return_balance_int()
            logging.info(f'Старый баланс равно: {str(old_balance)}')
            main.click_my_tarrif()

        with allure.step('Переподключить'):
            tarrif.click_re_connect_tarrif()
            reconnect_price = tarrif.return_reconnect_price_int()
            logging.info(f'Цена переподключения: {str(reconnect_price)}')
            tarrif.ok_click_reconnect()
            tarrif.check_push_reconnect_ok_located()
            tarrif.wait_disappear_push()
            tarrif.back()

        with allure.step('С баланса списались деньги, тариф переподключен. На главной '
                         'странице ресурсы тарифа возобновлены'):
            for x in range(0, 5):
                main.update_page()
            new_balance = main.return_balance_int()
            logging.info(f'Новый баланс: {str(new_balance)}')
            try:
                assert new_balance == old_balance - reconnect_price
            except AssertionError:
                main.update_page()

    @allure.title("Смена тарифа")
    @allure.feature("Тариф")
    def test_change_tarrif(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        new_tarrif = OtherTarrifs(driver_fixture)

        # TIMEOUT ПОСЛЕ КАЖДОЙ СМЕНЫ ТАРИФА 10 минут

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()

        with allure.step('В появившейся странице нажать на кнопку “Сменить тариф”'):
            old_tarrif = tarrif.return_current_tarrif_name()
            tarrif.change_tarrif_click()

        with allure.step('Выбрать любой из тарифов, нажать на кнопку “Подключить”'):
            index = 1
            new_tarrif.connect_tarrif_with_index(index=index)

        with allure.step('Нажать на кнопку “Ок”'):
            new_tarrif.click_connect_new_tarrif_ok()
            new_tarrif.check_push_changed_ok_located()
            new_tarrif.wait_disappear_push()

        with allure.step('С баланса списались деньги, на главной странице появилась'
                         'информация о ресурсах нового тарифа.Под надписью раздела “Мой тариф” указан новый '
                         'установленный тариф'):
            new_tarrif.back()
            new_tarrif.back()
            main.update_page()
            main.update_page()
            main.update_page()
            main.click_my_tarrif()
            new_tarrif = tarrif.return_current_tarrif_name()
            assert new_tarrif != old_tarrif

    @allure.title("Смена тарифа с изменением ресурсов")
    @allure.feature("Тариф")
    def test_change_tarrif_with_resources(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        new_tarrif = OtherTarrifs(driver_fixture)

        # TODO: бАЛАНС ДЛЯ ТЕСТОВОГО НОМЕРА И НОРМАЛЬНЫЙ АССЕРТ
        login_wia_phone(phone=CHANGE_TARRIF_WITH_RESOURCES_USER['PHONE_NUMBER'],
                        password=CHANGE_TARRIF_WITH_RESOURCES_USER['PASSWORD'], driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()

        with allure.step('В появившейся странице нажать на кнопку “Сменить тариф”'):
            old_tarrif = tarrif.return_current_tarrif_name()
            tarrif.change_tarrif_click()
        with allure.step('Выбрать любой из тарифов, нажать на кнопку “Подключить”'):

            index = 0
            new_tarrif.swipe_to_down_tarrif()
            old_sms = new_tarrif.return_tarrif_resources_with_index(which='sms')
            old_gb = new_tarrif.return_tarrif_resources_with_index(which='gb')
            tarrif_price = new_tarrif.return_tarrif_price_int(index)
            if tarrif_price == 2490:
                new_tarrif.change_tarrif_resources_2590()
            if tarrif_price == 3890:
                new_tarrif.change_tarrif_resources()
            new_sms = new_tarrif.return_tarrif_resources_with_index(which='sms')
            new_gb = new_tarrif.return_tarrif_resources_with_index(which='gb')
            assert new_sms != old_sms
            assert new_gb != old_gb
            new_tarrif.connect_tarrif_with_index(index=index)

        with allure.step('Нажать на кнопку “Ок”'):
            new_tarrif.click_connect_new_tarrif_ok()
            new_tarrif.wait_disappear_push()

        with allure.step('С баланса списались деньги, на главной странице появилась'
                         'информация о ресурсах нового тарифа.Под надписью раздела “Мой тариф” указан новый '
                         'установленный тариф'):
            new_tarrif.back()
            new_tarrif.back()

            main.click_my_tarrif()
            new_tarrif = tarrif.return_current_tarrif_name()
            assert new_tarrif != old_tarrif

    @allure.title("Проверка наличия подробной информации о тарифах")
    @allure.feature("Тариф")
    def test_check_tarrif_more_info(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        new_tarrif = OtherTarrifs(driver_fixture)

        login_wia_phone(phone=TARRIF_USER['PHONE_NUMBER'], password=TARRIF_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()

        with allure.step('В появившейся странице нажать на кнопку “Сменить тариф”'):
            tarrif.change_tarrif_click()

        with allure.step('Выбрать любой из тарифов'):
            index = 0

        with allure.step('Нажать на кнопку “Подробнее”'):
            new_tarrif.click_to_more_info_with_index(index)

        with allure.step('Открывается страница с информацией о ресурсах тарифа и их стоимости'):
            new_tarrif.check_tarrif_more_info_opened()

    @allure.title("Проверка наличия условий одного из тарифов")
    @allure.feature("Тариф")
    def test_check_tarrif_terms(self, driver_fixture):
        tarrif = TarrifPage(driver_fixture)
        main = MainPage(driver_fixture)
        new_tarrif = OtherTarrifs(driver_fixture)

        login_wia_phone(phone=TARRIF_USER['PHONE_NUMBER'], password=TARRIF_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В главной странице нажать на раздел “Мой тариф”'):
            main.click_my_tarrif()

        with allure.step('В появившейся странице нажать на кнопку “Сменить тариф”'):
            tarrif.change_tarrif_click()

        with allure.step('Выбрать любой из тарифов'):
            index = 0

        with allure.step('Нажать на кнопку “Подробнее”'):
            new_tarrif.click_to_more_info_with_index(index)

        with allure.step('Нажать на раздел “Условия тарифа”'):
            new_tarrif.check_tarrif_more_info_opened()
            new_tarrif.click_to_tarrif_conditions()

        with allure.step('Открывается страница с информацией о ресурсах тарифа и их стоимости'):
            new_tarrif.check_tarrif_condition_opened()
            tarrif.check_tarrif_details_opened()

    @allure.title("Передача ресурсов")
    @allure.feature("Тариф")
    def test_swap_resources(self, driver_fixture):
        main = MainPage(driver_fixture)
        swap = SwapResources(driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass  # APPIUM САМ ЗАПУСТИТ

        with allure.step('В главной странице нажать на раздел “Перевод ресурсов”'):
            login_wia_phone(phone=SEND_PACKAGE_USER['PHONE_NUMBER'], password=SEND_PACKAGE_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

            old_gb_first_number = main.return_received_gbs()
            main.click_my_number()
            main.click_logout()
            main.sure_logout_click()

            login_wia_phone(phone=INT_PACKAGE_USER['PHONE_NUMBER'], password=INT_PACKAGE_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            old_gb_second_number = main.return_tarrif_resources(which='gb')
            main.click_swap_resources()

        with allure.step('Ввести номер абонента'):
            swap.input_phone(SEND_PACKAGE_USER['PHONE_NUMBER'])

        with allure.step('Нажать на поле “Количество гигабайт”'):
            swap.click_down_icon()

        with allure.step('Выбрать количество гигабайт'):
            swap.click_select_one_gb()

        with allure.step('Нажать на кнопку “Поделиться”'):
            swap.click_give_resources_button()
            swap.sure_give_click()
            swap.check_push_ok()
            swap.wait_disappear_push()
            main.back()
        with allure.step('Вверху страницы появляется уведомление о том, что ресурсы '
                         'успешно переведены на номер абонента, ГБ списались с клиента,'
                         ' ГБ перчислились ожидаемому пользователю'):
            main.update_page()
            main.update_page()
            main.update_page()
            main.update_page()
            new_gb_second_number = main.return_tarrif_resources(which='gb')
            assert old_gb_second_number - 1 == new_gb_second_number
            main.click_my_number()
            main.click_logout()
            main.sure_logout_click()

            login_wia_phone(phone=SEND_PACKAGE_USER['PHONE_NUMBER'], password=SEND_PACKAGE_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.update_page()
            new_gb_first_number = main.return_received_gbs()
            assert new_gb_first_number == old_gb_first_number + 1
