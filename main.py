import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from classroom_utils import get_course_id, get_coursework_id, get_students, get_submissions_with_attachments
from drive_utils import download_drive_file
from report import Report

SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly',
    'https://www.googleapis.com/auth/classroom.student-submissions.students.readonly',
    'https://www.googleapis.com/auth/classroom.rosters.readonly',
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive'
]

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("classroom", "v1", credentials=creds)
        drive_service = build("drive", "v3", credentials=creds)

        course_name = "4L TPSIT 2024-25"
        coursework_name = "Verifica Python e Unit Testing"

        course_id = get_course_id(service, course_name)
        coursework_id = get_coursework_id(service, course_id, coursework_name)
        students = get_students(service, course_id)
        submissions = get_submissions_with_attachments(service, course_id, coursework_id)

        output_folder = os.path.join(course_name, coursework_name)
        os.makedirs(output_folder, exist_ok=True)

        for user_id, file_id in submissions:
            student_name = students.get(user_id, f"Unknown_Student_{user_id}")
            student_folder = os.path.join(output_folder, student_name)
            os.makedirs(student_folder, exist_ok=True)
            download_drive_file(drive_service, file_id, student_folder)

        output_excel = os.path.join(output_folder, "report.xlsx")
        Report.create_submission_report(students, submissions, output_excel)

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
