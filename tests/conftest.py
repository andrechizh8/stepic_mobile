import allure
import allure_commons
import pytest
import requests
from selene.support.shared import browser
from selene import support
from appium import webdriver
import pytest
from _pytest.nodes import Item
from _pytest.runner import CallInfo
from model.utils import attach

import config


@pytest.fixture(scope='function', autouse=True)
def driver_management(request):
    browser.config.timeout = config.settings.timeout
    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    browser.config.driver = webdriver.Remote(
        config.settings.remote_url, options=config.settings.driver_options
    )

    yield

    if config.settings.run_on_browserstack and request.node.result_of_call.failed:
        '''
        request.node is an "item" because we use the default "function" scope
        '''
        attach.screenshot()
        attach.screen_xml_dump()

    session_id = browser.driver.session_id

    if config.settings.run_on_browserstack:
        attach.video_from_browserstack(session_id=session_id)
        attach.screenshot()
        attach.screen_xml_dump()

    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: Item, call: CallInfo):
    outcome = yield
    result_of_ = outcome.get_result()
    setattr(item, 'result_of_' + result_of_.when, result_of_)
