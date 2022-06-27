

class DesiredCapAndroid(object):
    ANDROID_FOR_REAL_TEST = {}
    ANDROID_FOR_REAL_TEST['platformName'] = "Android"
    ANDROID_FOR_REAL_TEST['platformVersion'] = "12"
    ANDROID_FOR_REAL_TEST['deviceName'] = "Emulator"
    ANDROID_FOR_REAL_TEST['automationName'] = 'UiAutomator2'
    ANDROID_FOR_REAL_TEST['appPackage'] = 'kz.tele2.app'
    ANDROID_FOR_REAL_TEST['appPackage'] = 'team.alabs.tele2.dev'
    ANDROID_FOR_REAL_TEST['appActivity'] = "kz.sardarpro.tele2.ui.unauthorized.UnauthorizedActivity"
    ANDROID_FOR_REAL_TEST['resetKeyboard'] = "true"
    ANDROID_FOR_REAL_TEST['unlockType'] = "pin"
    ANDROID_FOR_REAL_TEST['unlockKey'] = "7586"
    ANDROID_FOR_REAL_TEST['noReset'] = "true"
    ANDROID_FOR_REAL_TEST['fullReset'] = "false"
    ANDROID_FOR_REAL_TEST['avdLaunchTimeout'] = '300000'
    # ANDROID_FOR_REAL_TEST['appium:chromedriverExecutable'] = "/Users/muratisaev/Downloads/chromedriver"

    ANDROID_FOR_DEBUG = {}
    ANDROID_FOR_DEBUG['platformName'] = "Android"
    ANDROID_FOR_DEBUG['platformVersion'] = "12"
    ANDROID_FOR_DEBUG['deviceName'] = "Emulator"
    ANDROID_FOR_DEBUG['automationName'] = 'UiAutomator2'
    ANDROID_FOR_DEBUG['resetKeyboard'] = "true"
    ANDROID_FOR_DEBUG['noReset'] = "true"
    ANDROID_FOR_DEBUG['fullReset'] = "false"
    ANDROID_FOR_DEBUG['unlockType'] = "pin"
    ANDROID_FOR_DEBUG['unlockKey'] = "7586"
    # ANDROID_FOR_DEBUG['appium:chromedriverExecutable'] = "/Users/muratisaev/Downloads/chromedriver"

    ANDROID_EMULATOR = {}
    ANDROID_EMULATOR['platformName'] = "Android"
    ANDROID_EMULATOR['platformVersion'] = "11"
    ANDROID_EMULATOR['deviceName'] = "Android emulator"

