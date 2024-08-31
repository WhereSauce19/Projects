import os
from shutil import move
from tkinter import messagebox

# Getting the Documents directory of computer.
text_files_path = "~\\Documents\\File Organizer (files)"
text_files_path = os.path.expanduser(text_files_path)
# Creating a folder for text files if it dose'nt exist.
if not(os.path.exists(text_files_path)):
    os.mkdir(text_files_path)

# Creating extension and folder Dictionary.
def read_ext_fold():
    file_name = "ext_fold.txt"
    ext_fold_path = os.path.join(text_files_path, file_name)
    dict1 = {}
    # Creating the text file if it dose'nt exist.
    if not(os.path.exists(ext_fold_path)):
        file = open(ext_fold_path, 'w')
        file.close()
        messagebox.showinfo("File Created", f"ext_fold.txt file created at {text_files_path}")
    # Reading the text file for extensions and relevant folders.
    with open(ext_fold_path, 'r') as ext_fold_file:
        for line in ext_fold_file.readlines():
            line = line.strip()
            # To only fnd the extensions.
            if line.startswith('.'):
                ext, fold = line.split('|')
                dict1[ext] = fold
    # Returning the created Dictionary.
    return dict1

# Calling function to get Dictionary of extensions and folders.
ext_fold = {}
ext_fold = read_ext_fold()

# Function for organizing files.
def file_organizer(files_dir, dest_dir):
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

def read_directories(directory_file_path):
    # Opening directories file for reading.
    directories_file = open(directory_file_path, 'r')
    # Reading the default destination directory.
    default_des_dir = directories_file.readline().strip().split('=')[1]
    file_dir = ""
    dest_dir = ""
    directories = {}
    # Reading directories file for file directories and destination directories.
    for line in directories_file.readlines():
        line = line.strip()
        # Checking if line has a destination directory.
        if (line.startswith('>')) and ('|' in line):
            file_dir, dest_dir = line.split('|')
            file_dir = file_dir.removeprefix('>')
        # Checking if line dose'nt have a destination directory.
        elif (line.startswith('>')) and ('|' not in line):
            file_dir = line
            file_dir = file_dir.removeprefix('>')
            # Using the default destination directory.
            dest_dir = default_des_dir
        # Adding file directories and relevant destination directories to Dictionary. 
        directories[file_dir] = dest_dir
    # Closing the directories file.
    directories_file.close()
    # Returning the directories Dictionary.
    return directories

directories_file_name = "directories.txt"
directories_file_path = os.path.join(text_files_path, directories_file_name)
try:
    # Using the Dictionary's directories to organize files.
    for file_dir, dest_dir in read_directories(directories_file_path).items():
        file_organizer(file_dir, dest_dir)
except:
    # Creating directories file if it dose'nt exist.
    with open(directories_file_path, 'w') as directories_file:
        directories_file.write("Default destination directory =")
        messagebox.showerror("Directory not found.", f"The relevant directories were not found at {directories_file_path}")
