from pages.GenericPage import GenericPage
from robot.libraries.BuiltIn import BuiltIn

_bi = BuiltIn()


class UserNotificationSettingsLocators:
    USER_NOTIFICATION_SETTINGS_PART_URL = '/user/settings'
    SETTINGS_FORM = 'css = table.settings'
    EMAIL_ACTIVATE_BUTTON = 'css = span.tender-header__link4'
    ACTIVATED_OPTION = 'css = td.settings-info.active'
    PAUSE_BUTTON = 'css = .tender-header__link4 i.icon-pause'
    CANCEL_BUTTON = 'css = .tender-header__link4 i.icon-remove'
    PAUSE_APPROVE_BUTTON = 'css = div#review_form4 a.tender-header__link2:first-child'
    PAUSE_DECLINE_BUTTON = 'css = div#review_form4 a.tender-header__link2:nth-child(2)'
    RENEW_APPROVE_BUTTON = 'css = div#review_form5 a.tender-header__link2:first-child'
    RENEW_DECLINE_BUTTON = 'css = div#review_form5 a.tender-header__link2:nth-child(2)'
    CANCEL_APPROVE_BUTTON = 'css = div#review_form6 a.tender-header__link2:first-child'
    CANCEL_DECLINE_BUTTON = 'css = div#review_form6 a.tender-header__link2:nth-child(2)'
    RENEW_SUBSCRIPTION_BUTTON = 'css = td.w-1percent span.tender-header__link4'


class UserNotificationSettings(GenericPage):
    def should_be_notification_settings_page(self):
        _bi.run_keyword('Location Should Contain', UserNotificationSettingsLocators.USER_NOTIFICATION_SETTINGS_PART_URL)
        _bi.run_keyword('Wait Until Page Contains Element', UserNotificationSettingsLocators.SETTINGS_FORM)

    def user_activate_email_subscription(self):
        self.wait_and_click(UserNotificationSettingsLocators.EMAIL_ACTIVATE_BUTTON)
        _bi.run_keyword('Wait Until Page Contains Element', UserNotificationSettingsLocators.ACTIVATED_OPTION)

    def should_be_pause_and_cancel_subscription_button(self):
        _bi.run_keyword('Wait Until Page Contains Element', UserNotificationSettingsLocators.PAUSE_BUTTON)
        _bi.run_keyword('Wait Until Page Contains Element', UserNotificationSettingsLocators.CANCEL_BUTTON)

    def user_pause_subscription(self):
        self.wait_and_click(UserNotificationSettingsLocators.PAUSE_BUTTON)
        self.wait_and_click(UserNotificationSettingsLocators.PAUSE_APPROVE_BUTTON)
        _bi.run_keyword('Wait Until Page Contains Element', UserNotificationSettingsLocators.RENEW_SUBSCRIPTION_BUTTON)

    def user_restore_subscription(self):
        self.wait_and_click(UserNotificationSettingsLocators.RENEW_SUBSCRIPTION_BUTTON)
        self.wait_and_click(UserNotificationSettingsLocators.RENEW_APPROVE_BUTTON)

    def user_cancel_subscription(self):
        self.wait_and_click(UserNotificationSettingsLocators.CANCEL_BUTTON)
        self.wait_and_click(UserNotificationSettingsLocators.CANCEL_APPROVE_BUTTON)
        _bi.run_keyword('Wait Until Page Contains Element', UserNotificationSettingsLocators.EMAIL_ACTIVATE_BUTTON)

