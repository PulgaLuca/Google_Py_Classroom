'''
INSTALLATION:
python -m venv venv
venv\Scripts\activate.bat
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
'''

'''
COURSES:
TechInfo_1G_23-24_IS_Pascal_Comandini
random
4L - Sistemi & Reti - 2024/25
4L - TPSIT - 2024/25
SR 3I 2024-25
TechInfo_1BIO_24-25_IS_Pascal_Comandini
TechInfo_1H_24-25_IS_Pascal_Comandini
TechInfo_1G_24-25_IS_Pascal_Comandini
TechInfo_1E_24-25_IS_Pascal_Comandini
Informatica
'''

'''
LINKS:
https://console.cloud.google.com/apis/dashboard?authuser=6&inv=1&invt=AbmPng&project=idyllic-nova-446811-j6
'''

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly',
    'https://www.googleapis.com/auth/classroom.student-submissions.me.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]

def main():
  """Shows basic usage of the Classroom API.
  Prints the names of the first 10 courses the user has access to.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("classroom", "v1", credentials=creds)

    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get("courses", [])

    if not courses:
      print("No courses found.")
      return
    # Prints the names of the first 10 courses.
    print("Courses:")
    for course in courses:
      print(course["name"])

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()