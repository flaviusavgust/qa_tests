from allure_commons.types import AttachmentType
import allure


def allure_screenshot(driver, name='Скриншот теста'):
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.JPG)
