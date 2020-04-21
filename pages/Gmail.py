import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
from apiclient import errors

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def gmail_auth():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def get_list_of_present_mail(service, gmail_query=None):
    message_list_response = service.users().messages().list(userId='me', q=gmail_query).execute()

    if message_list_response['resultSizeEstimate'] > 0:
        message_id = message_list_response['messages']

    else:
        print('No recent messages')
        return None

    return message_list_response


def get_message_body(service, message_id):
    message_response = service.users().messages().get(userId='me', id=message_id).execute()
    message_body = str(base64.urlsafe_b64decode(message_response['payload']['body']['data']), 'utf-8')
    return message_body


def delete_mail(service, message_id):
    try:
        service.users().messages().delete(userId='me', id=message_id).execute()
        print
        'Message with id: %s deleted successfully.' % msg_id
    except errors.HttpError:
        print(f'An error occurred: {errors.HttpError}')
