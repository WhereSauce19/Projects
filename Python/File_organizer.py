import os
from shutil import move
from tkinter import messagebox

# Getting the Documents directory of computer.
text_files_path = "~\\Documents\\File Organizer(files)"
text_files_path = os.path.expanduser(text_files_path)
# Creating a folder for text files if it dose'nt exist.
if not(os.path.exists(text_files_path)):
    os.mkdir(text_files_path)
# Creating extension and folder Dictionary.
def read_ext_fold():
    file_name = "ext_fold.txt"
    ext_fold_path = os.path.join(text_files_path, file_name)
    dict1 = {}
    # Checking if file already exists.
    try:
        with open(ext_fold_path, 'r') as file:
            for line in file.readlines():
                line = line.strip()
                if not(line.startswith('#')):
                    ext, fold = line.split('|')
                    dict1[ext] = fold
    # Handling exception if file dose'nt exist.
    except FileNotFoundError:
        file = open(ext_fold_path, 'w')
        file.close()
        messagebox.showinfo("File Created", f"ext_fold.txt file created at {text_files_path}")
    # Returning the created Dictionary .
    return dict1

# Initializing read_ext_fold function.
ext_fold = {}
ext_fold = read_ext_fold()

def organize_files(files_dir, dest_dir):
    # listing files directory.
    files = os.listdir(files_dir)
    # Looping across files list.
    for file in files:
        name, ext = os.path.splitext(file)
        # Checking extension of file.
        if ext in ext_fold:
            fold = ext_fold[ext]
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

# Reading file_directories from text file.
def read_file_dir():
    file_name = "file_dir.txt"
    file_dir_path = os.path.join(text_files_path, file_name)
    file_directory_list = []
    # Checking if file already exists.
    try:
        with open(file_dir_path, 'r') as file:
            for line in file.readlines():
                file_directory = line.strip()
                # Checking if file directory already exist.
                try:
                    file_directory_list.index(file_directory)
                # Appending directory if it dose'nt exist.
                except ValueError:
                    file_directory_list.append(file_directory)
    # Handling exception if file dose'nt exist.
    except FileNotFoundError:
        file = open(file_dir_path, 'w')
        file.close()
        messagebox.showinfo("File Created", f"file_dir.txt file created at {text_files_path}")
    # Returning directories by a list.
    return file_directory_list

# Destination directory.
dest_dir = "Destination directory goes here"
# Looping over the directories list:
for file_directory in read_file_dir():
    # Organizing files.
    organize_files(file_directory, dest_dir)
