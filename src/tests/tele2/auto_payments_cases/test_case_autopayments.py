from src.assert_functions.asserts_autpayments import assert_card_number
from src.pages.tele2.main_page import MainPage
from src.pages.tele2.auto_payments import AutoPaymentsPage, AddCardPage
from common_imports import *
from src.setup_and_teardowns.setup_and_teardown_for_autopayments import SetupForAutopayments as setup_
from src.setup_and_teardowns.setup_and_teardown_for_autopayments import TeardownForAutopayments as teardown_
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone
from src.helpers.data_parser_and_test_data import GeneratedDataAutopayments
from src.helpers.data_manipulator import card_number_for_look_at_payment, card_number_hidden
TEST_DATA = data_for_test()['AUTOPAYMENTS_DATA']
AUTOPAYMENT_USER = user_for_test()['AUTOPAYMENT_FIRST_USER']
CONSTANT_CARD = data_for_test()['TEST_CARD_CONSTANT']
TEST_CARD = data_for_test()['TEST_CARD_FIRST']


# TODO: Добавить teardown

class TestAutopayments:

    @allure.title("Проверка наличия раздела “Автоплатеж”")
    @allure.feature("Автоплатежи")
    def test_check_visibility_auto_payments(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('Открывается страница автоплатежа '):
            auto_p.assert_autopayments_opened()

    @allure.title("Проверка наличия меню")
    @allure.feature("Автоплатежи")
    def test_check_visibility_menu(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице в правом верхнем углу нажать на три линии'):
            auto_p.click_menu_icon()
        with allure.step(' Открывается меню с подразделами “Мои карты” и “Что такое автоплатеж”'):
            auto_p.assert_menu_opened()

    @allure.title("Проверка наличия раздела “Мои карты”")
    @allure.feature("Автоплатежи")
    def test_check_visibility_my_cards(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице в правом верхнем углу нажать на три линии'):
            auto_p.click_menu_icon()
        with allure.step('Нажать на подраздел “Мои карты”'):
            auto_p.click_my_cards()
        with allure.step(' Открывается страница со списком карт.'):
            auto_p.assert_my_cards_opened()

    @allure.title("Удаление карты в разделе “Мои карты”")
    @allure.feature("Автоплатежи")
    def test_check_delete_card(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        setup_.add_test_card(driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице в правом верхнем углу нажать на три линии'):
            auto_p.click_menu_icon()
        with allure.step('Нажать на подраздел “Мои карты”'):
            auto_p.click_my_cards()
        with allure.step('Нажать на значок корзины справа от номера карты'):
            card = card_number_hidden(card=TEST_CARD['CARD_NUMBER'])
            card_assert = assert_card_number(driver_fixture, card=card)
            auto_p.assert_text_page_source(card)

        with allure.step('Нажать на “Удалить”'):
            auto_p.delete_card_with_index(index=card_assert)
            auto_p.ok_button_click()
        with allure.step('В верхней части страницы появляется уведомление об успешном удалении карты. Автоплатежи '
                         'привязанные к удаленной карте также удаляются'):
            auto_p.assert_push_card_deleted(card)
            auto_p.assert_card_deleted(card)

    @allure.title("Проверка наличия раздела “Что такое автоплатеж”")
    @allure.feature("Автоплатежи")
    def test_check_visibility_what_is_auto_payments(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан'):
            pass  # APPIUM САМ ЗАПУСТИТ
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице в правом верхнем углу нажать на три линии'):
            auto_p.click_menu_icon()
        with allure.step('Нажать на подраздел “Что такое автоплатеж”'):
            auto_p.click_what_is_auto_payment()
        with allure.step('Открывается страница с описанием подробностей автоплатежа'):
            auto_p.assert_what_is_auto_payment_opened()

    @allure.id("59")
    @allure.title("Привязка карты к автоплатежам")
    @allure.label("owner", "admin")
    @allure.feature("Автоплатежи")
    def test_add_new_cart_autopayments_page(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)
        add_card = AddCardPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

        with allure.step("В главной странице нажать на раздел “Автоплатеж”"):
            main.click_auto_payments()

        with allure.step("В появившейся странице нажать на кнопку  “+ Добавить новую карту”"):
            auto_p.click_menu_icon()
            auto_p.click_my_cards()
            auto_p.click_button_add_new_payments()
            auto_p.ok_button_click()

        with allure.step("Ввести данные карты"):
            add_card.switch_web()
            add_card.input_card_number(TEST_CARD['CARD_NUMBER'])
            add_card.input_expiry_month(TEST_CARD['EXP_MONTH'])
            add_card.input_expiry_year(TEST_CARD['EXP_YEAR'])
            add_card.input_cvv(TEST_CARD['CVC'])

        with allure.step("Нажать на кнопку “Оплатить 10 KZT”"):
            add_card.click_pay_button()
            add_card.check_card_added()

        with allure.step("Ожидаемый результат: Появляется страница с квитанцией об оплате, карта появилась в списке "
                         "“Мои карты”, в странице автоплатежи исчезла кнопка добавить новую карту"):
            # ОЖИДАНИЕ потому что карта не сразу добавляется
            with allure.step('Жду 30 секунд что бы карта отобразилась'):
                sleep(30)
            main.click_auto_payments()
            auto_p.check_add_autopayment_button()
            auto_p.click_menu_icon()
            auto_p.click_my_cards()
            card = card_number_hidden(card=TEST_CARD['CARD_NUMBER'])

            auto_p.assert_text_page_source(card)
            card_assert = assert_card_number(driver_fixture, card=card)

            teardown_.delete_cart(driver_fixture, card_index=card_assert, card=card)

    @allure.title("Добавление автоплатежа (по порогу)")
    @allure.feature("Автоплатежи")
    def test_add_new_payments_threshold(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице нажать на кнопку  “+ Добавить автоплатеж”'):
            auto_p.click_button_add_new_payments()
        with allure.step('Ввести в поля корректные данные (в т.ч. поле порога для пополнения)'):
            auto_p.click_to_with_threshold()
            payments_name = GeneratedDataAutopayments.NAME
            auto_p.input_payment_name(payments_name)
            auto_p.input_payment_threshold(TEST_DATA['PAYMENT_THRESHOLD'])
            auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])

        with allure.step('Выбрать карту для оплаты'):
            auto_p.input_select_cart_payment()
            auto_p.select_card_with_index(int(TEST_DATA['CARD_FOR_PAYMENTS']))
        with allure.step('Нажать на кнопку “Сохранить”'):
            auto_p.click_save_button()
        with allure.step('Появится пуш уведомление об успешном добавлении автоплатежа,  '
                         'странице автоплатежей появляется новый автоплатеж по порогу'):
            auto_p.assert_push_payment_saved()
            auto_p.refresh_page()
            auto_p.assert_payments_main_page(name=payments_name)

        # teardown
        auto_p.delete_payments_with_index(index=-1)
        auto_p.assert_push_payments_deleted()

    @allure.title("Добавление автоплатежа (по периоду)")
    @allure.feature("Автоплатежи")
    def test_add_new_payments_period(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице нажать на кнопку  “+ Добавить автоплатеж”'):
            auto_p.click_button_add_new_payments()
            auto_p.click_to_with_period()
        with allure.step('Ввести в поля корректные данные (в т.ч. поле порога для пополнения)'):
            payments_name = GeneratedDataAutopayments.NAME

            auto_p.input_payment_name(payments_name)
            auto_p.input_periods_day(TEST_DATA['PAYMENT_DAY'])
            auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])
            auto_p.assert_next_payment_date(0)

        with allure.step('Выбрать карту для оплаты'):
            auto_p.input_select_cart_payment()
            auto_p.select_card_with_index(index=0)

        with allure.step('Нажать на кнопку “Сохранить”'):
            auto_p.click_save_button()

        with allure.step('Появится пуш уведомление об успешном добавлении автоплатежа,'
                         'странице автоплатежей появляется новый автоплатеж по порогу'):
            auto_p.assert_push_payment_saved()
            auto_p.refresh_page()
            auto_p.assert_payments_main_page(name=payments_name)

        # teardown
        auto_p.delete_payments_with_index(index=-1)
        auto_p.assert_push_payments_deleted()

    @allure.title("Добавление автоплатежа (по порогу, неверный номер)")
    @allure.feature("Автоплатежи")
    def test_add_new_payments_wrong_number(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()
        with allure.step('В появившейся странице нажать на кнопку  “+ Добавить автоплатеж”'):
            auto_p.click_button_add_new_payments()
            auto_p.click_to_with_threshold()

        with allure.step('В поле “Тип номера” выбрать “Другой номер”'):
            auto_p.click_to_other_number()

        with allure.step('Ввести в поля корректные данные (в т.ч. поле порога для пополнения)'):
            PAYMENT_NAME = GeneratedDataAutopayments.NAME
            auto_p.input_payment_name(PAYMENT_NAME)
            auto_p.input_phone_payment(TEST_DATA['WRONG_NUMBER'])
            auto_p.input_payment_threshold(TEST_DATA['PAYMENT_THRESHOLD'])
            auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])

        with allure.step('Выбрать карту для оплаты'):
            auto_p.input_select_cart_payment()
            auto_p.select_card_with_index(index=0)

        with allure.step('Нажать на кнопку “Сохранить”'):
            auto_p.click_save_button()
        with allure.step('Появится пуш уведомление об успешном добавлении автоплатежа,'
                         'странице автоплатежей появляется новый автоплатеж по порогу'):
            auto_p.assert_push_wrong_number()

    @allure.title("Просмотр автоплатежа")
    @allure.feature("Автоплатежи")
    def test_look_at_new_payments(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()

        # Setup что бы не сломать остальные тест
        PAYMENTS_NAME = GeneratedDataAutopayments.NAME
        setup_.create_new_autopayment_threshold(driver_fixture)

        with allure.step('В появившейся странице нажать на значок “три точки” '
                         'справа от названия любого из автоплатежей'):
            auto_p.click_menu_button_three_dot_with_index(0)
            auto_p.click_look_three_dot()
            auto_p.assert_payments_atr_at_look(payments_type='По порогу', payments_name=PAYMENTS_NAME,
                                               payments_number_type='Текущий номер',
                                               payments_number=AUTOPAYMENT_USER['PHONE_NUMBER'],
                                               payments_threshold=TEST_DATA['PAYMENT_THRESHOLD'],
                                               payments_sum=TEST_DATA['PAYMENT_SUM'],
                                               payments_card=card_number_for_look_at_payment
                                               (CONSTANT_CARD['CARD_NUMBER']))
            auto_p.click_back_icon()

        # teardown
        teardown_.delete_created_autopayments(driver_fixture)

    @allure.title("Выход из меню автоплатежа")
    @allure.feature("Автоплатежи")
    def test_deny_autopayments_menu(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()

        # Setup что бы не сломать остальные тест
        setup_.create_new_autopayment_threshold(driver_fixture)

        with allure.step(
                'В появившейся странице нажать на значок “три точки” справа от названия любого из автоплатежей'):
            auto_p.click_menu_button_three_dot_with_index(0)
            auto_p.click_deny_three_dot()
            auto_p.assert_three_dot_menu_closed()

        with allure.step('Ожидаемый результат: Происходит возврат на страницу автоплатежей'):
            auto_p.assert_autopayments_opened()

        teardown_.delete_created_autopayments(driver_fixture)

    @allure.title("Добавление второго автоплатежа по порогу (негативный сценарий)")
    @allure.feature("Автоплатежи")
    def test_add_second_autopayment(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('Запустить приложение Теле2 Казахстан будучи авторизованным'):
            pass
        with allure.step('В главной странице нажать на раздел “Автоплатеж”'):
            main.click_auto_payments()

        # Setup что бы создать автоплатеж
        setup_.create_new_autopayment_threshold(driver_fixture)
        main.back()
        main.click_auto_payments()

        with allure.step('Подключить второй автоплатеж по порогу'):
            PAYMENT_NAME = GeneratedDataAutopayments.NAME

            auto_p.click_button_add_new_payments()
            auto_p.click_to_with_threshold()
            auto_p.input_payment_name(PAYMENT_NAME)
            auto_p.input_payment_threshold(TEST_DATA['PAYMENT_THRESHOLD'])
            auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])

            auto_p.input_select_cart_payment()
            auto_p.select_card_with_index(index=int(TEST_DATA['CARD_FOR_PAYMENTS']))
            auto_p.click_save_button()

        with allure.step('Ожидаемый результат: Появляется ошибка о подключении автоплатежа в верхней части страницы'):
            auto_p.assert_push_can_not_create_autopayments_limit()
            auto_p.click_back_icon()

        # teardown
        teardown_.delete_created_autopayments(driver_fixture)

    @allure.id("177")
    @allure.title("Подключение автоплатежа с одинаковой периодичностью (негативный тест-кейс)")
    @allure.label("owner", "admin")
    @allure.feature("Автоплатежи")
    def test_add_autopayment_with_same_period(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)

        with allure.step("Запустить приложение Теле2 Казахстан будучи авторизованным"):
            login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
        with allure.step("В главной странице нажать на раздел “Автоплатеж”"):
            main.click_auto_payments()
            setup_.create_new_autopayment_with_period(driver_fixture)
        with allure.step("В появившейся странице нажать на кнопку  “Добавить автоплатеж”"):
            auto_p.click_button_add_new_payments()
        with allure.step('Нажать на "По периоду"'):
            auto_p.click_to_with_period()
        with allure.step("Ввести верные данные"):
            PAYMENT_NAME = GeneratedDataAutopayments.NAME

            auto_p.input_payment_name(PAYMENT_NAME)
            auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])
            auto_p.assert_next_payment_date(0)
        with allure.step('В поле "Периодичность" ввести такое же число как и в другом автоплатеже'):
            auto_p.input_periods_day(TEST_DATA['PAYMENT_DAY'])
        with allure.step('Нажать на "Сохранить" '):
            auto_p.input_select_cart_payment()
            auto_p.select_card_with_index(index=0)
            auto_p.click_save_button()
        with allure.step(
                "Выходит ошибка о том, что автоплатеж с выбранным интервалом уже существует. Автоплатеж не добавился"):
            auto_p.check_push_autopayment_with_that_period_exist()
            auto_p.back()

        teardown_.delete_created_autopayments(driver_fixture)

    @allure.id("72")
    @allure.title("Добавление более 5 автоплатежей (негативный тест-кейс)")
    @allure.label("suite", "Тест-кейсы для раздела “Автоплатеж”")
    @allure.label("owner", "admin")
    @allure.feature("Автоплатежи")
    def test_add_five_autopayment_with_period(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)
        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("Создать 5 автоплатежей"):
            main.click_auto_payments()
            setup_.create_new_autopayment_with_period(driver_fixture, payments_day=1)
            setup_.create_new_autopayment_with_period(driver_fixture, payments_day=2)
            setup_.create_new_autopayment_with_period(driver_fixture, payments_day=3)
            setup_.create_new_autopayment_with_period(driver_fixture, payments_day=4)
            setup_.create_new_autopayment_with_period(driver_fixture, payments_day=5)
        with allure.step("Подключить еще 1 автоплатеж по периоду"):
            auto_p.click_button_add_new_payments()
        with allure.step("Ожидаемый результат: Появляется ошибка о подключении автоплатежа в верхней части страницы"):
            auto_p.check_pop_up_max_payments_located()
            auto_p.ok_button_click()
        for x in range(0, 5):
            teardown_.delete_created_autopayments(driver_fixture)

    @allure.id("73")
    @allure.title("Добавление новой (второй) карты")
    @allure.label("suite", "Тест-кейсы для раздела “Автоплатеж”")
    @allure.label("owner", "admin")
    @allure.feature("Автоплатежи")
    def test_add_second_card(self, driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)
        add_card = AddCardPage(driver_fixture)

        login_wia_phone(phone=AUTOPAYMENT_USER['PHONE_NUMBER'], password=AUTOPAYMENT_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главной странице нажать на раздел “Автоплатеж”"):
            main.click_auto_payments()
        with allure.step("В появившейся странице нажать на три линии сверху справа"):
            auto_p.click_menu_icon()
        with allure.step("Нажать “Мои карты”"):
            auto_p.click_my_cards()
        with allure.step("Предисловие: Должна быть привязана одна карта"):
            card = card_number_hidden(card=CONSTANT_CARD['CARD_NUMBER'])
            auto_p.assert_text_page_source(card)
        with allure.step("Нажать “Добавить новую карту”"):
            auto_p.click_add_not_first_cart()
        with allure.step("Нажать “Ок”"):
            auto_p.ok_button_click()
        with allure.step('Добавить новую карту'):
            add_card.switch_web()
            add_card.input_card_number(TEST_CARD['CARD_NUMBER'])
            add_card.input_expiry_month(TEST_CARD['EXP_MONTH'])
            add_card.input_expiry_year(TEST_CARD['EXP_YEAR'])
            add_card.input_cvv(TEST_CARD['CVC'])
            add_card.click_pay_button()
            add_card.check_card_added()
            with allure.step('Жду 30 секунд что бы карта добавилась'):
                sleep(30)
            main.click_auto_payments()
            auto_p.click_menu_icon()
            auto_p.click_my_cards()
        with allure.step("Ожидаемый результат: Появляется страница с квитанцией об оплате, новая карта привязана"):
            card = card_number_hidden(card=TEST_CARD['CARD_NUMBER'])

            auto_p.assert_text_page_source(card)
            card_assert = assert_card_number(driver_fixture, card=card)

        teardown_.delete_cart(driver_fixture, card_index=card_assert, card=card)
