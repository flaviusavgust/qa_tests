import allure
from src.pages.tele2.group_discount_page import GroupDiscount, AddUsePage
from src.pages.tele2.main_page import MainPage
from selenium.common.exceptions import TimeoutException


# Тут хранятся сетапы и тирдавны


class TeardownForGroupDiscounts:

    @staticmethod
    def remove_group(driver):
        group_discounts = GroupDiscount(driver)
        with allure.step('Teardown по удалению группы'):
            group_discounts.click_on_remove_group()
            group_discounts.click_ok_remove_group()
            group_discounts.check_group_dont_created()

    @staticmethod
    def leave_group(driver):
        group_discounts = GroupDiscount(driver)
        with allure.step('Teardown по выходу из группы'):
            group_discounts.click_on_leave_group()
            group_discounts.click_ok_leave_group()
            group_discounts.check_group_dont_created()


class SetupForGroupDiscounts:

    @staticmethod
    def create_group(driver):
        group_discounts = GroupDiscount(driver)
        main = MainPage(driver)

        with allure.step('Setup по созданию группы'):
            main.click_group_discounts()
            SetupForGroupDiscounts.delete_group_if_created(driver)
            group_discounts.click_on_create_group_button()

    @staticmethod
    def delete_group_if_created(driver):
        group_discounts = GroupDiscount(driver)

        with allure.step('Setup по удалению группы, если группа создана'):
            try:
                group_discounts.assert_group_did_not_created()
            except (AssertionError, TimeoutException, Exception):
                group_discounts.click_on_remove_group()
                group_discounts.click_ok_remove_group()

    @staticmethod
    def add_user_in_group(driver, phone):
        group_discounts = GroupDiscount(driver)
        add_user = AddUsePage(driver)
        with allure.step('Setup по добавлению участника в группу'):
            group_discounts.click_on_add_user()
            add_user.input_phone_number(phone)
            add_user.invite_button_click()
            add_user.click_ok_pop_up()
            group_discounts.check_user_invite_sent(phone=phone)

    @staticmethod
    def accept_invite_on_group(driver):
        main = MainPage(driver)

        with allure.step('Setup по принятию приглашения вступления в группу'):
            main.accept_invite_on_group()
            main.wait_until_push_disappear()
