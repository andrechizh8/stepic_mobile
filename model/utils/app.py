from model.pages.main_page import MainPage
from model.pages.auth_page import AuthPage
from model.pages.product_select_page import ProductSelectPage
from model.pages.profile_page import ProfilePage
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selene.support.shared import browser
from selene import be, have

main = MainPage()
product = ProductSelectPage()
auth = AuthPage()
profile = ProfilePage()


def given_opened():
    """Skip  onboarding pages and auth by email/password"""
    browser.element((AppiumBy.ACCESSIBILITY_ID, "Close")).with_(timeout=3).should(be.clickable).click()


def scroll_to():
    """Scroll to element for different screen size"""
    for each in range(1, 2):
        browser.driver.swipe(500, 1700, 500, 1000, 400)
