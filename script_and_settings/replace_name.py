import os
import argparse

def replace_in_file(file_path, name2replace, new_name):
    encodings = ['utf-8', 'latin1', 'utf-16']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeDecodeError(f"Unable to decode file {file_path} with available encodings.")
    
    content = content.replace(name2replace, new_name)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def replace_in_folder(folder, name2replace, new_name):
    for root, dirs, files in os.walk(folder, topdown=False):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if name2replace in file_name:
                new_file_name = file_name.replace(name2replace, new_name)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(file_path, new_file_path)
                file_path = new_file_path
            replace_in_file(file_path, name2replace, new_name)
        
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if name2replace in dir_name:
                new_dir_name = dir_name.replace(name2replace, new_name)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(dir_path, new_dir_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Replace text in files and filenames.')
    parser.add_argument('--folder', required=True, help='Folder to search for files')
    parser.add_argument('--new_name', required=True, help='New name to replace with')
    parser.add_argument('--name2replace', required=True, help='Name to be replaced')

    args = parser.parse_args()

    replace_in_folder(args.folder, args.name2replace, args.new_name)