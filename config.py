import pydantic
from appium.options.android import UiAutomator2Options
from typing import Literal, Optional
from model.utils import file

EnvContext = Literal['browserstack', 'local']


class Settings(pydantic.BaseSettings):
    context: EnvContext = 'browserstack'

    # --- Appium Capabilities ---
    platformName: str = 'android'
    platformVersion: str = '9.0'
    deviceName: str = 'Google Pixel 3'
    app: Optional[str] = None
    appName: Optional[str] = None
    newCommandTimeout: Optional[int] = 60
    udid: Optional[str] = None
    appWaitActivity: Optional[str] = None

    # --- > BrowserStack Capabilities ---
    projectName: Optional[str] = None
    buildName: Optional[str] = None
    sessionName: Optional[str] = None
    # --- > > BrowserStack credentials---
    userName: Optional[str] = pydantic.Field(None, env='browserstack.userName')
    accessKey: Optional[str] = pydantic.Field(None, env='browserstack.accessKey')

    # --- Remote Driver ---
    remote_url: str = 'http://127.0.0.1:4723/wd/hub'

    # --- Selene ---
    timeout = 60

    @property
    def run_on_browserstack(self):
        return 'hub.browserstack.com' in self.remote_url

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        if self.deviceName:
            options.device_name = self.deviceName
        if self.platformName:
            options.platform_name = self.platformName
        options.app = (
            file.abs_path_from_project(self.app)
            if self.app and (self.app.startswith('stepic') or self.app.startswith('ste'))
            else self.app
        )
        options.new_command_timeout = self.newCommandTimeout
        if self.udid:
            options.udid = self.udid
        if self.appWaitActivity:
            options.app_wait_activity = self.appWaitActivity
        if self.run_on_browserstack:
            options.load_capabilities(
                {
                    'platformVersion': self.platformVersion,
                    'bstack:options': {
                        'projectName': self.projectName,
                        'buildName': self.buildName,
                        'sessionName': self.sessionName,
                        'userName': self.userName,
                        'accessKey': self.accessKey,
                    },
                }
            )

        return options

    @classmethod
    def in_context(cls, env: Optional[EnvContext] = None) -> 'Settings':

        asked_or_current = env or cls().context
        return cls(
            _env_file=file.abs_path_from_project(f'config.{asked_or_current}.env')
        )


settings = Settings.in_context()
