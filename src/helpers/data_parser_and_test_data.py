from configparser import ConfigParser
import os
from src.helpers.time_utils import date_hours_minutes_return
from faker import Faker

fake = Faker()

config = ConfigParser()

path = str('/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])) + '/test_data'


def user_for_test():
    config.read(os.path.join(path, 'test_users.ini'))

    return config


def data_for_test():
    config.read(os.path.join(path, 'test_data.ini'))

    return config


class GeneratedDataAutopayments:
    NAME = f'Тестовый автоплатеж {date_hours_minutes_return()}'


class GeneratedDataGroupDisc:
    FAKE_NAME = fake.name()
