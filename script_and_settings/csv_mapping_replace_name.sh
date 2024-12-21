#!/bin/bash
csv_path="${1}"
folder_path="${2}"

# Open the csv_path and read it line by line to get the name of the file and the new name
while read line ; do 
    # Split the line by comma
    IFS=',' read -r -a array <<< "$line"
    # Remove the 換行符號 from array
    array=("${array[@]//[$'\r']}")
    # Get the name of the file
    file_name="${array[0]}"
    # Get the new name
    new_name="${array[1]}"
    # Replace the name of the file with the new name
    python /home/ymj1123/generative_agents_chinese/script_and_settings/replace_name.py --folder "$folder_path" --name2replace "$file_name" --new_name "$new_name"
done < "$csv_path"




