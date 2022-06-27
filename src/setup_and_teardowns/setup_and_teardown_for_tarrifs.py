import pytest
from src.pages.tele2.main_page import MainPage
from src.pages.tele2.auto_payments import AutoPaymentsPage

from src.helpers.constants import TestData as test_data
from common_imports import *


# Тут хранятся сетапы и тирдавны


class SetupForTarrif:

    @staticmethod
    def balance_checker(driver_fixture, min_balance):
        main_page = MainPage(driver_fixture)

        balance = main_page.return_balance_int()
        logging.info('')

        try:
            assert balance >= min_balance
            logging.info(f'Баланс пользователя соответствует минимальному порогу: {str(min_balance)}'
                         f' для выполнения теста!')
        except AssertionError:
            logging.error(f'Баланс на счете пользователя меньше минимального который вы указали: {str(min_balance)}'
                          f' Пополните БАЛАНС!!!')
            raise AssertionError

