from selene.support.shared import browser
from selene import be, have
from appium.webdriver.common.appiumby import AppiumBy
from model.utils import app


class MainPage:
    def click_search_button(self):
        """Select search input to type """
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Catalog")).click()
        return self

    def open_profile(self):
        """Open profile page"""
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text("Profile")).click()
        return self

    def open_wishlist(self):
        """Open wishlist to add course"""
        app.scroll_to()
        browser.all((AppiumBy.ID, "org.stepic.droid:id/wishlistActionTitle")).element_by(
            (have.text("Wishlist"))).click()
        browser.element((AppiumBy.ID, "org.stepic.droid:id/goToCatalog")).click()
        return self
