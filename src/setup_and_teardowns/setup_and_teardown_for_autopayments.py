from src.pages.tele2.main_page import MainPage
from src.pages.tele2.auto_payments import AutoPaymentsPage, AddCardPage
from common_imports import *
from src.helpers.data_parser_and_test_data import GeneratedDataAutopayments


TEST_CARD = data_for_test()['TEST_CARD_FIRST']
TEST_CARD_CONSTANT = data_for_test()['TEST_CARD_CONSTANT']
TEST_DATA = data_for_test()['AUTOPAYMENTS_DATA']

# Тут хранятся сетапы и тирдавны


class SetupForAutopayments:

    @staticmethod
    def create_new_autopayment_threshold(driver_fixture):
        auto_p = AutoPaymentsPage(driver_fixture)

        auto_p.click_button_add_new_payments()
        auto_p.click_to_with_threshold()

        PAYMENT_NAME = GeneratedDataAutopayments.NAME

        auto_p.input_payment_name(PAYMENT_NAME)
        auto_p.input_payment_threshold(TEST_DATA['PAYMENT_THRESHOLD'])
        auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])
        auto_p.input_select_cart_payment()
        auto_p.select_card_with_index(int(TEST_DATA['CARD_FOR_PAYMENTS']))
        auto_p.click_save_button()
        auto_p.assert_push_payment_saved()
        auto_p.refresh_page()
        auto_p.assert_payments_main_page(name=PAYMENT_NAME)

    @staticmethod
    def create_new_autopayment_with_period(driver_fixture, payments_day=TEST_DATA['PAYMENT_DAY']):
        auto_p = AutoPaymentsPage(driver_fixture)

        auto_p.click_button_add_new_payments()
        auto_p.click_to_with_period()

        PAYMENT_NAME = GeneratedDataAutopayments.NAME

        auto_p.input_payment_name(PAYMENT_NAME)
        auto_p.input_periods_day(payments_day)
        auto_p.input_payment_sum(TEST_DATA['PAYMENT_SUM'])

        auto_p.input_select_cart_payment()
        auto_p.select_card_with_index(index=0)

        auto_p.click_save_button()

        auto_p.assert_push_payment_saved()
        auto_p.assert_payments_main_page(name=PAYMENT_NAME)

    @staticmethod
    def add_test_card(driver_fixture):
        main = MainPage(driver_fixture)
        auto_p = AutoPaymentsPage(driver_fixture)
        add_card = AddCardPage(driver_fixture)

        with allure.step("Setup по добавлению тестовой карты"):
            main.click_auto_payments()
            auto_p.click_menu_icon()
            auto_p.click_my_cards()
            auto_p.click_button_add_new_payments()
            auto_p.ok_button_click()
            add_card.switch_web()
            add_card.input_card_number(TEST_CARD['CARD_NUMBER'])
            add_card.input_expiry_month(TEST_CARD['EXP_MONTH'])
            add_card.input_expiry_year(TEST_CARD['EXP_YEAR'])
            add_card.input_cvv(TEST_CARD['CVC'])
            add_card.click_pay_button()
            add_card.check_card_added()
            sleep(15)


class TeardownForAutopayments:

    @staticmethod
    def delete_created_autopayments(driver_fixture):
        auto_p = AutoPaymentsPage(driver_fixture)

        sleep(1)
        auto_p.delete_payments_with_index(index=-1)
        auto_p.assert_push_payments_deleted()

    @staticmethod
    def delete_cart(driver_fixture, card_index, card):
        auto_p = AutoPaymentsPage(driver_fixture)

        with allure.step('Teardown теста по удалению добавленной карты'):
            auto_p.delete_card_with_index(card_index)
            auto_p.ok_button_click()
            auto_p.assert_push_card_deleted(card)
