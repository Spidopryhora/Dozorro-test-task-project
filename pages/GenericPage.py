from robot.libraries.BuiltIn import BuiltIn

_bi = BuiltIn()


class GenericPage:

    def __init__(self, url='https://dev.dozorro.work'):
        self.base_url = url

    def open_page(self, page, browser='chrome'):
        """
        This keyword build url of specific page and open browser using this url

        Args:
            page(string): The part of the url of the specific page, use "/" for base url

        Retunrs:
            dest_url(string): Built url of specific page

        """

        dest_url = f"{self.base_url}{page}"
        _bi.run_keyword('Open browser', dest_url, f'browser={browser}')

        return dest_url

    def go_to_page(self, page):
        """
        This keyword build url of specific page and navigate user to this url

        Args:
            page(string): The part of the url of the specific page, use "/" for base url

        Retunrs:
            dest_url(string): Built url of specific page

        """
        dest_url = f"{self.base_url}{page}"
        _bi.run_keyword('Go to', dest_url)

        return dest_url

    def wait_and_click(self, locator):
        """
        This keyword wait until element appears on the page and than click it

        Args:
            locator(string): The locator of the element

        Retunrs:
            None

        """

        _bi.run_keyword("Wait Until Page Contains Element", locator)
        _bi.run_keyword("Set Focus To Element", locator)
        _bi.run_keyword("Click element", locator)

    def wait_and_type(self, locator, text):
        """
        This keyword wait until input field appears on the page and than typr text into it

        Args:
            locator(string): The locator of the field
            text(string): User's text

        Retunrs:
            None

        """
        _bi.run_keyword("Wait Until Page Contains Element", locator)
        _bi.run_keyword("Set Focus To Element", locator)
        _bi.run_keyword("Input text", locator, text)

