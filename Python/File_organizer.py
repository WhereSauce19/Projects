import os
from shutil import move
from tkinter import messagebox

def extensions_folders():
    dict = {}
    with open("extensions and folders.txt", 'r') as file:
        for line in file.readlines():
            line = line.strip()
            if not(line.startswith('#')):
                ext,fold = line.split('|')
                dict[ext] = fold
    return dict

def file_directories(dest_dir):
    with open("file directories.txt", 'r') as file:
        for line in file.readlines():
            direc = ""
            line = line.strip()
            for char in line:
                if char == "\\":
                    char = char *2
                direc += char
            organize_files(direc, dest_dir)

def organize_files(files_dir, dest_dir):
    # listing files directory.
    files = os.listdir(files_dir)
    # Extensions and relevant folders.
    ext_fold = {}
    try:
        # Reading extensions and folders from text file.
        ext_fold = extensions_folders()
    except FileNotFoundError:
        # Handling file if it dosen't exist
        file = open("extensions and folders.txt", 'w')
        file.close()
        messagebox.showinfo("File Created", f"extensions and folders.txt file created at {os.getcwd()}")
        # Rereading the extensions and folder from text file.
        ext_fold = extensions_folders()

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

try:
    # Reading file directories from text file.
    file_directories("C:\\Users\\sanit\\Videos")
except FileNotFoundError:
    # Handling file if it dosen't exist.
    file = open("file directories.txt", 'w')
    file.close()
    messagebox.showinfo("File Created", f"file directories.txt file created at {os.getcwd()}")
    # Rereading the file directories from text file.
    file_directories("C:\\Users\\sanit\\Videos")
