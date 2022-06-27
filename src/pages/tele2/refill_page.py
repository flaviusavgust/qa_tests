from selenium.common.exceptions import TimeoutException
from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class RefillPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._input_refill_sum = (MobileBy.ID, f'{ENV}:id/enterBalanceView')

    def input_refill_sum(self, sum):
        with allure.step(f'Ввести сумму: {str(sum)} в поле ввода суммы'):
            self.input(*self._input_refill_sum, text=str(sum))
