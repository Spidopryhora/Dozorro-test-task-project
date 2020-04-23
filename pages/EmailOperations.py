from robot.libraries.BuiltIn import BuiltIn
import time
from pages.Gmail import *

_bi = BuiltIn()
service = gmail_auth()


class EmailOperations():

    def user_get_activation_link(self):
        _bi.sleep(10)
        mails_list = get_list_of_present_mail(service, gmail_query='from:notify@bot.dozorro.org is:unread')
        self.dozorro_mail = mails_list['messages'][0]['id']
        message_body = get_message_body(service, self.dozorro_mail)
        self.activation_link = message_body.split(' ')[-1]  # get activation link

    def user_navigates_through_the_link(self):
        _bi.run_keyword('Go to', self.activation_link)

    def user_delete_activation_email(self):
        delete_mail(service, self.dozorro_mail)

    @staticmethod
    def send_successful_test_run_report():
        subject = f'Test run {time.asctime(time.localtime(time.time()))} was successful!'
        body_message = f'Test run {time.asctime(time.localtime(time.time()))} was successful!'
        msg = create_message(sender='bzserptest@gmail.com', to='bzserptest@gmail.com', subject=subject,
                             message_text=body_message)
        send_message(service, user_id='me', message=msg)

    @staticmethod
    def send_failed_test_run_report():
        subject = f'Test run {time.asctime(time.localtime(time.time()))} was failed!'
        body_message = f'Test run {time.asctime(time.localtime(time.time()))} was failed!'
        msg = create_message(sender='bzserptest@gmail.com', to='bzserptest@gmail.com', subject=subject,
                             message_text=body_message)
        send_message(service, user_id='me', message=msg)
