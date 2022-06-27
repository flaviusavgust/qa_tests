import time
from src.helpers.time_utils import return_date_for_calendar_autopayments
from src.pages.tele2.main_page import MainPage
from src.setup_and_teardowns.login_and_logout_methods import login_wia_phone, logout_from_account
from src.pages.tele2.group_discount_page import GroupDiscount, AddUsePage, RenameUserPage
from src.pages.tele2.services_page import ServicesPage
from src.setup_and_teardowns.setup_and_teardown_for_group_discounts import TeardownForGroupDiscounts, \
    SetupForGroupDiscounts
from common_imports import *
from src.helpers.data_parser_and_test_data import GeneratedDataGroupDisc

teardown_ = TeardownForGroupDiscounts
setup_ = SetupForGroupDiscounts

TEST_USERS = user_for_test()


# TODO: Добавить setup для удаление группы если не удалена

class TestGroupDiscount:

    @allure.id("123")
    @allure.title("Приглашение на вступление в группу")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_invite_and_create_group(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        add_user = AddUsePage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_FIRST_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_SECOND_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('В главном экране нажать на раздел "Выгодно вместе"'):
            main.click_group_discounts()
        with allure.step("Создать группу (если группы нет)"):
            setup_.delete_group_if_created(driver_fixture)
            group_discounts.click_on_create_group_button()
        with allure.step('Нажать на "Добавить участника"'):
            group_discounts.click_on_add_user()
        with allure.step("Ввести номер приглашаемого участника"):
            add_user.input_phone_number(SECOND_TEST_USER['PHONE_NUMBER'])
        with allure.step('Нажать на "Пригласить"'):
            add_user.invite_button_click()
        with allure.step("Группа успешно создана и приглашение отправлено"):
            add_user.check_invite_sent_popup(phone=SECOND_TEST_USER['PHONE_NUMBER'])
            add_user.click_ok_pop_up()
            group_discounts.check_user_invite_sent(phone=SECOND_TEST_USER['PHONE_NUMBER'])

        teardown_.remove_group(driver_fixture)

    @allure.id("127")
    @allure.title("Удаление участника из группы организатором")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_delete_from_group_by_owner(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_THIRD_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_FOURTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        main.click_group_discounts()
        setup_.add_user_in_group(phone=SECOND_TEST_USER['PHONE_NUMBER'], driver=driver_fixture)
        main.back()
        logout_from_account(driver_fixture)
        login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        setup_.accept_invite_on_group(driver_fixture)
        logout_from_account(driver_fixture)

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('В главном экране нажать на раздел "Выгодно вместе"'):
            main.click_group_discounts()
        with allure.step("Нажать на иконку удаления участника справа от номера"):
            group_discounts.click_on_remove_icon_with_index(index=0)
        with allure.step("Нажать на кнопку 'Удалить'"):
            group_discounts.sure_remove_user_click()
        with allure.step('Появляется пуш уведомление о том что пользователь удален из группы'):
            group_discounts.check_push_user_deleted_from_group()
            group_discounts.check_user_not_in_group(SECOND_TEST_USER['PHONE_NUMBER'])

    @allure.id("131")
    @allure.title("Выход участника из группы, инициированный участником")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_leave_group_by_member(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_THIRD_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_FOURTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)
        main.click_group_discounts()
        setup_.add_user_in_group(phone=SECOND_TEST_USER['PHONE_NUMBER'], driver=driver_fixture)
        main.back()
        logout_from_account(driver_fixture)

        login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        setup_.accept_invite_on_group(driver_fixture)

        with allure.step("В главном экране нажать на раздел 'Выгодно вместе'"):
            main.click_group_discounts()
        with allure.step('Нажать на "Покинуть группу" в появившейся странице'):
            group_discounts.click_on_leave_group()
        with allure.step('Нажать на "Покинуть"'):
            group_discounts.click_ok_leave_group()
        with allure.step("Участник успешно покинул группу. Организатор и если есть остальные"
                         " участники получают смс о том, что один из участников "
                         "покинул группу + уведомление о понижении скидки."):
            group_discounts.check_group_dont_created()
            group_discounts.back()
            logout_from_account(driver_fixture)

            login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)

            main.click_group_discounts()
            group_discounts.check_user_not_in_group(SECOND_TEST_USER['PHONE_NUMBER'])

    @allure.id("176")
    @allure.title("Отклонение приглашения участником")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_deny_group_invite(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_SIXTH_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_EIGHT_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        setup_.create_group(driver_fixture)

        with allure.step("Организатору отправить приглашение участнику"):
            setup_.add_user_in_group(phone=SECOND_TEST_USER['PHONE_NUMBER'], driver=driver_fixture)
            main.back()
            logout_from_account(driver_fixture)

        with allure.step('Участнику нажать на "Отклонить" в уведомлении'):
            login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.decline_invite_on_group()
            main.click_group_discounts()
            group_discounts.check_invites()
            group_discounts.back()
            logout_from_account(driver_fixture)

        with allure.step("Приглашение успешно отклонено"):
            login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.click_group_discounts()
            group_discounts.check_user_invite_sent(phone=SECOND_TEST_USER['PHONE_NUMBER'])
        teardown_.remove_group(driver_fixture)

    @allure.id("171")
    @allure.title("Смена имени участника, инициированная организатором")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_change_name_by_owner(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        rename = RenameUserPage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_NINTH_USER']
        MEMBER_NAME = GeneratedDataGroupDisc.FAKE_NAME
        MEMBER_INDEX = 1

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('В главном экране нажать на раздел "Выгодно вместе"'):
            main.click_group_discounts()
        with allure.step("Нажать на иконку смены имени"):
            group_discounts.click_on_rename_member(MEMBER_INDEX)
        with allure.step("Ввести новое имя"):
            rename.input_new_name(MEMBER_NAME)
        with allure.step('Нажать на "Сохранить"'):
            rename.click_save()
        with allure.step("В верхней части страницы появляется уведомление о смене имени, имя успешно изменено"):
            group_discounts.check_push_saved()
            group_discounts.check_user_name(name=MEMBER_NAME, user_index=MEMBER_INDEX)

    @allure.id("170")
    @allure.title("Смена имени участника, инициированная участником")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_change_name_by_member(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        rename = RenameUserPage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_TENTH_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_NINTH_USER']
        MEMBER_NAME = GeneratedDataGroupDisc.FAKE_NAME
        MEMBER_INDEX = 1

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step('В главном экране нажать на раздел "Выгодно вместе"'):
            main.click_group_discounts()
        with allure.step("Нажать на иконку смены имени одного из участников"):
            group_discounts.click_on_rename_member(0)
        with allure.step("Ввести новое имя"):
            rename.input_new_name(MEMBER_NAME)
        with allure.step('Нажать на "Сохранить"'):
            rename.click_save()
        with allure.step("В верхней части страницы появляется уведомление о сохранении смены имени, имя участника "
                         "успешно изменено"):
            group_discounts.check_push_saved()
            group_discounts.check_user_name(name=MEMBER_NAME, user_index=MEMBER_INDEX)
            group_discounts.back()
            logout_from_account(driver_fixture)
            login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.click_group_discounts()
            group_discounts.check_group_discounts_loaded()
            group_discounts.check_user_name(name=MEMBER_NAME, user_index=MEMBER_INDEX)

    @allure.id("169")
    @allure.title("Открытие страницы подробной информации об услуге")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_more_about_group_discounts(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        services = ServicesPage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_ELEVENTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)
        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            main.click_group_discounts()
        with allure.step("Нажать на \"Подробнее\" в появившейся странице"):
            group_discounts.click_on_details()
        with allure.step("Открывается страница с подробностями услуги"):
            services.check_group_discounts_services_page_opened()

    @allure.id("175")
    @allure.title("Перейти к чату в Whatsapp с участником группы")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_go_to_whatsapp(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_TENTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            main.click_group_discounts()
        with allure.step("Нажать на иконку Whatsapp рядом с именем одного из участников"):
            group_discounts.click_on_whatsapp()
        with allure.step("Открывается Whatsapp c чатом с выбранным участником"):
            group_discounts.check_whatsapp_opened()

    @allure.id("132")
    @allure.title("Повышение скидки в связи с увеличением кол-ва участников в 2")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_rise_discount_price_depends_on_new_person(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        add_user = AddUsePage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['TARRIF_USER']
        SECOND_TEST_USER = TEST_USERS['INTERNET_PACKAGE_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            main.click_group_discounts()
        with allure.step("Нажать на \"Добавить участника\""):
            group_discounts.click_on_add_user()
        with allure.step("Ввести номер приглашаемого участника"):
            add_user.input_phone_number(SECOND_TEST_USER['PHONE_NUMBER'])
        with allure.step("Нажать на \"Пригласить\""):
            add_user.invite_button_click()
        with allure.step("Участнику принять приглашение"):
            add_user.check_invite_sent_popup(phone=SECOND_TEST_USER['PHONE_NUMBER'])
            add_user.click_ok_pop_up()
            group_discounts.check_user_invite_sent(phone=SECOND_TEST_USER['PHONE_NUMBER'])
            group_discounts.back()
            logout_from_account(driver_fixture)
            login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.accept_invite_on_group()
            main.wait_until_push_disappear()
        with allure.step("Участник успешно присоединился к группе, скидка увеличена до 5/10/15%"):
            with allure.step('Жду 30 секунд что бы процент скидки обновился в биллинге и это отобразилось на странице'):
                time.sleep(30)
            main.click_group_discounts()
            group_discounts.check_discount(5)

        teardown_.leave_group(driver_fixture)

    @allure.id("172")
    @allure.title("Просмотр истории с датой по умолчанию")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_show_history_with_default_period(self, driver_fixture):
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_THIRTEENTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):

            setup_.create_group(driver_fixture)
        with allure.step("Перейти в раздел \"История\""):
            group_discounts.click_on_history()
        with allure.step("Открывается страница с историей за срок, установленный по умолчанию"):
            group_discounts.check_history_user_added_to_group()

        teardown_.remove_group(driver_fixture)

    @allure.id("173")
    @allure.title("Просмотр истории со сменой даты")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_change_time_and_check_history(self, driver_fixture):
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_THIRTEENTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            setup_.create_group(driver_fixture)
        with allure.step("Перейти в раздел \"История\""):
            group_discounts.click_on_history()
        with allure.step("Нажать на иконку календаря"):
            group_discounts.click_on_calendar_icon_history()
        with allure.step("Установить период истории"):
            group_discounts.click_select_day_calendar(first_date=return_date_for_calendar_autopayments(0),
                                                      second_date=return_date_for_calendar_autopayments(-3))
        with allure.step("Нажать на \"Выбрать\""):
            group_discounts.select_date_button_click()
        with allure.step("Открывается страница с историей за установленный срок"):
            group_discounts.check_history_user_added_to_group()

        teardown_.remove_group(driver_fixture)

    @allure.id("174")
    @allure.title("Отправление напоминания участнику")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_send_remind_to_member(self, driver_fixture):
        group_discounts = GroupDiscount(driver_fixture)
        main = MainPage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_TENTH_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_NINTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            main.click_group_discounts()

        with allure.step("Нажать на иконку уведомления рядом с именем одного из участников"):
            group_discounts.click_on_reminder()

        with allure.step("Появляется пуш уведомление о том что уведомление отправлено"):
            group_discounts.check_push_remind_sent()
            group_discounts.back()
            logout_from_account(driver_fixture)
            login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.check_remainder_pop_up_located(phone=FIRST_TEST_USER['PHONE_NUMBER'])
            main.ok_pop_up_reminder()

    @allure.id("130")
    @allure.title("Отключение услуги в связи с удалением группы организатором")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_delete_group_by_owner(self, driver_fixture):
        group_discounts = GroupDiscount(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['GROUP_DISC_FOURTEENTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            setup_.create_group(driver_fixture)
        with allure.step("Нажать на \"Удалить группу\" в появившейся странице"):
            group_discounts.click_on_remove_group()
        with allure.step("Нажать на \"Удалить\""):
            group_discounts.click_ok_remove_group()
        with allure.step("Группа успешно удалена. Организатор и участники получают уведомлении об отключении услуги"):
            group_discounts.check_group_dont_created()

    @allure.id("126")
    @allure.title("Добавление участника с несписанным тф")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_add_user_with_unwritten_tarrif(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        add_user = AddUsePage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['TARRIF_USER']
        SECOND_TEST_USER = TEST_USERS['GROUP_DISC_FIFTEENTH_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            main.click_group_discounts()
        with allure.step("Нажать на \"Добавить участника\""):
            group_discounts.click_on_add_user()
        with allure.step("Ввести номер участника с тарифом, где АП несписана"):
            add_user.input_phone_number(SECOND_TEST_USER['PHONE_NUMBER'])
        with allure.step("Нажать на \"Пригласить\""):
            add_user.invite_button_click()
        with allure.step("Участнику принять предложение"):
            add_user.check_invite_sent_popup(phone=SECOND_TEST_USER['PHONE_NUMBER'])
            add_user.click_ok_pop_up()
            group_discounts.check_user_invite_sent(phone=SECOND_TEST_USER['PHONE_NUMBER'])
            group_discounts.back()
            logout_from_account(driver_fixture)
            login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.accept_invite_on_group()
            main.wait_until_push_disappear()
        with allure.step("Участник успешно добавлен, скидка не увеличилась в связи с несписанной АП у участника"):
            with allure.step('Жду 40 секунд для того что бы скидка точно отобразилась в странице скидки'):
                time.sleep(40)
            main.click_group_discounts()
            group_discounts.check_discount(0)

        teardown_.leave_group(driver_fixture)

    @allure.id("125")
    @allure.title("Добавление участника со списанным тф")
    @allure.label("suite", "Групповые скидки")
    @allure.label("owner", "admin")
    @allure.feature("Выгодно вместе")
    def test_add_user_with_written_tarrif(self, driver_fixture):
        main = MainPage(driver_fixture)
        group_discounts = GroupDiscount(driver_fixture)
        add_user = AddUsePage(driver_fixture)

        FIRST_TEST_USER = TEST_USERS['TARRIF_USER']
        SECOND_TEST_USER = TEST_USERS['INTERNET_PACKAGE_USER']

        login_wia_phone(phone=FIRST_TEST_USER['PHONE_NUMBER'], password=FIRST_TEST_USER['PASSWORD'],
                        driver_fixture=driver_fixture)

        with allure.step("В главном экране нажать на раздел \"Выгодно вместе\""):
            main.click_group_discounts()
        with allure.step("Нажать на \"Добавить участника\""):
            group_discounts.click_on_add_user()
        with allure.step("Ввести номер участника с тарифом, где АП списана"):
            add_user.input_phone_number(SECOND_TEST_USER['PHONE_NUMBER'])
        with allure.step("Нажать на \"Пригласить\""):
            add_user.invite_button_click()
        with allure.step("Участнику принять предложение"):
            add_user.click_ok_pop_up()
            group_discounts.check_user_invite_sent(phone=SECOND_TEST_USER['PHONE_NUMBER'])
            group_discounts.back()
            logout_from_account(driver_fixture)
            login_wia_phone(phone=SECOND_TEST_USER['PHONE_NUMBER'], password=SECOND_TEST_USER['PASSWORD'],
                            driver_fixture=driver_fixture)
            main.accept_invite_on_group()
            main.wait_until_push_disappear()
        with allure.step("Участник успешно добавлен, скидка увеличилась до 5/10/15%"):
            with allure.step('Жду 50 секунд что бы значение скидки отобразилось'):
                time.sleep(50)
            main.click_group_discounts()
            group_discounts.check_discount(5)

        teardown_.leave_group(driver_fixture)
