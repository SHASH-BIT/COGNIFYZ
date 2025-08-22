import os
import shutil

# Path to the Downloads folder (change if needed)
source_folder = r"C:\Users\Shashwata\Downloads"
destination_folder = r"C:\Users\Shashwata\Downloads\Organized"

# Create destination folder if not exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
}

# Function to organize files
def organize_files():
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # Skip if it's a folder
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(file_name)

        moved = False
        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(destination_folder, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file_name))
                print(f"Moved: {file_name} → {folder_name}")
                moved = True
                break

        # If no match, move to "Others"
        if not moved:
            target_folder = os.path.join(destination_folder, "Others")
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file_name))
            print(f"Moved: {file_name} → Others")

# Run the script
organize_files()
print("✅ All files organized successfully!")
