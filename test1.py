
email_sender = "dusach2018@gmail.com"
email_password = "siheqnayysqtlwcj"

import ssl
import smtplib
from email.message import EmailMessage
import random
import string
import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

spreadsheet_id = '1I11-qzlo9UxWwl1IVKfpzmtIGfQza7l6Ux8GPwWN9wQ'
class SheetObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        print("Credentials Done!")
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("/Users/abdullaharean/Desktop/django/mailSender/token.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    try:
        service =build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId = spreadsheet_id, range = "Sheet1!A1:L38").execute()
        values = result.get("values", [])
        header_row = values[0]
        objects = []

        for row in values[1:]:
            data = {}
            for i, value in enumerate(row):
                data[header_row[i]] = value

            obj = SheetObject(**data)
            objects.append(obj)

        for obj in objects:
            print(obj.name)
            
    except HttpError as error:
        print(error)
        
if __name__ == "__main__":
    main()