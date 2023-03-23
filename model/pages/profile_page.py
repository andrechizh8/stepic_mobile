import time
from selene.support.shared import browser
from selene import be, have
from appium.webdriver.common.appiumby import AppiumBy


class ProfilePage:
    def open_profile_settings(self):
        """Open settings to change in profile page"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/menu_item_edit")).click()
        browser.all((AppiumBy.ID, "org.stepic.droid:id/title")).element_by(have.text("Personal info")).click()
        return self

    def change_firstname(self,value):
        browser.element((AppiumBy.ID, "org.stepic.droid:id/firstNameEditText")).type(value)
        return self

    def change_lastname(self,value):
        browser.element((AppiumBy.ID, "org.stepic.droid:id/lastNameEditText")).type(value)
        return self

    def change_bio(self,value):
        browser.element((AppiumBy.ID, "org.stepic.droid:id/shortBioEditText")).type(value)
        return self

    def change_about_info(self,value):
        browser.element((AppiumBy.ID, "org.stepic.droid:id/shortBioEditText")).type(value)
        return self

    def submit_changes(self):
        browser.element((AppiumBy.ID, "org.stepic.droid:id/profile_edit_save")).click()
        return self

    def assert_changed_info(self,value):
        """Check profile info change is successful"""
        browser.all((AppiumBy.ID, "org.stepic.droid:id/title")).element_by(have.text("Personal info")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/lastNameEditText")).should(have.text(value))
        return self
