import ssl
import smtplib
from email.message import EmailMessage
from seatprint import create_participants_grid
from listprint import create_participants_list
email_sender = "dusach2018@gmail.com"
email_password = "ruqqcqqlfzhzwmtw"

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

spreadsheet_id = '18T4Rck7xpFRyQK5Sjp0HNkENSSrb_RI8vIuCbSOPuIo'

class SheetObject:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
def mail(student_info):
    # Customize the confirmation message using the student information
    registration_confirmation = f"""
Dear {student_info.name},
Thanks for registering for DUSACH Admission Guideline Program Season 4. Your Registration is confirmed and your reserved seat number is "{student_info.sitNum}".
From "{student_info.schoolName}", to getting GPA "{student_info.sscResult}" in SSC and then getting into your dream college "{student_info.collegeName}", your hard work and dedication have been truly commendable. We sincerely hope that you will secure admission into the renowned public universities of Bangladesh. This programs aims at making the pathway smooth for you!

The token collection for the program will begin at "9 AM", and it is essential that registered students collect their tokens from the spot booth and take their designated seats. Please note that entry into the auditorium will require a valid token, and token collection will close promptly at "9:30 AM". 

Event Details:
Date: 1st July 2023
Venue: Chatkhil Upazilla Parishad Auditorium, Chatkhil, Noakhali 
Seat Number: "{student_info.sitNum}"

Event Schedule:
Morning 09:00 - 09:30:Token Collection From Spot 
Morning 10:00 - 10:20: Recitation and recitation of the Quran
Morning 10:20 - 11:30: Instructional speech (Science, Business Education, Humanity)
Morning 11:30 - 1:00: Speech by invited guests
Afternoon 1:00 - 2:00: Prayer and lunch break + Lunch
Afternoon 2:00 - 3:00: Quiz competition
Afternoon 3:00 - 4:00: Closing ceremony + Snacks 

Your presence will be essential to ensuring that the program runs smoothly and that we achieve our goals. Your insights and feedback were invaluable, and I am confident that they will help us to make this program even better.

Yours faithfully,
Abdullah Ibne Hanif Arean
Department of Computer Science and Engineering
University of Dhaka
Joint General Secretary
Dhaka University Student's Association of Chatkhil (DUSACH)
    """


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = student_info.email
    em[
        'Subject'
    ] = f"Registration Confirmation Seat {student_info.sitNum} : Dhaka University Admission Test Guideline Program Season 4"
    em.set_content(registration_confirmation)

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls(context=context)
        smtp.login(email_sender, email_password)
        smtp.send_message(em)
def print_college_occurrences(objects):
    college_counts = {}
    
    for obj in objects:
        college_name = obj.collegeName
        if college_name in college_counts:
            college_counts[college_name] += 1
        else:
            college_counts[college_name] = 1
    
    for college_name, count in college_counts.items():
        print(f"{college_name}, :: {count}")

def main():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        print("Credentials Done!")
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("token.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())
    try:
        service =build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()
        result = sheets.values().get(spreadsheetId = spreadsheet_id, range = "Sheet1!A1:O83").execute()
        values = result.get("values", [])
        header_row = values[0]
        objects = []

        for row in values[1:]:
            data = {}
            for i, value in enumerate(row):
                data[header_row[i]] = value

            obj = SheetObject(**data)
            objects.append(obj)
        print_college_occurrences(objects)
        create_participants_grid(objects)
        create_participants_list(objects)
        for obj in objects:
            print(obj.__dict__)
                
                

        
            
    except HttpError as error:
        print(error)
        
if __name__ == "__main__":
    main()