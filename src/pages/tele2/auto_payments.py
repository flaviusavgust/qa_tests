from selenium.common.exceptions import TimeoutException
from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV
from src.helpers.data_manipulator import card_number_for_look_at_payment


class AutoPaymentsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._android_pop_up_title = (MobileBy.ID, 'android:id/alertTitle')
        self._title = (MobileBy.ID, f'{ENV}:id/titleTv')
        self._delete_card_icon = (MobileBy.ID, f'{ENV}:id/deleteCardIv')
        self._add_payments_button = (MobileBy.ID, f'{ENV}:id/addCardBtn')
        self._add_first_payment_button = (MobileBy.ID, f'{ENV}:id/addFirstBtn')
        self._add_new_card = (MobileBy.ID, f'{ENV}:id/addNewCardBtn')
        self._add_card_but = (MobileBy.ID, f'{ENV}:id/addCardBtn')
        self._autopayments_web_view = (By.XPATH, f'//*[text()="Виды автоплатежа"]')
        self._menu_icon = (MobileBy.ID, f'{ENV}:id/rightIconBv')
        self._my_cards = (MobileBy.ID, f'{ENV}:id/myCardsLl')
        self._what_is_auto_payment = (MobileBy.ID, f'{ENV}:id/aboutAutoCompleteTv')
        self._ok_button = (MobileBy.ID, f'android:id/button1')
        self._number_card = (MobileBy.ID, f'{ENV}:id/cardNumberTv')
        self._push = (MobileBy.ID, f'{ENV}:id/titleTextView')
        self._payments_name = (MobileBy.ID, f'{ENV}:id/nameTv')

        # Три точки справа от платежа
        self._menu_but_three_dot = (MobileBy.ID, f'{ENV}:id/menuIv')
        self._delete_three_dot = (MobileBy.ID, f'{ENV}:id/deleteTv')
        self._look_three_dot = (MobileBy.ID, f'{ENV}:id/lookTv')
        self._deny_three_dot = (MobileBy.ID, f'{ENV}:id/denyTv')
        # Страница просмотра после трех точек
        self._payments_type_three_dot = (MobileBy.ID, f'{ENV}:id/typeTv')
        self._payments_name_three_dot = (MobileBy.ID, f'{ENV}:id/nameTv')
        self._payments_number_type_three_dot = (MobileBy.ID, f'{ENV}:id/numberTypeTv')
        self._payments_number_three_dot = (MobileBy.ID, f'{ENV}:id/numberTv')
        self._payments_threshold_three_dot = (MobileBy.ID, f'{ENV}:id/thresholdTv')
        self._payments_sum_three_dot = (MobileBy.ID, f'{ENV}:id/sumTv')
        self._payments_card_three_dot = (MobileBy.ID, f'{ENV}:id/cardTv')
        self._back_icon = (MobileBy.ID, f'{ENV}:id/leftIconBv')

        # WebView elements
        # card
        self._google_play = (By.XPATH, '//*[@class="css-12jigj6 e1r1ca9c3"]')
        self._card_number_input = (MobileBy.XPATH, '//*[@text="10KZT"]')
        self._card_xpr_moth_input = (By.ID, 'cardExpiryMonth')
        self._card_xpr_year_input = (By.ID, 'cardExpiryYear')
        self._cvv_input = (By.ID, 'cardCode')
        self._name_input = (By.ID, 'cardHolder')
        self._pay_btn = (By.XPATH, '//*[@src="https://test-cdn.homebank.kz/epay2'
                                   '/4b97ba08108fd66f18ec36288b0e25d254a222338daf182d4436754fb29ae8b4.png"]')

        # Add new payments page
        self._with_period = (MobileBy.ACCESSIBILITY_ID, 'По периоду')
        self._with_threshold = (MobileBy.ACCESSIBILITY_ID, 'По порогу')
        self._to_other_number = (MobileBy.ID, f'{ENV}:id/otherNumberRb')
        self._input_name_payment = (MobileBy.ID, f'{ENV}:id/nameEt')
        self._input_phone_payment = (MobileBy.ID, f'{ENV}:id/phoneEt')
        self._input_period_payment = (MobileBy.ID, f'{ENV}:id/periodEt')
        self._next_time_period_payment = (MobileBy.ID, f'{ENV}:id/nextPeriodDateEt')
        self._input_threshold_payment = (MobileBy.ID, f'{ENV}:id/thresholdEt')
        self._input_sum_payment = (MobileBy.ID, f'{ENV}:id/sumEt')
        self._select_card_input = (MobileBy.ID, f'{ENV}:id/chooseCardEt')
        self._card_list = (MobileBy.ID, f'{ENV}:id/recyclerView')
        self._save_button = (MobileBy.ID, f'{ENV}:id/saveButton')
        self._push_bad = (MobileBy.ID, f'{ENV}:id/messageTextView')
        self._calendar_icon = (MobileBy.ID, f'{ENV}:id/calendarView')

    def assert_autopayments_opened(self):
        with allure.step('Обнаружить страницу " Автоплатежи"'):
            self.assert_text_inside_element(*self._title, text='Автоплатежи')
            allure_screenshot(self.driver)

    def check_autopayment_page_empty(self):
        with allure.step('Обнаружить страницу " Автоплатежи" с пустым списком платежей'):
            self.assert_element_located(*self._add_first_payment_button)
            allure_screenshot(self.driver)

    def refresh_page(self):
        with allure.step('Свайп для обновления страницы'):
            self.swipe_with_coord([538, 563], [234, 905])

    def assert_payments_main_page(self, name):
        with allure.step(f'Обнаружить автоплатеж по наименованию:{name}'):
            self.assert_text_inside_element(*self._payments_name, text=name, unique=False, index=-1)
            allure_screenshot(self.driver)

    def check_add_autopayment_button(self):
        with allure.step('Обнаружить Кнопку "Добавить автоплатеж"'):
            self.assert_text_inside_element(*self._add_first_payment_button, text='+ ДОБАВИТЬ АВТОПЛАТЕЖ')
            allure_screenshot(self.driver)

    # Страница меню три точки возле автоплатежа

    def delete_payments_with_index(self, index):
        with allure.step(f'Удалить {str(index)}-ый автоплатеж'):
            self.click(*self._menu_but_three_dot, unique=False, index=index)
            self.click(*self._delete_three_dot)
            self.click(*self._ok_button)

    def click_menu_button_three_dot_with_index(self, index):
        with allure.step(f'Кликнуть на иконку меню (три точки) {str(index)}-го автоплатежа'):
            self.click(*self._menu_but_three_dot, unique=False, index=index)

    def click_look_three_dot(self):
        with allure.step('Кликнуть на "Посмотреть" автоплатеж'):
            self.click(*self._look_three_dot)

    def click_deny_three_dot(self):
        with allure.step('Кликнуть на "Отмена" в меню'):
            self.click(*self._deny_three_dot)

    # Ассерт составляющих автоплатежа во вкладке просмотр автоплатежа
    def assert_payments_atr_at_look(self, payments_type, payments_name, payments_number_type,
                                    payments_number, payments_threshold, payments_sum, payments_card):

        attributes = [str(payments_type), str(payments_name), str(payments_number_type), str(payments_number),
                      str(payments_threshold), str(payments_sum), str(payments_card)]

        locators = [self._payments_type_three_dot, self._payments_name_three_dot, self._payments_number_type_three_dot,
                    self._payments_number_three_dot, self._payments_threshold_three_dot, self._payments_sum_three_dot,
                    self._payments_card_three_dot]

        with allure.step('Проверка составляющих автоплатежа'):
            for atr, loc in zip(attributes, locators):
                self.assert_text_inside_element(*loc, text=atr)
            allure_screenshot(self.driver)

    def click_back_icon(self):
        with allure.step('Кликнуть на иконку "Назад"'):
            self.click(*self._back_icon)

    def click_add_not_first_cart(self):
        with allure.step('Нажать на"Добавить новую карту"'):
            self.click(*self._add_card_but)

    def assert_three_dot_menu_closed(self):
        with allure.step('Проверить что меню (три точки) закрылось'):
            self.wait_until_disappear(*self._delete_three_dot, timeout=3)
            allure_screenshot(self.driver)

    def assert_push_payments_deleted(self):
        with allure.step('Обнаружить пуш уведомление о том что автоплатеж удален'):
            self.assert_text_inside_element(*self._push, text='Автоплатеж удален')
            allure_screenshot(self.driver)

    def assert_push_can_not_create_autopayments_limit(self):
        push_text = 'Достигнуто максимальное количество платежей по порогу'
        with allure.step(f'Обнаружить пуш уведомление о том что {push_text}'):
            self.assert_text_inside_element(*self._push_bad, text=push_text)
            allure_screenshot(self.driver)
            self.wait_until_disappear(*self._push_bad, timeout=6)

    def check_push_autopayment_with_that_period_exist(self):
        push_text = 'Подписка с указанным интервалом уже существует'
        with allure.step(f'Обнаружить пуш уведомление о том что {push_text}'):
            self.assert_text_inside_element(*self._push_bad, text=push_text)
            allure_screenshot(self.driver)
            self.wait_until_disappear(*self._push_bad, timeout=6)

    def return_card_number_with_index(self, index):
        text = self.return_element_text(*self._number_card, index=index, unique=False)
        return str(text)

    def click_add_new_cart(self):
        with allure.step('нажать на Добавить новую карту'):
            self.click(*self._add_new_card)

    def assert_card_deleted(self, number):
        with allure.step('Обнаружить что карта удалена'):
            self.assert_text_page_source(text=number, expected=False, timeout=7)
            allure_screenshot(self.driver)

    def assert_push_card_deleted(self, number):
        with allure.step('Обнаружить пуш уведомление о том что карта удалена'):
            self.assert_text_inside_element(*self._push, text=f'Карта {str(number)} удалена')
            allure_screenshot(self.driver)

    def delete_card_with_index(self, index):
        with allure.step(f'Удалить {str(index)}-ую карту'):
            self.click(*self._delete_card_icon, index=index, unique=False)

    def ok_button_click(self):
        with allure.step('Кликнуть на "ОК"'):
            self.click(*self._ok_button)

    def click_button_add_new_payments(self):
        with allure.step('Добавить новый автоплатежей'):
            try:
                self.click(*self._add_first_payment_button, timeout=3)
            except TimeoutException:
                self.click(*self._add_payments_button, timeout=3)

    def click_button_add_card(self):
        with allure.step('Кликнуть на добавить новую карту'):
            self.click(*self._add_first_payment_button)

    def click_menu_icon(self):
        with allure.step('Нажать на иконку "МЕНЮ"'):
            self.click(*self._menu_icon)

    def click_close_icon(self):
        with allure.step('Нажать на иконку "Закрыть"'):
            self.click(*self._menu_icon)

    def assert_menu_opened(self):
        with allure.step('Обнаружить что меню открыто'):
            self.assert_element_located(*self._my_cards)
            self.assert_element_located(*self._what_is_auto_payment)
            allure_screenshot(self.driver)

    def check_pop_up_max_payments_located(self):
        with allure.step('Обнаружить что pop_up с ошибкой о максимальном кол-во платежей отображается'):
            self.assert_text_inside_element(*self._android_pop_up_title,
                                            text='Достигнуто максимальное количество автоплатежей')
            allure_screenshot(self.driver)

    def click_my_cards(self):
        with allure.step('Кликнуть на "Мои карты"'):
            self.click(*self._my_cards)

    def assert_my_cards_opened(self):
        with allure.step('Обнаружить что страница "Мои карты" открыта'):
            self.assert_text_inside_element(*self._title, text='Мои карты')
            self.assert_element_located(*self._add_card_but)
            allure_screenshot(self.driver)

    def click_what_is_auto_payment(self):
        with allure.step('Кликнуть на "Что такое Автоплатежи"'):
            self.click(*self._what_is_auto_payment)

    def assert_what_is_auto_payment_opened(self):
        with allure.step('Обнаружить что страница "Что такое автоплатежи" октрыта:'):
            self.switch_to_webview()
            self.assert_element_located(*self._autopayments_web_view, timeout=6)
            self.back_to_native_after_switch_wv()
            allure_screenshot(self.driver)

    # Страница добавления нового автоплатежа

    def click_to_with_period(self):
        with allure.step('Кликнуть на "По периоду"'):
            self.click(*self._with_period)

    def click_to_with_threshold(self):
        with allure.step('Кликнуть на "По порогу"'):
            self.click(*self._with_threshold)

    def click_to_other_number(self):
        with allure.step('Кликнуть на "Другой номер"'):
            sleep(1)
            self.click(*self._to_other_number)

    def input_payment_name(self, name):
        with allure.step(f'Ввести наименование:{name} в поле ввода наименования автоплатежа'):
            self.input(*self._input_name_payment, text=str(name))

    def input_phone_payment(self, phone):
        with allure.step(f'Ввести номер:{str(phone)} в поле ввода номера автоплатежа'):
            self.input(*self._input_phone_payment, text=str(phone))

    def input_payment_threshold(self, amount):
        with allure.step(f'Ввести сумму:{str(amount)} в поле ввода порога для автоплатежа'):
            self.input(*self._input_threshold_payment, text=f'{str(amount)} ₸')

    def click_on_calendar_icon(self):
        with allure.step('Клик на иконку каледнаря'):
            self.click(*self._calendar_icon)

    def select_day_for_pay(self, days):
        locator_for_date = \
            (MobileBy.XPATH, f'//*[@text="{str(time_utils.return_date_for_calendar_autopayments(days))}"]')
        with allure.step(f'Выбор {str(days)}-го дня в календаре'):
            self.click(*locator_for_date)

    def input_periods_day(self, days):
        with allure.step(f'Ввести кол-во:{str(days)} в поле ввода дней для автоплатежа'):
            self.input(*self._input_period_payment, text=str(days))

    def input_payment_sum(self, amount):
        with allure.step(f'Ввести сумму:{str(amount)} в поле ввода суммы для автоплатежа'):
            self.input(*self._input_sum_payment, text=f'{str(amount)} ₸')

    def assert_next_payment_date(self, date):
        date = time_utils.return_date_for_payments(days=date)
        with allure.step('Обнаружить правильную дату для следующего автоплатежа'):
            self.assert_text_inside_element(*self._next_time_period_payment, text=date)

    def input_select_cart_payment(self):
        with allure.step('Кликнуть на оплата по карте'):
            self.click(*self._select_card_input)

    def select_card_with_index(self, index):
        with allure.step(f'Выбрать {str(index)}-ю карту для оплаты автоплатежа'):
            self.click(*self._card_list, unique=False, index=index)

    def click_save_button(self):
        self.swipe_until(*self._save_button, timeout=1)
        with allure.step('Кликнуть на "Сохранить"'):
            self.click(*self._save_button)

    def click_name(self):
        self.click(*self._input_name_payment)
        self.back()
        self.click(*self._input_period_payment)
        self.back()
        self.click(*self._input_sum_payment)
        self.back()

    def assert_push_payment_saved(self):
        with allure.step('Обнаружить пуш уведомление о том что автоплатеж сохранен'):
            self.assert_text_inside_element(*self._push, text='Успешно сохранено', timeout=13)
            allure_screenshot(self.driver)

    def assert_push_wrong_number(self):
        with allure.step('Обнаружить пуш уведомление о том что неправильный номер'):
            self.assert_text_inside_element(*self._push_bad, text='Услуга недоступна для абонентов других операторов')
            allure_screenshot(self.driver)


class AddCardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._input_card_number = (By.XPATH, '//input[@name="cardnumber"]')
        self._input_expiry_month = (By.XPATH, '//input[@name="ccmonth"]')
        self._input_expiry_year = (By.XPATH, '//input[@name="ccyear"]')
        self._input_cvv = (By.XPATH, '//input[@name="cvc"]')
        self._pay_button = (By.XPATH, '//*[@class="btn btn-primary va"]')
        self._card_added_text = (By.XPATH, "//*[text()='Оплата прошла успешно']")

    def switch_web(self):
        sleep(5)
        self.switch_to_webview(timeout=10)
        self.assert_element_located(*self._input_card_number, timeout=30)

    def input_card_number(self, card_number):
        with allure.step('Ввод номера карты для привязки'):
            self.input(*self._input_card_number, text=card_number)

    def input_expiry_month(self, month):
        with allure.step('Ввод месяца окончания действия карты для привязки'):
            self.input(*self._input_expiry_month, text=month)

    def input_expiry_year(self, year):
        with allure.step('Ввод года окончания действия карты для привязки'):
            self.input(*self._input_expiry_year, text=year)

    def input_cvv(self, cvv):
        with allure.step('Ввод cvv карты для привязки'):
            self.input(*self._input_cvv, text=cvv)

    def click_pay_button(self):
        with allure.step('Кликнуть на оплатить 10ТГ для привязки'):
            self.click(*self._pay_button)

    def check_card_added(self):
        sleep(5)
        allure_screenshot(self.driver)
        self.back_to_native_after_switch_wv()
        self.back()
        self.back()
        self.back()
