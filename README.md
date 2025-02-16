# 📚 Classroom Downloader 🚀  

Automise download of homework from Google Classroom  

This script allows you to automatically download the attachments of assignments handed in by students on Google Classroom, organising them in folders by class and assignment. It also generates an Excel report with the status of the assignments.  

## ✨ Functionality  
- ✅ Download student files for a specific task  
- ✅ Automatically organises files into folders  
- ✅ Generates an Excel report with delivery status  
- ✅ Secure access via OAuth 2.0 with Google API  

## 🚀 How to use it  
### 1️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure Google credentials
Download the credentials.json file from the Google Cloud Console
Place it in the project's root folder

### 3️⃣ Start the script
```bash
python main.py
```

### 4️⃣ Customise class and task to download
Edit the following parameters within the main.py script
```bash
course_name = ‘Class Name’
coursework_name = ‘Name of the Task’
```

## 🛠️ Requirements
Python  3.11
Access to a Google Classroom account
Google Drive API enabled

## ⚠️ Notes
Make sure you have the necessary permissions on Google Classroom and Google Drive
First start-up will require authentication with a Google account
