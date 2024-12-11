import os
import re
from opencc import OpenCC

cc = OpenCC('s2tw')
simplified_chinese_regex = re.compile(r'[\u4e00-\u9fff]')
target_extensions = {'.py', '.json', '.txt', '.csv'}
log_file = "detected_files.txt"

def contains_simplified_chinese(text):
    """
    Check if the text contains Simplified Chinese characters.
    """
    return bool(simplified_chinese_regex.search(text))

def transform_file(filepath):
    """
    Transform Simplified Chinese parts in a file to Traditional Chinese.
    Only modifies files if Simplified Chinese is found.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    modified = False
    transformed_lines = []

    for line in lines:
        if contains_simplified_chinese(line):
            transformed_line = cc.convert(line)
            transformed_lines.append(transformed_line)
            modified = True
        else:
            transformed_lines.append(line)

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(transformed_lines)
        return True
    return False

def scan_directory(directory):
    """
    Scan through the directory for files with the target extensions.
    Detect and transform files containing Simplified Chinese.
    """
    with open(log_file, 'w', encoding='utf-8') as log:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()

                if file_extension in target_extensions:
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()

                        if contains_simplified_chinese(content):
                            log.write(f"{file_path}\n")
                            if transform_file(file_path):
                                print(f"Transformed: {file_path}")
                    except (UnicodeDecodeError, IOError) as e:
                        print(f"Error reading file {file_path}: {e}")

if __name__ == "__main__":
    # Specify the directory to scan
    directory_to_scan = input("Enter the directory to scan: ")
    scan_directory(directory_to_scan)
    print(f"Scanning completed. Detected file paths logged in {log_file}.") 