import json
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import JSON_Files_Reader as read

extension_file = read.extension_file
directories_file = read.directories_file
icon_file = read.icon_file

# Dictionaries created by JSON files.
extensions_dict = read.read_extensions(extension_file)
folders = list(set(extensions_dict.values()))
directories_dict = read.read_directories(directories_file)

# Dimensions of main window.
WIDTH = 300
HEIGHT = 400
main_window = tk.Tk()
main_window.title("File Organizer")
if os.path.exists(icon_file):
    icon = tk.PhotoImage(file=icon_file)
    main_window.iconphoto(True, icon)
main_window.geometry(f"{WIDTH}x{HEIGHT}")
main_window.resizable(False, False)

notebook = ttk.Notebook(main_window)
notebook.pack(expand=True, 
              fill="both")

def display_listbox(dictionary, listbox, want):
    listbox.delete(0, tk.END)
    if want:
        dictionary = {key: value for key, value in sorted(dictionary.items(), key=lambda item:item[1])}
    for key, value in dictionary.items():
        item = f">>{key}-->{value}"
        listbox.insert(tk.END, item)

# Frame for extensions.
extension_frame = ttk.Frame(notebook)
notebook.add(extension_frame, 
             text="Extensions")

ext_title = ttk.Label(extension_frame, 
                      text="Add Extensions", 
                      font=("Consolas", 25, 'bold'))
ext_title.pack()

folder_select = ttk.Combobox(extension_frame, 
                             values=folders)
folder_select.place(x=70, y=70)
folder_select_label = ttk.Label(extension_frame, 
                                text="Select folder:", 
                                font=("Consolas", 11))
folder_select_label.place(x=90, y=45)

ext_input = ttk.Entry(extension_frame, 
                      font=("Consolas", 10))
ext_input.place(x=70, y=120)
ext_input_label = ttk.Label(extension_frame, 
                            text="Enter extension:", 
                            font=("Consolas", 11))
ext_input_label.place(x=74, y=95)

def add_ext():
    fold = folder_select.get()
    ext = ext_input.get()
    if not((fold == "") or (ext == "")):
        if not(ext.startswith('.')):
            ext = f".{ext}"
        extensions_dict.update({ext:fold})
        with open(extension_file, 'w') as file:
            json.dump(extensions_dict, file, indent=2)
        display_listbox(extensions_dict, ext_listbox, True)
        ext_input.delete(0, tk.END)
    elif (fold == "") and (ext == ""):
        messagebox.showerror("Error", "Entries are empty.")
    elif fold == "":
        messagebox.showerror("Error", "Folder cannot be empty.")
    elif ext == "":
        messagebox.showerror("Error", "Extension cannot be empty.")
        
def remove_ext():
    selected_index = ext_listbox.curselection()
    if selected_index:
        selected = str(ext_listbox.get(selected_index[0]))
        ext = selected.split("-->")[0]
        ext = ext.replace('>', '')
        del extensions_dict[ext]
        with open(extension_file, 'w') as file:
            json.dump(extensions_dict, file, indent=2)
        display_listbox(extensions_dict, ext_listbox, True)

add_ext_button = ttk.Button(extension_frame, 
                            text="Add Extension", 
                            command=add_ext)
add_ext_button.place(x=100, y=150)


ext_listbox = tk.Listbox(extension_frame, width=45)
ext_listbox.place(x=10, y=180)
display_listbox(extensions_dict, ext_listbox, True)

remove_ext_button = ttk.Button(extension_frame, 
                            text="Remove Extension", 
                            command=remove_ext)
remove_ext_button.place(x=90, y=347)

# Frame for directories.
directory_frame = ttk.Frame(notebook)
notebook.add(directory_frame, text="Directories")

dir_title = ttk.Label(directory_frame, 
                      text="Add Directories", 
                      font=("Consolas", 25, 'bold'))
dir_title.pack()

    # File directory widgets.
def get_file_dir():
    file_dir = filedialog.askdirectory()
    file_dir_entry.delete(0, tk.END)
    file_dir_entry.insert(0, file_dir)

file_dir_label = ttk.Label(directory_frame, 
                           text="Select file directory:", 
                           font=("Consolas", 11))
file_dir_label.place(x=65, y=45)

file_dir_entry = ttk.Entry(directory_frame, 
                           font=("Consolas", 10))
file_dir_entry.place(x=50, y=70)

file_dir_button = ttk.Button(directory_frame, 
                             text="Browse", 
                             command=get_file_dir)
file_dir_button.place(x=200, y=68)

    # Destination directory widgets.
def get_dest_dir():
    dest_dir = filedialog.askdirectory()
    dest_dir_entry.delete(0, tk.END)
    dest_dir_entry.insert(0, dest_dir)

dest_dir_label = ttk.Label(directory_frame, 
                           text="Select destination directory:", 
                           font=("Consolas", 11))
dest_dir_label.place(x=10, y=95)

dest_dir_entry = ttk.Entry(directory_frame, 
                           font=("Consolas", 10))
dest_dir_entry.place(x=50, y=120)

dest_dir_button = ttk.Button(directory_frame, 
                             text="Browse", 
                             command=get_dest_dir)
dest_dir_button.place(x=200, y=118)

def add_dir():
    file_dir = file_dir_entry.get()
    dest_dir = dest_dir_entry.get()
    if not(os.path.exists(dest_dir)) and (dest_dir != ""):
        os.makedirs(dest_dir)
    elif dest_dir == "":
        messagebox.showerror("Error", "Destination path cannot be empty.")
        return
    if os.path.exists(file_dir):
        directories_dict.update({file_dir:dest_dir})
        with open(directories_file, 'w') as file:
            json.dump(directories_dict, file, indent=2)
        file_dir_entry.delete(0, tk.END)
        dest_dir_entry.delete(0, tk.END)
    elif file_dir == "":
        messagebox.showerror("Error", "File path cannot be empty.")
    elif not(os.path.exists(file_dir)):
        messagebox.showerror("Error", "File path does not exist.")
        file_dir_entry.delete(0, tk.END)
    display_listbox(directories_dict, dir_listbox, False)

add_dir_button = ttk.Button(directory_frame, 
                            text="Add Directory", 
                            command=add_dir)
add_dir_button.place(x=100, y=150)

def remove_dir():
    selected_index = dir_listbox.curselection()
    if selected_index:
        selected = str(dir_listbox.get(selected_index[0]))
        f_dir = selected.split("-->")[0]
        f_dir = f_dir.replace('>', '')
        del directories_dict[f_dir]
        with open(directories_file, 'w') as file:
            json.dump(directories_dict, file, indent=2)
        display_listbox(directories_dict, dir_listbox, False)

dir_listbox = tk.Listbox(directory_frame, width=45)
dir_listbox.place(x=10, y=180)
display_listbox(directories_dict, dir_listbox, False)

remove_dir_button = ttk.Button(directory_frame, 
                            text="Remove Directory", 
                            command=remove_dir)
remove_dir_button.place(x=90, y=347)

main_window.mainloop()