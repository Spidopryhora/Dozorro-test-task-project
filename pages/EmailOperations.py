from robot.libraries.BuiltIn import BuiltIn
import time
from pages.Gmail import *

_bi = BuiltIn()


class EmailOperations:
    def __init__(self, ):
        self.sender = 'bzserptest@gmail.com'
        self.to = 'bzserptest@gmail.com'


    def user_get_activation_link(self):
        _bi.sleep(5)
        self.service = gmail_auth()
        mails_list = get_list_of_present_mail(self.service, gmail_query='from:notify@bot.dozorro.org is:unread')
        self.dozorro_mail = mails_list['messages'][0]['id']
        message_body = get_message_body(self.service, self.dozorro_mail)
        self.activation_link = message_body.split(' ')[-1]  # get activation link

    def user_navigates_through_the_link(self):
        _bi.run_keyword('Open Browser', self.activation_link, 'chrome')

    def user_delete_activation_email(self):
        delete_mail(self.service, self.dozorro_mail)

    def send_successful_test_run_report(self):
        subject = f'Test run {time.asctime(time.localtime(time.time()))} was successful!'
        body_message = f'Test run {time.asctime(time.localtime(time.time()))} was successful!'
        msg = create_message_with_attachment(sender=self.sender, to=self.to, subject=subject, message_text=body_message,
                                             file='../report.html')
        send_message(self.service, user_id='me', message=msg)

    def send_failed_test_run_report(self):
        subject = f'Test run {time.asctime(time.localtime(time.time()))} was failed!'
        body_message = f'Test run {time.asctime(time.localtime(time.time()))} was failed!'
        msg = create_message_with_attachment(sender=self.sender, to=self.to, subject=subject, message_text=body_message,
                                             file='../report.html')
        send_message(self.service, user_id='me', message=msg)


