from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account 

# if modifying these scopes delete the file token.json
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """ Show basic usage of the Gmail API.
        Lists the user's Gmail labels
    """

    creds = None
    # the file token.json stores the user's access and refresh tokens
    # and is created automatically when the authorization flow completes for the first time

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # if there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # flow = InstalledAppFlow.from_client_secrets_file('helloworld-326911-88f09c03d285.json', SCOPES)
            # creds = flow.run_local_server(port=0)            

            creds = service_account.Credentials.from_service_account_file('helloworld-326911-88f09c03d285.json', scopes = SCOPES)

        # save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        result = service.users().labels().list(userId='me').execute()
        labels = result.get('labels', [])

        if not labels:
            print('No labels found.')
            return

        print('Labels:')
        for label in labels:
            print(label['name'])

    except HttpError as error:
        # Handle errors from gmail API
        print(f'An error occured: {error}')


if __name__ == '__main__':
    main()