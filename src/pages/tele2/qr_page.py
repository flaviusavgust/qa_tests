import allure

from src.helpers.constants import ENVIRONMENT as ENV
from common_imports import *


class QrPayPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._verification_otp_text = (MobileBy.ID, f'{ENV}:id/verificationCodeInfo')

    def check_sms_info_located(self):
        with allure.step('Обнаружить текст об sms'):
            self.assert_element_located(*self._verification_otp_text, timeout=20)
            allure_screenshot(self.driver)
