# This module is very useful. It allows you to do things like get the current working directory or list all of the files in a directory. 
# The commands work on all operating systems.
import os
import shutil

#Get the current working directory
os.getcwd()

#List items in directory
    # By default it will be the current directory
    # You can pass another directory as an argument to get the items in there
    # Can be useful - example: a for loop to open all files in a directory
os.listdir()
os.listdir('c:\\Users\\')

# There are 3 methods for deleting a file - cannot be reversed
    # They are operating at the command line, so it isn't like sending a file to the trash
    # Permanent removal
# Unlink - deletes a file at the provided path
# Rmdir - deletes a folder (must be empty) at the provided path
# Rmtree (shutil) - deletes all files and folders contained in the path. Most dangerous
# Because these removal methods are dangerous, it may be better to use the send2trash module
    # pip install send2trash
    # send2trash.send2trash(file/path)
os.unlink(path)
os.rmdir(path)
shutil.rmtree(path)

# Walk - yields a tuple for each directory in the current or specified dir
    # dirpath, dirname, filenames
    # Very useful
for folder, subfolders, files in os.walk(path):
    print(f"Currently looking at {folder}")

    print("The subfolders are: ")
    for subfolder in subfolders:
        print(f"Subfolder: {subfolder}")
    
    print("The files are: ")
    for file in files:
        print(f"File: {file}")