import allure
import pytest
import logging
from appium import webdriver
from src.helpers.desired_capabilities import DesiredCapAndroid
from src.helpers.allure_utils import allure_screenshot
import os


remote = 'http://172.22.2.15:4723/wd/hub'
locahost = 'http://localhost:4723'


@pytest.fixture()
@allure.title('Настройки драйвера Appium')
def driver_fixture(request):
    logging.info("Инициализация драйвера Appium")

    appium_driver = webdriver.Remote(locahost, desired_capabilities=DesiredCapAndroid.ANDROID_FOR_REAL_TEST)
    logging.info("ID сессии {}".format(appium_driver.session_id))
    failed_before = request.session.testsfailed

    yield appium_driver

    if request.session.testsfailed != failed_before:
        appium_driver.switch_to.context('NATIVE_APP')
        allure_screenshot(appium_driver, 'Скриншот при провале теста')

    appium_driver.quit()
