import os
import glob
import shutil
import re
import uuid

download_dir = os.path.join(os.path.expanduser("~"), "Downloads/*")
file_names = glob.glob(download_dir)

# File extension lists
documents = ['.pdf', '.docx', '.doc', '.txt', '.accdb', '.pptx', '.xls', '.csv']
media = ['.jpeg', '.jpg', '.svg', '.png', '.PNG', '.mp4', '.mp3']
setupFiles = ['.exe', '.msi', '.apk']
compressedFiles = ['.zip']

# Destination folder locations
Document_Location = 'C:/Users/daraa/Downloads/Documents'
Media_Location = 'C:/Users/daraa/Downloads/Media'
SetupFiles_Location = 'C:/Users/daraa/Downloads/SetupFiles'
CompressedFiles_Location = 'C:/Users/daraa/Downloads/CompressedFiles'
Misselaneous_Location = 'C:/Users/daraa/Downloads/Misselaneous'

for file in file_names:
    destination_folder = None

    if os.path.splitext(file)[1] in documents:
        destination_folder = Document_Location
    elif os.path.splitext(file)[1] in media:
        destination_folder = Media_Location
    elif os.path.splitext(file)[1] in setupFiles:
        destination_folder = SetupFiles_Location
    elif os.path.splitext(file)[1] in compressedFiles:
        destination_folder = CompressedFiles_Location
    elif re.match(r"\.[^.]*$", os.path.splitext(file)[1]):
        destination_folder = Misselaneous_Location

    if destination_folder:
        destination_path = os.path.join(destination_folder, os.path.basename(file))

        # Handle file name collisions
        while os.path.exists(destination_path):
            base_name, extension = os.path.splitext(destination_path)
            destination_path = f"{base_name}_{uuid.uuid4().hex[:8]}{extension}"

        os.makedirs(destination_folder, exist_ok=True)
        shutil.move(file, destination_path)
