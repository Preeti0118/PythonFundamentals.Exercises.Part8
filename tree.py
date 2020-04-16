import os

from glob import glob

file_path = '/Users/psehgal/dev/PythonFundamentals.Exercises.Part8'


path = input('Enter a directory name - ')
directory_name = os.walk(path)
for path_name, subdirc_name, file_name in directory_name:
    print(path_name, subdirc_name,file_name)
    for var_file in file_name:
        print(os.path.join(path_name, var_file))


def walk(dirname, file_handler):
    items = os.listdir