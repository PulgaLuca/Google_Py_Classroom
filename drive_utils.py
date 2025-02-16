import os
import re
from googleapiclient.http import MediaIoBaseDownload

def sanitize_filename(filename):
    """Rimuove caratteri non validi per il filesystem dai nomi dei file."""
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def download_drive_file(drive_service, file_id, student_folder):
    try:
        file_metadata = drive_service.files().get(fileId=file_id, fields="name").execute()
        filename = sanitize_filename(file_metadata['name'])
        filepath = os.path.join(student_folder, filename)

        with open(filepath, 'wb') as f:
            request = drive_service.files().get_media(fileId=file_id)
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                if status:
                    print(f"Download {filename}: {int(status.progress() * 100)}%.")
        return filepath
    except Exception as e:
        print(f"Failed to download file {file_id}: {e}")
        return None
