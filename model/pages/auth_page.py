import time

from selene.support.shared import browser
from selene import be, have
from model.utils import app
from appium.webdriver.common.appiumby import AppiumBy


class AuthPage:

    def type_email(self, email):
        """Select email field and typing info"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/signInWithEmail")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/loginField")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/loginField")).type(email)

        return self

    def type_password(self, password):
        """Select password field and typing info"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/passwordField")).type(password)
        browser.element((AppiumBy.ID, "org.stepic.droid:id/loginButton")).click()

        return self

    def skip_message(self):
        """Skip greeting`s message"""
        browser.element((AppiumBy.ID, "android:id/button1")).click()
        time.sleep(2)
        browser.element((AppiumBy.ID, "android:id/button1")).click()

        return self

    def check_successful_auth(self):
        """Check that auth is successful"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/containerTitle")).should(be.clickable)

        return self

    def assert_error_login_password(self):
        """Check error message"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/loginErrorMessage")).should(
            have.text("Login/password was incorrect"))
        return self
