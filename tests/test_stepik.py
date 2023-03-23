import allure
import pytest
from allure_commons.types import Severity
from model.utils import app
from model.data.user_data import current_user


class TestMobile:

    @pytest.mark.login
    @allure.tag('UI', 'MOBILE')
    @allure.description('STEPIC UI MOBILE test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('MOBILE')
    @allure.story('Successful Login')
    @allure.severity(Severity.CRITICAL)
    def test_successful_login(self):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()

        # WHEN
        with allure.step("Type correct auth data"):
            app.auth.type_email(current_user.email)
            app.auth.type_password(current_user.password)
            app.auth.skip_message()

        # THEN
        with allure.step("Check successful auth"):
            app.auth.check_successful_auth()

    @pytest.mark.error
    @allure.tag('UI', 'MOBILE')
    @allure.description('STEPIC UI MOBILE test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('MOBILE')
    @allure.story('Unsuccessful Login')
    @allure.severity(Severity.CRITICAL)
    def test_login_with_rong_email(self):
        # GIVEN
        with allure.step("Open main page"):
            app.given_opened()

        # WHEN
        with allure.step("Type incorrect auth data"):
            app.auth.type_email(current_user.random_email)
            app.auth.type_password(current_user.random_password)

        # THEN
        with allure.step("Check auth error"):
            app.auth.assert_error_login_password()

    @pytest.mark.search
    @allure.tag('UI', 'MOBILE')
    @allure.description('STEPIC UI MOBILE test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('MOBILE')
    @allure.story('Search course')
    @allure.severity(Severity.CRITICAL)
    def test_search_courses(self):
        # GIVEN
        with allure.step("Login"):
            self.test_successful_login()

        # WHEN
        with allure.step("Search course"):
            app.main.click_search_button()
            app.product.change_course_language_to_rus()
            app.product.search_course_with_filters()

        # THEN
        with allure.step("Check searching course"):
            app.product.assert_course_found_successful()

    @pytest.mark.search
    @allure.tag('UI', 'MOBILE')
    @allure.description('STEPIC UI MOBILE test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('MOBILE')
    @allure.story('Add to wishlist')
    @allure.severity(Severity.NORMAL)
    def test_add_course_to_wishlist(self):
        # GIVEN
        with allure.step("Login"):
            self.test_successful_login()

        # WHEN
        with allure.step("Open wishlist page"):
            app.main.open_wishlist()
            app.product.add_course_to_wishlist()

        # THEN
        with allure.step("Check adding to wishlist"):
            app.product.assert_course_add_to_wishlist()
        with allure.step("Delete course from wishlist"):
            app.product.delete_course_from_wishlist()

    @pytest.mark.profile
    @allure.tag('UI', 'MOBILE')
    @allure.description('STEPIC UI MOBILE test')
    @allure.label('owner', 'andrechizh8')
    @allure.feature('MOBILE')
    @allure.story('Change profile info')
    @allure.severity(Severity.NORMAL)
    def test_change_profile_settings(self):
        # GIVEN
        with allure.step("Login"):
            self.test_successful_login()

        # WHEN
        with allure.step("Open profile settings"):
            app.main.open_profile()
            app.profile.open_profile_settings()
        with allure.step("Change profile name"):
            app.profile.change_firstname(current_user.first_name)
            app.profile.change_lastname(current_user.last_name)
        with allure.step("Change profile bio"):
            app.profile.change_bio(current_user.bio_info)
        with allure.step("Submit profile changing"):
            app.profile.submit_changes()

        # THEN
        with allure.step("Check profile changed"):
            app.profile.assert_changed_info(current_user.last_name)
