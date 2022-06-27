import allure

from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV


class RoamingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._roaming_info_title = (MobileBy.ID, f'{ENV}:id/infoRoamingTitleTv')
        self._roaming_switcher = (MobileBy.ID, f'{ENV}:id/roamingSwitchView')
        self._ok_button = (MobileBy.ID, 'android:id/button1')
        self._push_text = (MobileBy.ID, f'{ENV}:id/titleTextView')

    def check_roaming_info_located(self):
        with allure.step('Обнаружить базовую тарификацию роуминга'):
            self.assert_element_located(*self._roaming_info_title)
            allure_screenshot(self.driver)

    def click_switcher_roaming(self):
        with allure.step('Нажать переключатель кнопку активации роуминга'):
            self.click(*self._roaming_switcher)

    def click_ok_activate_roaming(self):
        with allure.step('Нажать ОК подвердить активацию роуминга'):
            self.click(*self._ok_button)

    def check_push_roaming_activated_located(self):
        with allure.step('Обнаружить пуш уведомление об успешном подключении роуминга'):
            self.assert_text_inside_element(*self._push_text, text='Заявка на подключение услуги отправлена. '
                                                                   'Подключение произойдет в течение минуты.')
            allure_screenshot(self.driver)

    def check_push_roaming_deactivated_located(self):
        with allure.step('Обнаружить пуш уведомление об успешном отключении роуминга'):
            self.assert_text_inside_element(*self._push_text, text='Заявка на отключение услуги отправлена.Отключение '
                                                                   'произойдет в течение минуты.')
            allure_screenshot(self.driver)

    def check_roaming_deactivated(self):
        with allure.step('Обнаружить что роуминг деактивирован'):
            self.assert_text_inside_element(*self._roaming_switcher, text='ВЫКЛ')
            allure_screenshot(self.driver)

    def check_roaming_activated(self):
        with allure.step('Обнаружить что роуминг активирован'):
            self.assert_text_inside_element(*self._roaming_switcher, text='ВКЛ')
            allure_screenshot(self.driver)
