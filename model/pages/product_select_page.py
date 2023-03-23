import time
from selene.support.shared import browser
from selene import be, have
from appium.webdriver.common.appiumby import AppiumBy
from model.utils import app


class ProductSelectPage:

    def change_course_language_to_rus(self):
        """Change language of course"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/languageRu")).click()
        return self

    def search_course_with_filters(self):
        """Typing course name in search field and choose different filters to select course"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/search_src_text")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/search_src_text")).send_keys("Python")
        browser.element((AppiumBy.ID, "org.stepic.droid:id/filterIcon")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/certificatesSwitch")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/applyFilterAction")).click()
        return self

    def assert_course_found_successful(self):
        """Check that right course is found"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/courseItemName")).with_(timeout=10).should(be.visible).should(have.text("Python"))
        return self

    def add_course_to_wishlist(self):
        """Open wishlist and add selected course"""
        browser.all((AppiumBy.ID, "org.stepic.droid:id/containerTitle")).element_by(
            have.text("Editors' choice")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/courseItemName")).should(be.clickable).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/wishlist_course")).with_(timeout=2).should(
            be.clickable).click()
        return self

    def assert_course_add_to_wishlist(self):
        """Open wishlist and check that course was added"""
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).should(be.clickable).click()
        time.sleep(2)
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).should(be.clickable).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/home")).click()
        app.scroll_to()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/wishlistActionCourseCount")).should(be.visible).should(
            have.text("1 course"))
        return self

    def delete_course_from_wishlist(self):
        """Open wishlist and delete selected course"""
        browser.all((AppiumBy.ID, "org.stepic.droid:id/wishlistActionTitle")).element_by(
            (have.text("Wishlist"))).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/courseItemName")).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/wishlist_course")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Navigate up")).click()
        return self

    def assert_course_deleted_from_wishlist(self):
        """Check that course was deleted"""
        browser.element((AppiumBy.ID, "org.stepic.droid:id/placeholderMessage")).should(have.text("Courses not found"))
        return self
