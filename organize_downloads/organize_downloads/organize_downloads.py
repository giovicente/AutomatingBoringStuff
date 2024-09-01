import os.path
import shutil
import sys
from os import listdir
from os.path import isfile, join
from dotenv import load_dotenv


if __name__ == '__main__':
    # Load path to the downloads directory from the environment file
    load_dotenv()
    file_path = os.getenv('DOWNLOADS_FOLDER_PATH')
    # Iterate and get all files in the directory and add them to a list named 'files'
    files = [f for f in listdir(file_path) if isfile(join(file_path, f))]

    if len(files) == 0:
        print('There are no files to move in the source folder')
        sys.exit()

    file_list = []
    filetype_dict = {}

    # Check if file type is already in the dictionary, if not, create a new folder for that file type
    for file in files:
        filetype = file.split('.')[1]
        new_folder_name = ''

        if filetype not in filetype_dict:
            file_list.append(filetype)
            new_folder_name = file_path + '/' + filetype + '_folder'
            filetype_dict[str(filetype)] = str(new_folder_name)

        if os.path.isdir(new_folder_name):
            continue
        else:
            os.mkdir(new_folder_name)

    i = 1

    # Move the files to the respective folders
    # Surround duplicate file exception with a try-except block
    for file in files:
        try:
            src_path = file_path + '/' + file
            filetype = file.split('.')[1]
            if filetype in filetype_dict.keys():
                dest_path = filetype_dict[str(filetype)]
                shutil.move(src_path, dest_path)
                print(f'File {i}: {file} moved to {filetype_dict[filetype]}')
                i += 1
        except Exception as e:
            print(f'An error occurred while moving the file {file}: {e}')
