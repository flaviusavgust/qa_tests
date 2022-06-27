import logging
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_actions import PointerInput
from src.helpers.constants import WEBVIEW
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    ElementNotVisibleException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.touch_action = TouchAction(driver)
        self.actions = ActionChains(driver)

    def launch_app(self):
        self.driver.launch_app()

    def element_find(self, *locator, timeout=10):
        """
        Функция поиска элемента.
        Используйте оператор распаковки * для указания локатор
        :param locator: locator
        :param timeout: int
        :return: the first element which matches the locator
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)

        except TimeoutException:
            logging.error(f"Не удается найти элемент - {str(locator)}")
            raise TimeoutException("Не удалось найти элемент : %s" % str(locator))

        except Exception:
            logging.error('Что-то пошло не так при поиске элемента, но это не TimeoutException!!')
            raise Exception()

        finally:
            logging.info(f"Успех при поиске элемента - {str(locator)}")

    def elements_find(self, *locator, timeout=10, index):
        """
        Функция поиска элементов.
        Используйте оператор распаковки * для указания локатора
        :param locator: locator
        :param timeout: int
        :param index: int
        :return: the list of elements which matches the locator
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)[index]

        except TimeoutException:
            logging.error(f"Не удается найти элемент - {str(locator)}")
            raise TimeoutException("Не удалось найти элемент : %s" % str(locator))

        except Exception:
            logging.error('Что-то пошло не так при поиске элемента, но это не TimeoutException!!')
            raise Exception('Что-то пошло не так при поиске элемента, но это не TimeoutException!!')

        finally:
            logging.info(f"Успех при поиске элементов - {str(locator)}")

    def elements_list(self, *locator, timeout=10):
        """
        Функция возвращает массив элементов.
        Используйте оператор распаковки * для указания локатора
        :param locator: locator
        :param timeout: int
        :param index: int
        :return: the list of elements which matches the locator
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)

        except TimeoutException:
            logging.error(f"Не удается найти элемент - {str(locator)}")
            raise TimeoutException("Не удалось найти элемент : %s" % str(locator))

        except Exception:
            logging.error('Что-то пошло не так при поиске элемента, но это не TimeoutException!!')
            raise Exception('Что-то пошло не так при поиске элемента, но это не TimeoutException!!')

        finally:
            logging.info(f"Успех при поиске элементов - {str(locator)}")

    def is_displayed(self, *locator, timeout=7, unique=True, index=0):
        """
        Функция проверки отображения и наличия элемента или элементов.
        Используйте оператор распаковки * для указания локатора
        НЕ assert ФУНКЦИЯ!! использовать только для элементов которые не имеют значения на результаты теста!
        :param locator: locator
        :param timeout: int
        :param unique: bool
        :return: bool
        :param index: int
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(locator))

        if unique:
            self.element_find(*locator).is_displayed()
        if not unique:
            return self.elements_find(*locator, index=index).is_displayed()

    def click(self, *locator, timeout=7, unique=True, index=0):
        """
        Функция клика на элемент.
        Используйте оператор распаковки * для указания локатора
        :param locator: locator
        :param timeout: int
        :param unique: bool
        :return: click element
        :param index: int
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(locator))
        try:
            if unique:
                self.element_find(*locator).click()
            if not unique:
                self.elements_find(*locator, index=index).click()
        except ElementClickInterceptedException:
            logging.error('Элемент не кликабельный в момент клика')
            raise ElementClickInterceptedException('Элемент не кликабельный в момент клика')
        except ElementNotVisibleException:
            logging.error('Элемент не отображается, но имеется в DOM')
            raise ElementNotVisibleException('Элемент не отображается, но имеется в DOM')
        except Exception:
            logging.error('Что-то пошло не так при клике на элемент....')
            raise Exception('Что-то пошло не так при клике на элемент....')
        except StaleElementReferenceException:
            if unique:
                sleep(3)
                self.element_find(*locator).click()
            if not unique:
                sleep(3)
                self.elements_find(*locator, index=index).click()

    def tap(self, *locator):
        actions = TouchAction(self.driver)
        actions.tap(self.element_find(*locator)).perform()

    def input(self, *locator, text):
        """
        Функция ввода текста на элемент.
        Используйте оператор распаковки * для указания локатора
        :param locator: locator
        :param text: text for input
        :return: input text for element
        """
        try:
            e = self.element_find(*locator)
            e.send_keys(text)
        except ElementNotVisibleException:
            logging.error('Элемент не отображается, но имеется в DOM')
            raise ElementNotVisibleException('Элемент не отображается, но имеется в DOM')
        except Exception:
            logging.error('Что-то пошло не так при вводе текста на элемент....')
            raise Exception('Что-то пошло не так при вводе текста на элемент....')

    def clear(self, *locator):
        """
        Функция очищения поля для ввода текста.
        Используйте оператор распаковки * для указания локатора
        :param locator: locator
        :return: clear input field
        """
        try:
            e = self.element_find(*locator)
            e.clear()
        except ElementNotVisibleException:
            logging.error('Элемент не отображается, но имеется в DOM')
            raise ElementNotVisibleException('Элемент не отображается, но имеется в DOM')
        except Exception:
            logging.error('Что-то пошло не так при очистке поля ввода текста....')
            raise Exception('Что-то пошло не так при очистке поля ввода текста....')

    def back(self):
        """
        Функция нажатия на кнопку BACK на смарфтоне
        :return: back button click
        """
        try:
            self.driver.back()
        except Exception:
            logging.error('ошибка при попытке нажать на кнопку НАЗАД на ОС')
            raise Exception('ошибка при попытке нажать на кнопку НАЗАД на ОС')
        else:
            logging.info('Успех при нажатии кнопки НАЗАД')

    def enter_button(self):
        """
        Клик на кнопку ENTER в клавиатуре
        :return: click enter button
        """
        try:
            self.driver.press_keycode(66)
        except Exception:
            logging.error('Не удалось применить кнопку ENTER')
            raise Exception('Не удалось применить кнопку ENTER')

    # Assert functions

    def assert_text_page_source(self, text, expected=True, timeout=4):
        """
        Функция assert или assert not текста в DOM страницы
        :param text: str (text for assert)
        :param expected: bool
        :param timeout: int
        :return: assert text inside DOM
        """
        if expected:
            try:
                assert text in self.driver.page_source
            except AssertionError:
                logging.error(f'Не удалось обнаружить ожидаемый текст: {text}  в странице элемента')
                raise AssertionError(f'Не удалось обнаружить ожидаемый текст: {text}  в странице элемента')

        if not expected:
            for i in range(timeout):
                try:
                    sleep(1)
                    assert text not in self.driver.page_source
                    break
                except AssertionError:
                    if i == timeout - 1:
                        logging.error(f'Удалось обнаружить текст: {text} в DOM, который по условия не должен')
                        raise AssertionError(f'Удалось обнаружить текст: {text}  в DOM, который по условия не должен')

    def assert_text_inside_element(self, *locator, text, unique=True, index=0, timeout=6, expected=True):
        """
        Assert любого текста в тексте элемента
        :param locator: element
        :param text: str Text for assert
        :param unique: bool
        :param index: if element not unique index
        """
        global e_text

        try:
            if unique:
                e_text = self.element_find(*locator, timeout=timeout).text
            elif not unique:
                e_text = self.elements_find(*locator, index=index, timeout=timeout).text

        except Exception:
            logging.error('Ошибка при assert, но это не AssertionError!!')
            raise Exception

        finally:
            if expected:
                try:
                    assert text == e_text
                except AssertionError as err:
                    logging.error(f'Не удалось assert ожидаемый текст: {text}, вместо этого найден: {e_text}')
                    raise err
            if not expected:
                try:
                    assert not text == e_text
                except AssertionError as err:
                    logging.error(f'Не удалось assert ожидаемый текст: {text}, вместо этого найден: {e_text}')
                    raise err

    def assert_element_located(self, *locator, expected=True, timeout=3):
        """
        Assert того что элемент отображен
        :param locator: element
        :param expected: bool
        :param timeout: int
        :return: assert true or false
        """
        wait = WebDriverWait(self.driver, timeout)
        if expected:
            try:
                assert wait.until(EC.visibility_of_element_located(locator))

            except TimeoutException:
                logging.error(f"Не удается найти элемент - {str(locator)}")
                raise TimeoutException(f"Не удается найти элемент - {str(locator)}")

        elif not expected:
            try:
                assert not wait.until(EC.visibility_of_element_located(locator))

            except Exception:
                logging.error(f"Не удается найти элемент - {str(locator)}")
                raise Exception

    # Return functions

    def return_element_text(self, *locator, timeout=7, index=1, unique=True):
        """
            return текста элемента
            :param locator: element
            :param timeout: int
            :param index: int
            :param unique: bool
            :return: str element_text
            """
        try:
            if unique:
                return self.element_find(*locator, timeout=timeout).text
            if not unique:
                return self.elements_find(*locator, index=index, timeout=timeout).text
        except Exception:
            logging.error(f"Ошибка при return текста элемента")
            raise Exception("Не удалось найти элемент : %s" % str(locator))

    def return_page_source(self):
        """
            return dom страницы
            :return: str page_source
            """
        source = self.driver.page_source
        return source

    # Swipe functions

    def swipe_with_coord(self, x, y):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(x[0], y[0])
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(x[1], y[1])
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def switch_to_webview(self, timeout=3):

        global webview_index

        for i in range(timeout):
            try:
                sleep(1)
                contexts = self.driver.contexts
                webview_index = contexts.index(WEBVIEW)
                logging.info('Удалось переключиться на WebView')
                break

            except ValueError as m:
                if i == 10 - 1:
                    raise m
                logging.error('Не удалось переключиться на WebView, проверьте приложение и страницу, '
                              f'доступные context: {self.driver.contexts}')

        self.driver.switch_to.context(self.driver.contexts[webview_index])

    def back_to_native_after_switch_wv(self):
        """
        Вернуться на нативку после подключчения к Webview.
        Используйте оператор распаковки * для указания локатор
        :return: back to native after switch wv
        """
        try:
            self.driver.switch_to.context(self.driver.contexts[0])
            logging.info(f'Удалось переключиться на {self.driver.contexts[0]}')

        except Exception:
            logging.error('Ошибка при возвращении на Native_VIEW')
            raise Exception('Ошибка при возвращении на Native_VIEW')

    def swipe_until(self, *locator, start_x=1000, start_y=500, end_x=1000, end_y=200, count=10, unique=True,
                    index=1, timeout=4):
        """
        свайп вниз пока не найдется элемент
        """
        for i in range(count):
            try:
                if unique:
                    self.element_find(*locator, timeout=timeout).is_displayed()
                    break
                elif not unique:
                    self.elements_find(*locator, index=index, timeout=timeout)
                    break
            except TimeoutException:
                self.swipe_with_coord(x=[start_x, end_x], y=[start_y, end_y])

    def swipe_until_up(self, *locator, start_x=383, start_y=1517, end_x=368, end_y=1997, count=10,
                       unique=True, index=0):
        """
        Свайп вверх пока не найдется элемент
        """
        self.driver.implicitly_wait(0.5)  # waits half a second
        for i in range(count):
            try:
                if unique:
                    self.element_find(*locator, timeout=2).is_displayed()
                    break
                elif not unique:
                    self.elements_find(*locator, index=index, timeout=2)
                    break

            except TimeoutException:
                self.swipe_with_coord(x=[start_x, end_x], y=[start_y, end_y])

    def wait_until_disappear(self, *locator, timeout=2):
        """
        Ожидание пока элемент не исчезнет
        :param locator: locator
        :param timeout: int timeout
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.invisibility_of_element_located(locator))

    def tap_with_coord(self, x, y):
        """
        Клик по экрану по координатам(использовать в крайних случаях)
        :param x: int x coord
        :param y: int y coord
        """
        try:
            self.actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH,
                                                                                     "touch"))
            self.actions.w3c_actions.pointer_action.move_to_location(x, y)
            self.actions.w3c_actions.pointer_action.pointer_down()
            self.actions.w3c_actions.pointer_action.pause(0.1)
            self.actions.w3c_actions.pointer_action.release()
            self.actions.perform()
        except Exception:
            logging.info(f'Не удалось сделать тап по координатам x:{str(x)} y:{str(y)}')
            raise Exception(f'Не удалось сделать тап по координатам x:{str(x)} y:{str(y)}')

        else:
            logging.info(f'Удалось сделать тап по координатам x:{str(x)} y:{str(y)}')
