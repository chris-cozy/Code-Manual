#This module is useful for moving files around
import shutil

# Moves a file
    # Takes two main params - the src file/folder, and the dest folder
    # Similar to the unix 'mv' command
    # You need to correct permissions to use this
shutil.move('test.txt', 'c:\\Users\\cjsan\\Documents')

# Rmtree
    # deletes all files and folders contained in the path. Very dangerous
shutil.rmtree(path)