import json
import os

# Documents path.
doc_path = "~\\Documents\\File Organizer"
doc_path = os.path.expanduser(doc_path)
if not(os.path.exists(doc_path)):
    os.makedirs(doc_path)
# JSON file names.
extension_file = f"{doc_path}\\Extensions.json"
directories_file = f"{doc_path}\\Directories.json"
icon_file = f"{doc_path}\\icon.png"

def read_directories(file_path):
    directories_dict = {}
    try:
        with open(file_path, 'r') as file:
            directories_dict = dict(json.load(file))
    except json.decoder.JSONDecodeError:
        pass
    except FileNotFoundError:
        pass

    wrong_dirs = [f_dir for f_dir, d_dir in directories_dict.items() if not(os.path.exists(f_dir)) or not(os.path.exists(d_dir))]
    for dirs in wrong_dirs:
        del directories_dict[dirs]
        
    with open(file_path, 'w') as file:
        json.dump(directories_dict, file, indent=2)
    return directories_dict

def read_extensions(file_path):
    extensions_dict = {}
    try:
        with open(file_path, 'r') as file:
            extensions_dict = dict(json.load(file))
    except json.decoder.JSONDecodeError:
        pass
    except FileNotFoundError:
        pass

    wrong_ext = [ext for ext in extensions_dict.keys() if not(ext.startswith('.'))]
    for ext in wrong_ext:
        fold = extensions_dict.pop(ext)
        correct_ext = f".{ext}"
        extensions_dict.update({correct_ext:fold})

    with open(file_path, 'w') as file:
        json.dump(extensions_dict, file, indent=2)
    return extensions_dict