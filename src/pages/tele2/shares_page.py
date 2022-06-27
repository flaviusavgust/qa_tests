from src.helpers.constants import ENVIRONMENT as ENV
from common_imports import *


class SharesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._share_card = (MobileBy.ID, f'{ENV}:id/stockCardView')

    def check_share_card(self):
        with allure.step('Обнаружить карточку акции об sms'):
            self.assert_element_located(*self._share_card)
            allure_screenshot(self.driver)