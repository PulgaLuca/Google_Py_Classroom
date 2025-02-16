def get_course_id(service, course_name):
    courses = service.courses().list(pageSize=100).execute().get('courses', [])
    for course in courses:
        if course['name'] == course_name:
            return course['id']
    return None

def get_coursework_id(service, course_id, coursework_name):
    coursework_list = service.courses().courseWork().list(courseId=course_id, pageSize=100).execute().get('courseWork', [])
    for coursework in coursework_list:
        if coursework['title'] == coursework_name:
            return coursework['id']
    return None

def get_students(service, course_id):
    students = service.courses().students().list(courseId=course_id, pageSize=100).execute().get('students', [])
    return {student['userId']: student['profile']['name']['fullName'] for student in students}

def get_submissions_with_attachments(service, course_id, coursework_id):
    submissions = service.courses().courseWork().studentSubmissions().list(courseId=course_id, courseWorkId=coursework_id, pageSize=100).execute().get('studentSubmissions', [])
    submissions_data = []
    for submission in submissions:
        assignmentSubmission = submission.get('assignmentSubmission', None)
        attachments = assignmentSubmission.get('attachments', [])
        user_id = submission.get('userId')
        if attachments and user_id:
            for attachment in attachments:
                if 'driveFile' in attachment:
                    submissions_data.append((user_id, attachment['driveFile']['id']))
    return submissions_data
