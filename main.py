#!/usr/bin/env python3
import os
import shutil

username = 'adamflorez'
# Path to your desktop (change 'your_username' to your actual user name)
desktop_path = f'/Users/{username}/Desktop'
# Destination path for organized folders
organized_path = f'/Users/{username}/Desktop/Organized'
# Ensure the destination path exists
os.makedirs(organized_path, exist_ok=True)
# List all files on the desktop
for file_name in os.listdir(desktop_path):
    # Ignore directories and this script itself
    if not os.path.isfile(os.path.join(desktop_path, file_name)):
        continue
    # Get the file extension
    file_extension = file_name.split('.')[-1].lower()
    if file_extension == file_name:  # Handle files without an extension
        file_extension = 'NoExtension'
    # Folder path for this extension
    extension_folder = os.path.join(organized_path, file_extension)
    os.makedirs(extension_folder, exist_ok=True)
    # Move the file to its new folder
    shutil.move(os.path.join(desktop_path, file_name), os.path.join(extension_folder, file_name))

print("Files organized by extension.")
