from common_imports import *
from src.helpers.constants import ENVIRONMENT as ENV
from src.helpers.data_manipulator import full_phone_number_format

class GroupDiscount(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._add_user_text = (MobileBy.ID, f'{ENV}:id/addParticipantTextView')
        self._create_group_button = (MobileBy.ID, f'{ENV}:id/createGroupContainer')
        # Номер который не овнера группа
        self._history_text = (MobileBy.ACCESSIBILITY_ID, 'История')
        self._members_text = (MobileBy.ACCESSIBILITY_ID, 'Участники')
        self._discount_cotainer = (MobileBy.ID, f'{ENV}:id/wheelViewContainer')
        self._number_not_main_text = (MobileBy.ID, f'{ENV}:id/userNumberTextView')
        self._invite_status_text = (MobileBy.ID, f'{ENV}:id/inviteStatus')
        self._remove_group_text = (MobileBy.ID, f'{ENV}:id/removeGroupButton')
        self._info_label = (MobileBy.ID, f'{ENV}:id/infoLabel')
        self._created_group = (MobileBy.ID, f'{ENV}:id/infoLabel')
        self._ok_button = (MobileBy.ID, 'android:id/button1')
        self._delete_icon = (MobileBy.ID, f'{ENV}:id/deleteImageView')
        self._rename_icon = (MobileBy.ID, f'{ENV}:id/editImageView')
        self._push_text = (MobileBy.ID, f'{ENV}:id/titleTextView')
        self._user_number_full = (MobileBy.ID, f'{ENV}:id/numberPartTextView')
        self._user_name = (MobileBy.ID, f'{ENV}:id/nameTextView')
        self._invites_text = (MobileBy.ID, f'{ENV}:id/officesMapView')
        self._details_text = (MobileBy.ID, f'{ENV}:id/detailButton')
        self._icon_whatsapp = (MobileBy.ID, f'{ENV}:id/whatsAppImageView')
        self._icon_remainder = (MobileBy.ID, f'{ENV}:id/remainderImageView')
        self._icon_calendar = (MobileBy.ID, f'{ENV}:id/calendarImageView')
        self._select_button_date = (MobileBy.ID, f'{ENV}:id/chooseButtonView')
        self._whatsapp_message = (MobileBy.ID, 'android:id/message')
        self._chrome_url_input = (MobileBy.ID, 'com.android.chrome:id/url_bar')
        self._discount_sum_text = (MobileBy.ID, f'{ENV}:id/discountPercentTextView')
        self._number_status_history_text = (MobileBy.ID, f'{ENV}:id/numberStatusTextView')

    def click_on_add_user(self):
        with allure.step('Нажать на "Добавить участника"'):
            self.click(*self._add_user_text, timeout=30)

    def click_on_details(self):
        with allure.step('Нажать на "Подробнее"'):
            self.click(*self._details_text, timeout=30)

    def click_on_history(self):
        with allure.step('Нажать на "История"'):
            self.click(*self._history_text, timeout=30)

    def click_on_members(self):
        with allure.step('Нажать на "Участники"'):
            self.click(*self._history_text, timeout=30)

    def click_on_create_group_button(self):
        with allure.step('Нажать на "Создать группу"'):
            self.click(*self._create_group_button, timeout=30)

    def click_on_remove_group(self):
        with allure.step('Нажать на "Удалить группу"'):
            self.click(*self._remove_group_text, timeout=30)

    def click_ok_remove_group(self):
        with allure.step('Нажать на подтвердить УДАЛИТЬ'):
            self.click(*self._ok_button)

    def click_on_leave_group(self):
        with allure.step('Нажать на "Покинуть группу"'):
            self.click(*self._remove_group_text)

    def click_ok_leave_group(self):
        with allure.step('Нажать на подтвердить УДАЛИТЬ'):
            self.click(*self._ok_button)

    def click_on_rename_member(self, member_index):
        with allure.step(f'Нажать на иконку смены имени {str(member_index)}-го пользователя'):
            self.click(*self._rename_icon, unique=False, index=member_index)

    def click_on_remove_icon_with_index(self, index):
        with allure.step(f'Нажать на иконку корзины справа от {str(index)}-го участника группы'):
            self.click(*self._delete_icon, index=index, unique=False)

    def click_on_whatsapp(self):
        with allure.step('Нажатие на иконку Whatsapp'):
            self.click(*self._icon_whatsapp)

    def click_on_reminder(self):
        with allure.step('Нажатие на иконку Уведомить пользователя'):
            self.click(*self._icon_remainder)

    def click_on_calendar_icon_history(self):
        with allure.step('Нажать на иконку Календаря в истории'):
            self.click(*self._icon_calendar)

    def click_select_day_calendar(self, first_date, second_date):
        locator = (MobileBy.XPATH, f'//*[@text="{first_date}" and @enabled="true"]')
        locator2 = (MobileBy.XPATH, f'//*[@text="{second_date}" and @enabled="true"]')
        with allure.step('Выбрать дату'):
            self.click(*locator, unique=False, index=-1)
            self.click(*locator2, unique=False, index=-1)

    def select_date_button_click(self):
        with allure.step('Нажать на кнопку "Выбрать"'):
            self.click(*self._select_button_date)

    def check_whatsapp_opened(self):
        with allure.step('Проверить что открылся чат с Whatsup'):
            self.assert_element_located(*self._chrome_url_input)
            allure_screenshot(self.driver)
            self.back()

    def check_push_user_deleted_from_group(self):
        with allure.step('Проверить что появилось пуш уведомление о том что пользователь исключен с группы'):
            self.assert_text_inside_element(*self._push_text, text='Участник успешно исключен с группы', timeout=30)
            allure_screenshot(self.driver)

    def check_user_deleted_from_group(self, phone):
        with allure.step('Проверить то что пользователь исключен с группы и не отображается в списке'):
            self.assert_text_page_source(expected=False, text=full_phone_number_format(phone))
            allure_screenshot(self.driver)

    def check_push_remind_sent(self):
        with allure.step('Проверить что появилось пуш уведомление о том что отправлено уведомление пользователю'):
            self.assert_text_inside_element(*self._push_text, text='Напоминание отправлено', timeout=30)
            allure_screenshot(self.driver)

    def sure_remove_user_click(self):
        with allure.step('Нажать на подтверждение удаление пользователя из группы'):
            self.click(*self._ok_button)

    def check_user_invite_sent(self, phone):
        with allure.step('Проверить что отображается, номера пользователя в списке и статус инвайта "Отправлено"'):
            self.assert_text_inside_element(*self._invite_status_text, text='Отправлено', timeout=30)
            self.assert_text_inside_element(*self._number_not_main_text, text=full_phone_number_format(phone))
            allure_screenshot(self.driver)

    def check_discount(self, percentage):
        with allure.step(f'Обнаружить сумму скидки в {str(percentage)}%'):
            self.assert_text_inside_element(*self._discount_sum_text, text=f'{str(percentage)}%')
            allure_screenshot(self.driver)

    def assert_group_did_not_created(self):
        self.assert_text_inside_element(*self._info_label, text='Вы еще не состоите в группе', timeout=10)

    def check_group_dont_created(self, timeout=30):
        with allure.step('Обнаружить текст о том что пользователь не состоит в группе'):
            self.assert_text_inside_element(*self._info_label, text='Вы еще не состоите в группе', timeout=timeout)
            self.assert_element_located(*self._create_group_button)
            allure_screenshot(self.driver)

    def check_group_discounts_loaded(self):
        with allure.step('Обнаружить что страница групповых скидов открылась'):
            self.is_displayed(*self._discount_cotainer, timeout=30)
            allure_screenshot(self.driver)

    def check_invites(self):
        with allure.step('Обнаружить активные приглашения'):
            self.assert_text_inside_element(*self._invites_text, text='Приглашения')
            allure_screenshot(self.driver)

    def check_user_not_in_group(self, phone):
        sleep(3)  # sleep for wait deleting from group
        members = len(self.elements_list(*self._user_number_full))
        for x in range(0, members):
            self.assert_text_inside_element(*self._user_number_full, unique=False, index=x, expected=False,
                                            text=full_phone_number_format(phone))

    def check_user_name(self, name, user_index):
        with allure.step('Обнаружить имя пользователя: в списке title имени пользователя'):
            self.is_displayed(*self._rename_icon)
            self.assert_text_inside_element(*self._user_name, unique=False, index=user_index,
                                            text=name, expected=True)
            allure_screenshot(self.driver)

    def check_history_user_added_to_group(self):
        with allure.step('Обнаружить историю добавленного пользователя'):
            self.assert_element_located(*self._number_status_history_text)
            allure_screenshot(self.driver)
            self.click(*self._members_text)

    def check_push_saved(self):
        with allure.step('Обнаружить пуш о том что, имя пользователя сохранене'):
            self.element_find(*self._push_text, timeout=30)
            self.assert_text_inside_element(*self._push_text, text='Сохранено')
            allure_screenshot(self.driver)


class AddUsePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._number_input = (MobileBy.ID, f'{ENV}:id/phoneEditTextView')
        self._invite_button = (MobileBy.ID, f'{ENV}:id/inviteToGroupButton')
        self._title_pop_up = (MobileBy.ID, f'{ENV}:id/invitationTitleTextView')
        self._invite_status_text = (MobileBy.ID, f'{ENV}:id/invitationStatusTextView')
        self._ok_button = (MobileBy.ID, 'android:id/button1')

    def input_phone_number(self, phone):
        with allure.step(f'Ввод номера{str(phone)} в поле ввода номера'):
            self.input(*self._number_input, text=phone)

    def invite_button_click(self):
        with allure.step('Нажать на ПРИГЛАСИТЬ'):
            self.click(*self._invite_button)

    def check_invite_sent_popup(self, phone):
        with allure.step(f'Проверка появления popup, о том что приглашение отправлено'):
            self.assert_text_inside_element(*self._title_pop_up, text='Приглашение отправлено', timeout=30)
            self.assert_text_inside_element(*self._invite_status_text,
                                            text=f'Приглашение успешно отправлено на номер '
                                                 f'{full_phone_number_format(phone)}')
            allure_screenshot(self.driver)

    def click_ok_pop_up(self):
        with allure.step('Нажать на ОК'):
            self.click(*self._ok_button, timeout=30)


class RenameUserPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._name_input = (MobileBy.ID, f'{ENV}:id/nameEditTextView')
        self._edit_name_save_button = (MobileBy.ID, f'{ENV}:id/saveEditUserNameTextView')

    def input_new_name(self, new_name):
        with allure.step(f'Ввод нового имени {str(new_name)} в поле ввода номера'):
            self.clear(*self._name_input)
            self.input(*self._name_input, text=new_name)

    def click_save(self):
        with allure.step(f'Нажать на кнопку "сохранить"'):
            self.click(*self._edit_name_save_button)
