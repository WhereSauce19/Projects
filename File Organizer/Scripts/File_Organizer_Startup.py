import os
from shutil import move
import JSON_Files_Reader as read

# JSON files.
extension_file = read.extension_file
directories_file = read.directories_file

ext_dict = read.read_extensions(extension_file)
dir_dict = read.read_directories(directories_file)

def file_organizer(files_dir, dest_dir, ext_dict):
    # listing files directory.
    files = os.listdir(files_dir)
    # Looping across files list.
    for file in files:
        name, ext = os.path.splitext(file)
        # Checking extension of file.
        if ext in ext_dict:        
            fold = ext_dict[ext]
            fold_dir = os.path.join(dest_dir, fold)
            exists_dir = os.path.join(fold_dir, file)
            file_dir = os.path.join(files_dir, file)
            # Creating relevant folder.
            if not(os.path.exists(fold_dir)):
                os.mkdir(fold_dir)
            # Checking if file already exists.
            if not(os.path.exists(exists_dir)):
                move(file_dir, fold_dir)
            else:
                counter = 1
                while True:
                    new_file = f"{name} ({counter}){ext}"
                    new_file_dir = os.path.join(files_dir, new_file)
                    exists_dir = os.path.join(fold_dir, new_file)
                    # Renaming file since it already exists.
                    if not(os.path.exists(exists_dir)):
                        os.rename(file_dir, new_file_dir)
                        move(new_file_dir, fold_dir) 
                        break
                    else:
                        counter += 1
                        continue

for file_dir, dest_dir in dir_dict.items():
    file_organizer(file_dir, dest_dir, ext_dict)