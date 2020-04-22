from robot.libraries.BuiltIn import BuiltIn
import time
from pages.Gmail import *

_bi = BuiltIn()


class EmailOperations:

    def user_get_activation_link(self):
        _bi.sleep(5)
        self.service = gmail_auth()
        mails_list = get_list_of_present_mail(service, gmail_query='from:notify@bot.dozorro.org is:unread')
        self.dozorro_mail = mails_list['messages'][0]['id']
        message_body = get_message_body(service, self.dozorro_mail)
        self.activation_link = message_body.split(' ')[-1]  # get activation link

    def user_navigates_through_the_link(self):
        _bi.run_keyword('Open Browser', self.activation_link, 'chrome')

    def user_delete_activation_email(self):
        delete_mail(self.service, self.dozorro_mail)

    def send_successful_test_run_report(self):

        pass
