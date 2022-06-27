import allure

from src.helpers.constants import ENVIRONMENT as ENV
from common_imports import *


class TarrifPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._tarrif_name = (MobileBy.ID, f'{ENV}:id/tariffNameTv')
        self._tarrif_condition = (MobileBy.ID, f'{ENV}:id/tariffService')
        self._exchange_resource = (MobileBy.XPATH, '//*[@text="Обменять"]')
        self._title_tarrif_services = (MobileBy.ID, f'{ENV}:id/titleTv')
        self._reconnect_tarrif_button = (MobileBy.ID, f'{ENV}:id/primaryButtonView')
        self._reconnect_price = (MobileBy.ID, f'{ENV}:id/descriptionTextView')
        self._reconnect_ok = (MobileBy.ID, 'android:id/button1')
        self._change_tarrif = (MobileBy.ID, f'{ENV}:id/changeTariffTv')
        self._tarrif_shimmer = (MobileBy.ID, f'{ENV}:id/shimmerTv')
        self._tarrif_info = (By.XPATH, '//*[@class="css-18v40m9 e1rym3c70"]')
        self._push_notification = (MobileBy.ID, f'{ENV}:id/titleTextView')

    def return_current_tarrif_name(self):
        name = self.return_element_text(*self._tarrif_shimmer)
        return name

    def check_tarrif_components(self):
        with allure.step('Обнаружить имя тарифа и описание'):
            self.assert_element_located(*self._tarrif_name)
            self.assert_element_located(*self._tarrif_condition)
            allure_screenshot(self.driver)

    def change_tarrif_click(self):
        with allure.step('Кликнуть на поменять тариф'):
            self.click(*self._change_tarrif)

    def check_tarrif_details_opened(self):
        with allure.step('Обнаружить страницу Условий Тарифа'):
            self.assert_text_inside_element(*self._title_tarrif_services, text='Условия тарифа')
            self.switch_to_webview(timeout=5)
            self.back_to_native_after_switch_wv()
            allure_screenshot(self.driver)

    def click_tarrif_details(self):
        with allure.step('Нажать на Условия Тарифа'):
            self.click(*self._tarrif_condition, unique=False, index=0)

    def click_internet_packages(self):
        with allure.step('Нажать на интернет пакеты'):
            self.swipe_until(*self._tarrif_condition, unique=False, index=3)
            self.click(*self._tarrif_condition, unique=False, index=3)

    def click_exchange(self):
        with allure.step('Нажать на обменять'):
            self.swipe_until(*self._exchange_resource)
            self.click(*self._exchange_resource)

    def click_re_connect_tarrif(self):
        with allure.step('Клик на переподключить тариф'):
            self.click(*self._reconnect_tarrif_button)

    def return_reconnect_price_int(self):
        price = self.return_element_text(*self._reconnect_price)
        allure_screenshot(self.driver)
        return int(re.findall(r'\d+', price)[0])

    def ok_click_reconnect(self):
        with allure.step('Нажать на подтвердить переподключеине'):
            self.click(*self._reconnect_ok)

    def check_push_reconnect_ok_located(self):
        with allure.step('Обнаружить пуш уведомление о том что тариф переподключен'):
            self.assert_element_located(*self._push_notification)
            allure_screenshot(self.driver)

    def wait_disappear_push(self):
        with allure.step('Подождать пока пропадет пуш уведомление'):
            self.wait_until_disappear(*self._push_notification, timeout=6)


class InternetPackages(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._package_price = (MobileBy.ID, f'{env}:id/costTextView')
        self._package_connect = (MobileBy.ID, f'{env}:id/connectButtonView')
        self._package_connect_ok = (MobileBy.ID, f'{env}:id/okButton')
        self._back_button = (MobileBy.ID, f'{env}:id/leftIconBv')
        self._more_info = (MobileBy.ID, f'{env}:id/moreInfoTextView')
        self._package_name_title = (MobileBy.ID, f'{env}:id/serviceName')
        self._title_internet_packages = (MobileBy.ID, f'{env}:id/internetServiceTitleTextView')
        self._push_notification = (MobileBy.ID, f'{env}:id/titleTextView')

    def return_package_price_int(self, index):
        price = self.return_element_text(*self._package_price, unique=False, index=index)
        return int(re.findall(r'\d+', price)[0])

    def return_package_gb(self, index):
        gb = self.return_element_text(*self._title_internet_packages, unique=False, index=index)
        return int(re.findall(r'\d+', gb)[0])

    def return_package_name_str(self, index):
        self.assert_element_located(*self._package_connect, timeout=6)
        name = self.return_element_text(*self._title_internet_packages, unique=False, index=index)
        allure_screenshot(self.driver)
        logging.info(name)
        logging.info(name)
        return name

    def click_internet_connect(self, index):
        with allure.step(f'Нажать на подключить {str(index)}-ый интернет пакет'):
            self.click(*self._package_connect, unique=False, index=index)

    def connect_package_ok(self):
        with allure.step('Подключить пакет ОК Клик'):
            self.click(*self._package_connect_ok)

    def check_push_internet_ok_located(self):
        with allure.step('Обнаружить пуш уведомление о том что инетнер пакет подключен'):
            self.assert_element_located(*self._push_notification, timeout=15)
            allure_screenshot(self.driver)

    def wait_disappear_push(self):
        with allure.step('Подождать пока пуш уведомление исчезнет'):
            self.wait_until_disappear(*self._push_notification, timeout=6)

    def click_more_internet_package(self, index):
        with allure.step('Кликнуть на подробнее об интернет пакете'):
            self.click(*self._more_info, unique=False, index=index)

    def check_more_internet_title(self, text):
        with allure.step('Обнаружить страницу "Подробнее об интернет пакете"'):
            self.assert_text_inside_element(*self._package_name_title, text=text)
            allure_screenshot(self.driver)

    def back_icon_click(self):
        with allure.step('Нажать на иконку " Назад"'):
            self.click(*self._back_button, timeout=10)


class Exchange(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._seek_bar = (MobileBy.ID, f'{env}:id/rangeSeekBar')
        self._min_quantity = (MobileBy.ID, f'{env}:id/minuteTv')
        self._sms_quantity = (MobileBy.ID, f'{env}:id/smsTv')
        self._gb_quantity = (MobileBy.ID, f'{env}:id/gbTv')
        self._approve_button = (MobileBy.ID, f'{env}:id/approveButtonView')
        self._cancel_button = (MobileBy.ID, f'{env}:id/cancelButtonView')
        self._push_notification = (MobileBy.ID, f'{env}:id/titleTextView')

    def check_seek_bar_enabled(self):
        with allure.step('Обнаружить что слайдер обмена ресурсов обнаружен'):
            self.assert_element_located(*self._seek_bar)
            allure_screenshot(self.driver)

    def exchange_bar_move_sms_less(self):

        self.swipe_with_coord(x=[502, 311], y=[1037, 1046])
        self.swipe_with_coord(x=[646, 711], y=[1040, 1040])

        #На сяоми
        # self.swipe_with_coord(x=[388, 466], y=[748, 737])
        # self.swipe_with_coord(x=[291, 194], y=[748, 739])

    def exchange_bar_move_sms_greater(self):
        self.swipe_with_coord(x=[317, 474], y=[1055, 1034])
        self.swipe_with_coord(x=[735, 600], y=[1037, 1040])

        # На сяоми
        # self.swipe_with_coord(x=[502, 350], y=[737, 739])
        # self.swipe_with_coord(x=[224, 293], y=[733, 733])

    def return_quantity_resource(self, which):
        allure_screenshot(self.driver)
        if which == 'sms':
            return int(re.findall(r'\d+', self.return_element_text(*self._sms_quantity))[0])
        elif which == 'min':
            return int(re.findall(r'\d+', self.return_element_text(*self._min_quantity))[0])
        elif which == 'gb':
            return int(re.findall(r'\d+', self.return_element_text(*self._gb_quantity))[0])
        else:
            logging.error('Выберите какой ресурс отобразить')

    def approve_button_click(self):
        with allure.step('Нажать на подвердить'):
            self.click(*self._approve_button)

    def cancel_button_click(self):
        with allure.step('Нажать на подключить'):
            self.click(*self._cancel_button)

    def wait_disappear_push(self):
        with allure.step('Подождать пока пуш уведомление исчезнет'):
            self.wait_until_disappear(*self._push_notification, timeout=6)

    def check_banner_exchange_ok(self):
        with allure.step('Обнаружить что пуш о том что обмен ресурсов успешно'):
            self.assert_element_located(*self._push_notification)
            allure_screenshot(self.driver)


class OtherTarrifs(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._tarrif_price = (MobileBy.ID, f'{env}:id/balanceTextView')
        self._connect_tarrif_button = (MobileBy.ID, f'{env}:id/connectButtonView')
        self._connect_new_tarrif_ok = (MobileBy.ID, 'android:id/button1')
        self._tarrif_name = (MobileBy.ID, f'{env}:id/changeAllTitleTv')
        self._tarrif_sms = (MobileBy.ID, f'{env}:id/smsTv')
        self._tarrif_min = (MobileBy.ID, f'{env}:id/minuteTv')
        self._tarrif_gb = (MobileBy.ID, f'{env}:id/gbTv')
        self._more_info = (MobileBy.ID, f'{env}:id/moreInfoCallAllButtonView')
        self._tarrif_name_more_info = (MobileBy.ID, f'{env}:id/shimmerTv')
        self._tarrif_conditions = (MobileBy.ID, f'{env}:id/tariffConditionView')
        self._condition_title = (MobileBy.ID, f'{env}:id/titleTv')
        self._push_notification = (MobileBy.ID, f'{env}:id/titleTextView')

    def return_tarrif_price_int(self, index):
        price = self.return_element_text(*self._tarrif_price, unique=False, index=index, timeout=10)
        allure_screenshot(self.driver)
        return int(price)

    def swipe_to_down_tarrif(self):
        with allure.step('Cвайп на последний тариф снизу'):
            self.swipe_with_coord(x=[347, 390], y=[1347, 183])
            self.swipe_with_coord(x=[347, 390], y=[1347, 183])
            sleep(1)

    # Нужно вызвать метод выше что бы заюзать метод ниже потому-что СВАЙП
    def connect_tarrif_with_index(self, index):
        with allure.step(f'Подключить {str(index)}-ый тариф'):
            self.swipe_until(*self._connect_tarrif_button, index=index)
            self.click(*self._connect_tarrif_button, unique=False, index=0)

    def click_to_more_info_with_index(self, index):
        with allure.step('Клик на подробнее о тарифе'):
            self.click(*self._more_info, unique=False, index=index)

    def check_tarrif_more_info_opened(self):
        with allure.step('Обнаружить что страница с подробной информацией о тарифе отображается'):
            self.assert_element_located(*self._tarrif_name_more_info)
            allure_screenshot(self.driver)

    def click_to_tarrif_conditions(self):
        with allure.step('Нажать на условия о тарифе'):
            self.click(*self._tarrif_conditions)

    def check_tarrif_condition_opened(self):
        with allure.step('Обнаружить страницу с информацией о тарифах'):
            self.assert_element_located(*self._condition_title)
            allure_screenshot(self.driver)

    def change_tarrif_resources(self):
        self.swipe_with_coord([532, 692], [911, 898])

    def change_tarrif_resources_2590(self):
        self.swipe_with_coord([526, 674], [877, 892])

    def click_connect_new_tarrif_ok(self):
        with allure.step('Нажать на ОК '):
            self.click(*self._connect_new_tarrif_ok)

    def return_tarrif_resources_with_index(self, which):
        if which == 'sms':
            return int(re.findall(r'\d+', self.return_element_text(*self._tarrif_sms))[0])
        elif which == 'min':
            return int(re.findall(r'\d+', self.return_element_text(*self._tarrif_min))[0])
        elif which == 'gb':
            return int(re.findall(r'\d+', self.return_element_text(*self._tarrif_gb))[0])
        else:
            logging.error('Выберите какой ресурс отобразить')

    def return_tarrif_name_with_index(self, index):
        return self.return_element_text(*self._tarrif_name, unique=False, index=index)

    def check_push_changed_ok_located(self):
        with allure.step('Обнаружить пуш в котором отображено сообщение об успехе'):
            self.assert_element_located(*self._push_notification)
            allure_screenshot(self.driver)

    def wait_disappear_push(self):
        with allure.step('Подождать пока исчезнет пуш уведомление'):
            self.wait_until_disappear(*self._push_notification, timeout=6)
