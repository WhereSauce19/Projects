import os
from shutil import move

def organize_files(files_directory, dest_directory):
    # listing files directory
    files = os.listdir(files_directory)
    # Extensions and relevant folders
    ext_fold = {
                # Documents
                ".pdf":"Documents",
                ".docx":"Documents",
                ".doc":"Documents",
                ".pptx":"Documents",
                ".xlsx":"Documents",
                ".rtf":"Documents",
                ".zip":"Documents",
                ".rar":"Documents",
                ".txt":"Documents",
                # Images
                ".png":"Images",
                ".jpeg":"Images",
                ".jpg":"Images",
                ".bmp":"Images",
                # Videos
                ".mkv":"Videos",
                ".mp4":"Videos",
                # Audio
                ".mp3":"Audio"
                }

    # Looping across files list
    for file in files:
        name, ext = os.path.splitext(file)
        # Checking extension of file
        if ext in ext_fold:
            fold = ext_fold[ext]
            fold_dir = os.path.join(dest_directory, fold)
            exists_dir = os.path.join(fold_dir, file)
            file_dir = os.path.join(files_directory, file)
            # Creating relevant folder
            if not(os.path.exists(fold_dir)):
                os.mkdir(fold_dir)
            # Checking if file already exists
            if not(os.path.exists(exists_dir)):
                move(file_dir, fold_dir)
            else:
                counter = 1
                while True:
                    new_file = f"{name} ({counter}){ext}"
                    new_file_dir = os.path.join(files_directory, new_file)
                    exists_dir = os.path.join(fold_dir, new_file)
                    # Renaming file since it already exists
                    if not(os.path.exists(exists_dir)):
                        os.rename(file_dir, new_file_dir)
                        move(new_file_dir, fold_dir)
                        break
                    else:
                        counter += 1
                        continue
