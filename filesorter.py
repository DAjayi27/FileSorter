import os
import glob
import shutil
import re
import uuid
from pathlib import Path
from logger import logCreation
from tqdm import tqdm

def is_folder_empty(folder_path):
    return len(os.listdir(folder_path)) == 0


download_dir = os.path.join(os.path.expanduser("~"), "Downloads/*")

file_names = glob.glob(download_dir,recursive=True)


# File extension lists for each category

documents_ext = ['.pdf', '.doc', '.docx', '.txt', '.odt', '.xls', '.xlsx', '.ppt', '.pptx', '.csv']
photos_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
music_ext = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a']
videos_ext = ['.mp4', '.mkv', '.mov', '.avi', '.wmv', '.flv']
zip_files_ext = ['.zip', '.rar', '.7z', '.tar', '.gz']
miscellaneous_ext = ['.exe', '.apk', '.iso', '.bak', '.tmp']

# Destination folder locations
Document_Location = 'C:/Users/daraa/Downloads/Documents_2'
Photos_Location = 'C:/Users/daraa/Downloads/Images_2'
Video_Location = 'C:/Users/daraa/Downloads/Video_2'
Audio_Location = 'C:/Users/daraa/Downloads/Audio_2'
SetupFiles_Location = 'C:/Users/daraa/Downloads/SetupFiles_2'
CompressedFiles_Location = 'C:/Users/daraa/Downloads/CompressedFiles_2'
Misselaneous_Location = 'C:/Users/daraa/Downloads/Misselaneous_2'


excluded_folders = [Document_Location,Photos_Location,Video_Location,Audio_Location,SetupFiles_Location,CompressedFiles_Location,Misselaneous_Location]

# Normalize excluded folder paths for accurate comparison
excluded_folders = [os.path.abspath(folder) for folder in excluded_folders]



for file in   tqdm(file_names, desc="Processing files") :
    
    if os.path.isdir(file) or any(os.path.commonpath([file, folder]) == folder for folder in excluded_folders) :
        continue
    
    
    destination_folder = None

    if Path(file).suffix in documents_ext:
        destination_folder = Document_Location
    elif Path(file).suffix in photos_ext:
        destination_folder = Photos_Location
    elif Path(file).suffix in music_ext:
        destination_folder = Audio_Location
    elif Path(file).suffix in videos_ext:
        destination_folder = Video_Location
    elif Path(file).suffix in zip_files_ext:
        destination_folder =  CompressedFiles_Location
    else:
        destination_folder = Misselaneous_Location

    if destination_folder:
        destination_path = os.path.join(destination_folder, os.path.basename(file))

        # Handle file name collisions
        if os.path.exists(destination_path):
            base_name, extension = os.path.splitext(destination_path)
            destination_path = f"{base_name}_{uuid.uuid4().hex[:8]}{extension}"
        
        if not os.path.isdir(destination_folder):
            logCreation(f"The directory '{destination_folder}' was created by the program")
            os.makedirs(destination_folder)
        
        shutil.move(file, destination_path)

    
        
# cleanup empty folders 

for file in tqdm(file_names, desc="Deleting Empty Folders"):
    if os.path.isdir(file) and is_folder_empty(file):
        os.rmdir(file)
        
