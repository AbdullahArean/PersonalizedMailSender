# PersonalizedMailSender

This repository contains a Python script that allows you to fetch data from a Google Sheets spreadsheet, convert each row into an object, and send personalized emails to each object using their respective email addresses. This can be useful for tasks such as sending personalized newsletters, announcements, or notifications to a group of recipients.

## Prerequisites

Before using this script, make sure you have the following prerequisites set up:

1. Python: Make sure you have Python installed on your system. You can download it from the official Python website: [python.org/downloads](https://www.python.org/downloads/)

2. Google Sheets API: Enable the Google Sheets API for your project and obtain the necessary credentials. Refer to the Google Sheets API documentation for detailed instructions: [developers.google.com/sheets/api/quickstart](https://developers.google.com/sheets/api/quickstart)

3. Gmail API: Enable the Gmail API for your project and obtain the necessary credentials. Refer to the Gmail API documentation for detailed instructions: [developers.google.com/gmail/api/quickstart](https://developers.google.com/gmail/api/quickstart)

4. Libraries: Install the required Python libraries by running the following command:

```
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## Setup

1. Clone this repository to your local machine or download the script file `fetch_data_send_emails.py`.

2. Place the obtained credentials file (e.g., `token.json`) for both the Google Sheets API and Gmail API in the same directory as the script.

3. Open the script file `fetch_data_send_emails.py` in a text editor.

4. Update the following variables at the beginning of the script with the appropriate values

5. Customize the email content generation logic in the `generate_email_content` function according to your requirements. This function takes a row object as an argument and should return the personalized email content.

6. Save the script file after making the necessary changes.

## Usage

To use the script:

1. Open a terminal or command prompt.

2. Navigate to the directory containing the script file.

3. Run the following command to execute the script:

```
python fetch_data_send_emails.py
```

The script will fetch the data from the specified Google Sheets spreadsheet, create objects from each row, and send personalized emails to each object using their email addresses.

Note: The first row in the specified range is assumed to be the header row containing column names.

## Notes

- Make sure that the email account used to send emails has the necessary permissions to access the Google Sheets spreadsheet and send emails through the Gmail API.

- Take care to handle sensitive data securely, such as API credentials and recipient email addresses.

- It's recommended to test the script with a small dataset or in a controlled environment before using it with a large number of recipients.


