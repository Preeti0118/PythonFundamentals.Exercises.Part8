import os
#import glob
from glob import glob
from os import path
import stat

#file_path = input('enter a file path - ')

file_path = '/Users/psehgal/dev/PythonFundamentals.Exercises.Part8'

#file_path = 'PythonFundamentals.Exercises.Part8'

#def getcontents(filename):
#
#    files = os.listdir(filename)
#
#    for name in files:
#        if path.isfile(name):
#            print ('./'+ name)
#        elif path.isdir(name):
#            getcontents(name)
#
#getcontents(file_path)

#for x in os.walk(file_path):
#    print(x[0])
#    files = os.listdir(x[0])
#    for name in files:
#        if path.isfile(name):
#            print(str(x[0])+'\\'+name)
#        elif path.isdir(name):
#            files1 = os.listdir(name)
#            for name1 in files1:
#                if path.isfile(name1):
#                    print(name1)

#paths = glob('*/')
#print (paths)


#for name in os.walk(file_path):
#    print(name)


#path = '/Users/psehgal/dev/PythonFundamentals.Exercises.Part8/'
path = input('Enter a directory name - ')
directory_name = os.walk(path)
for path_name, subdirc_name, file_name in directory_name:
    print(path_name, subdirc_name,file_name)
    for var_file in file_name:
         print(os.path.join(path_name, var_file))