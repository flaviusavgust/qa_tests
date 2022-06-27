import allure

from common_imports import *
import re
from src.helpers.constants import ENVIRONMENT as ENV
from src.helpers.data_manipulator import full_phone_number_format, full_phone_number_main_page


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._push_title = (MobileBy.ID, f'{ENV}:id/titleTextView')
        self._loader_animation = (MobileBy.ID, f'{ENV}:id/lottieAnimationView')
        self._button_refill_balance = (MobileBy.ID, f'{ENV}:id/refillBalanceTv')
        self._user_phone_main_page = (MobileBy.ID, f'{ENV}:id/phoneNumberTv')
        self._my_tarrif = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="Мой тариф"]')
        self._auto_payments = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="Автоплатеж"]')
        self._roaming = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="Роуминг"]')
        self._qr_pay = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="QR оплата'
                                        f' в транспорте"]')
        self._swap_resources = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="Перевод '
                                                f'ресурсов"]')
        self._group_discount = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" '
                                                f'and @text="Выгодно вместе"]')
        self._store = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" '
                                       f'and @text="Магазин"]')
        self._shares = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="Акции Tele2"]')
        self._daily_packages = (MobileBy.XPATH, f'//*[@resource-id="{ENV}:id/primaryTextTv" and @text="Ежедневный '
                                                f'пакет"]')
        self._balance_sum = (MobileBy.ID, f'{ENV}:id/wholePartTv')
        self._internet_package_remainder = (MobileBy.ID, f'{ENV}:id/measureLeftTv')
        self._received_internet_balance = (MobileBy.ID, f'{ENV}:id/measureLeftTv')
        self._resources_text = (MobileBy.ID, f'{ENV}:id/leftTextTv')
        self._my_number = (MobileBy.ID, f'{ENV}:id/phoneNumberTv')
        self._action_account = (MobileBy.ID, f'{ENV}:id/actionTextView')
        self._ok_logout = (MobileBy.ID, 'android:id/button1')
        self._decline_invite = (MobileBy.ID, 'android:id/button2')
        self._main_menu_activity = (MobileBy.ID, f'{ENV}:id/primaryTextTv')
        self._stories_image = (MobileBy.ID, f'{ENV}:id/storiesImageView')
        self._pop_up_title = (MobileBy.ID, 'android:id/message')

    def update_page(self):
        with allure.step('Обновить страницу для изменения данных'):
            self.swipe_until_up(*self._balance_sum)
            sleep(1)
            self.swipe_with_coord(x=[803, 815], y=[277, 1185])
            sleep(1)

    def click_on_fill_balance(self):
        with allure.step('Нажать на кнопку "Пополнить баланс"'):
            self.click(*self._button_refill_balance)

    def check_user_authored(self, user_number):
        # Номер телефона должен быть в формате 7064100066
        with allure.step('Проверить что в главной странице отображается номер пользователя: {str(user_number)}'):
            self.assert_text_inside_element(*self._user_phone_main_page,
                                            text=full_phone_number_main_page(user_number))
            allure_screenshot(self.driver)

    def accept_invite_on_group(self):
        with allure.step('Принять приглашение в группу'):
            self.click(*self._ok_logout)

    def ok_pop_up_reminder(self):
        with allure.step('Нажать на ОК в pop-up напоминании оплате'):
            self.click(*self._ok_logout)

    def decline_invite_on_group(self):
        with allure.step('Отклонить приглашение в группу'):
            self.click(*self._decline_invite)

    def click_my_tarrif(self):
        with allure.step('Кликнуть на "Мой тариф" в главной странице'):
            self.swipe_until(*self._my_tarrif, timeout=3)
            self.click(*self._my_tarrif)

    def click_store(self):
        with allure.step('Кликнуть на "Магазин" в главной странице'):
            self.swipe_until(*self._store, timeout=3)
            self.click(*self._store)

    def click_auto_payments(self):
        with allure.step('Кликнуть на "Автоплатежи" в главной странице'):
            self.swipe_until(*self._auto_payments)
            self.click(*self._auto_payments)

    def click_roaming(self):
        with allure.step('Кликнуть на "Роумингу" в главной странице'):
            self.swipe_until(*self._roaming)
            self.click(*self._roaming)

    def click_qr_pay(self):
        with allure.step('Кликнуть на "QR pay" в главной странице'):
            self.swipe_until(*self._qr_pay)
            self.click(*self._qr_pay)

    def click_daily_package(self):
        with allure.step('Кликнуть на "Ежедневные пакеты" в главной странице'):
            self.swipe_until(*self._daily_packages)
            self.click(*self._daily_packages)

    def click_share_tele2(self):
        with allure.step('Кликнуть на "Акции Tele2" в главной странице'):
            self.swipe_until(*self._shares)
            self.click(*self._shares)

    def click_swap_resources(self):
        with allure.step('Кликнуть на "Обменять ресурсы"'):
            self.swipe_until(*self._swap_resources, timeout=3)
            self.click(*self._swap_resources)

    def click_group_discounts(self):
        with allure.step('Кликнуть на "Выгодно вместе"'):
            self.swipe_until(*self._group_discount, timeout=4)
            self.click(*self._group_discount)

    def click_my_number(self):
        with allure.step('Кликнуть на номер в главной странице'):
            self.click(*self._my_number, timeout=14)

    def wait_until_push_disappear(self):
        with allure.step('Подождать пока пропадет пуш'):
            self.element_find(*self._loader_animation, timeout=15)
            self.wait_until_disappear(*self._loader_animation, timeout=20)
            self.element_find(*self._push_title, timeout=20)
            self.wait_until_disappear(*self._push_title, timeout=15)

    def click_logout(self):
        with allure.step('Кликнуть на выйти из аккаунта в главной странице'):
            self.click(*self._action_account, unique=False, index=2)

    def sure_logout_click(self):
        with allure.step('Кликнуть на ВЫЙТИ подтверждение'):
            self.click(*self._ok_logout)

    # Return методы по хорошему нужно убрать из Page Class

    def return_balance_int(self):
        balance = self.return_element_text(*self._balance_sum)
        allure_screenshot(self.driver)
        return int(''.join(re.findall(r'\d+', balance)))

    def return_remainder_internet_package(self):
        remainder = self.return_element_text(*self._internet_package_remainder, unique=False, index=-1)
        return float((re.findall(r'\d+\.\d+', remainder)[0]))

    def return_received_gbs(self):
        received = self.return_element_text(*self._received_internet_balance, unique=False, index=-1)
        return float((re.findall(r'\d+\.\d+', received)[0]))

    def return_tarrif_resources(self, which):
        allure_screenshot(self.driver)
        if which == 'min':
            return int(re.findall(r'\d+', self.return_element_text(*self._resources_text, unique=False, index=0))[0])
        elif which == 'sms':
            return int(re.findall(r'\d+', self.return_element_text(*self._resources_text, unique=False, index=1))[0])
        elif which == 'gb':
            return int(re.findall(r'\d+', self.return_element_text(*self._resources_text, unique=False, index=2))[0])
        else:
            logging.error('Выберите какой ресурс отобразить')

    def check_remainder_pop_up_located(self, phone):
        with allure.step('Обнаружить pop-up уведомление о том что нужно пополнить абонентскую плату'):
            self.assert_text_inside_element(*self._pop_up_title, text=f'{full_phone_number_format(phone)} напоминает о '
                                                                      f'необходимости пополнить абонентскую плату')
            allure_screenshot(self.driver)


class Chapters(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._main = (MobileBy.ID, f'{ENV}:id/navigationMain')
        self._details = (MobileBy.ID, f'{ENV}:id/navigationDetail')
        self._services = (MobileBy.ID, f'{ENV}:id/navigationServices')
        self._help = (MobileBy.ID, f'{ENV}:id/navigationHelp')
        self._more = (MobileBy.ID, f'{ENV}:id/navigationMore')

    def click_main(self):
        with allure.step('Нажатие на "Главная" в меню навигации'):
            self.click(*self._main)

    def click_details(self):
        with allure.step('Нажатие на "Детализация" в меню навигации'):
            self.click(*self._details)

    def click_services(self):
        with allure.step('Нажатие на "Услуги" в меню навигации'):
            self.click(*self._services)

    def click_help(self):
        with allure.step('Нажатие на "Помощь" в меню навигации'):
            self.click(*self._help)

    def click_more(self):
        with allure.step('Нажатие на "Еще" в меню навигации'):
            self.click(*self._more)


class RoamingPopUp(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._welcome_text = (MobileBy.ID, f'{ENV}:id/welcomeTextTv')

    def check_welcome_text_located(self, country: str):
        with allure.step('Обнаружить привественный текст в Pop-up с приветсвием'):
            self.assert_text_inside_element(*self._welcome_text, text=f'{country}, Приветствует вас!')
            allure_screenshot(self.driver)


class RoamingMainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._roaming_country_text = (MobileBy.ID, f'{ENV}:id/roamingCountryTv')
        self._you_are_in_roaming_text = (MobileBy.ID, f'{ENV}:id/roamingStatusDescTv')
        self._turn_on_roaming_text = (MobileBy.ID, f'{ENV}:id/navigationCaption')

    def check_user_in_roaming_main_page(self, country: str):
        with allure.step('Обнаружить что открылась главная страница пользователя в роуминге'):
            self.assert_text_inside_element(*self._roaming_country_text, text=country)
            self.assert_element_located(*self._you_are_in_roaming_text)
            allure_screenshot(self.driver)

    def check_roaming_deactivated(self):
        with allure.step('Проверить что роуминг отключен'):
            self.assert_text_inside_element(*self._turn_on_roaming_text, text='Подключить роуминг')
            allure_screenshot(self.driver)

    def check_roaming_activated(self):
        with allure.step('Проверить что роуминг подключен'):
            self.assert_text_inside_element(*self._turn_on_roaming_text, text='Интернет-пакеты в роуминге')
            allure_screenshot(self.driver)
