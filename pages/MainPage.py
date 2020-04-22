from pages import Config
from pages.GenericPage import GenericPage
from robot.libraries.BuiltIn import BuiltIn


_bi = BuiltIn()


class MainPageLocators:
    CLOSE_POPUP_LINK = 'css = div#review_form3_wrapper a.delete'
    LOGIN_LINK = 'css = div.login_link a'
    HEADER_LOGO = 'css = .c-header__logo'
    GOOGLE_AUTH = 'css = .btn-google'
    FACEBOOK_AUTH = 'css = .btn-facebook'
    USER_MENU_DROPDOWN = 'css = div.user_login'
    NOTIFICATION_SETTINGS_LINK = 'css = ul.dropdown-menu li:first-child'


class GoogleAuthLocators:
    GOOGLE_EMAIL_INPUT = 'css = input[type="email"]'
    GOOGLE_NEXT_BUTTON = 'css = div#identifierNext'
    GOOGLE_PASS_INPUT = 'css = input[type="password"]'
    GOOGLE_PASS_NEXT_BUTTON = 'css = div#passwordNext'


class MainPage(GenericPage):

    def open_main_page(self):
        self.open_page('/')
        _bi.run_keyword('Wait Until Element Is Visible', MainPageLocators.HEADER_LOGO, 'timeout=3')

    def guest_close_popup(self):
        self.wait_and_click(MainPageLocators.CLOSE_POPUP_LINK)

    def guest_go_to_login_link(self):
        self.wait_and_click(MainPageLocators.LOGIN_LINK)
        _bi.run_keyword('Wait Until Element Is Visible', MainPageLocators.GOOGLE_AUTH)
        _bi.run_keyword('Wait Until Element Is Visible', MainPageLocators.FACEBOOK_AUTH)

    def guest_log_in_by_google(self):
        self.wait_and_click(MainPageLocators.GOOGLE_AUTH)
        self.wait_and_type(GoogleAuthLocators.GOOGLE_EMAIL_INPUT, Config.email)
        self.wait_and_click(GoogleAuthLocators.GOOGLE_NEXT_BUTTON)
        _bi.sleep(2)
        self.wait_and_type(GoogleAuthLocators.GOOGLE_PASS_INPUT, Config.password)
        self.wait_and_click(GoogleAuthLocators.GOOGLE_PASS_NEXT_BUTTON)
        _bi.run_keyword('Wait Until Element Is Visible', MainPageLocators.USER_MENU_DROPDOWN, 'timeout=3')

    def user_go_to_account_settings(self):
        self.wait_and_click(MainPageLocators.USER_MENU_DROPDOWN)
        self.wait_and_click(MainPageLocators.NOTIFICATION_SETTINGS_LINK)
