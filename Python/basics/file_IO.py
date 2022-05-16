#Opening a text file in the current directory
#Opening a text file anywhere on the computer
#If the file doesn't already exist it will be created
test_file1 = open('filename.txt')
test_file2 = open("C: \\Users\\UserName\\Folder\\filename.txt")

#Built-in functions
#read - reads through the file, displays \n wherever there is a new line. Returns a string with file contents
    # If you call it again it will return an empty string, because the 'cursor' is already at the end of the file. 
    # To reset the 'cursor', use .seek(0)
#readlines - makes each line into a separate object. Returns a list of the lines
#seek - places the read curser of the desired line
#write - write a line to a file
#close - closes the file once done. very important
test_file1.read()
test_file1.seek(0)
test_file1.readlines()
test_file1.close()

test_file2.write("This is a test string to write to the file.")
test_file2.close()

#Can use a with-as statment to easily grab file contents. Using close is not necessary
with open('filename.txt') as test_file3:
    contents = test_file3.read()

#Can set the mode of a file as well
with open('filename.txt', mode = 'a') as test:
    test.write('Four on fourth')

#Another way to do this
test_file4 = open('filename.txt','w')
test_file4.write('Hello World')
test_file4.close()

#By using Shift+Tab right after open and before the file name you can access the File's information, such as the mode, which can be equal to:
        #'r' (read)
        #'w' (write or create new files)
        #'a' (append)
        #'r+' (read and write)
        #'w+" (write and read or create new files)

