from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from src.helpers.base_page import BasePage
import allure
from time import sleep
from src.helpers.allure_utils import allure_screenshot
import re
import logging
from src.helpers.constants import ENVIRONMENT as env
from selenium.common.exceptions import NoSuchElementException
from src.helpers import time_utils
from src.helpers.data_parser_and_test_data import user_for_test, data_for_test


