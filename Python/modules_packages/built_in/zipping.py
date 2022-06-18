# Zipping and Unzipping files in python
# Zipping is a way to compress a file
# Creating and zipping individual files. You create a zip file, then select individual files to insert to it
f = open('test_one.txt', 'w+')
f.write('One File')
f.close()

f = open('test_two.txt', 'w+')
f.write('Two File')
f.close()

import zipfile
comp_file = zipfile.Zipfile('comp_test.zip', 'w')
comp_file.write('test_one.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('test_two.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.close()

# Extracting an object from a zip file
# If looking for a specific file, use extract(*file to extract*)
# To extract everything, use extractall(*path to extract to*)
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')


# You can use the SHUTIL module to archive/extract entire directories
# Can also choose to make it a tar file
    # make_archive(new dir name, archive type, original dir path)
    # unpack_archive(zipped dir to unpack, new dir name, archove type)
import shutil
dir = 'path of directory to zip'
shutil.make_archive('example', 'zip', dir)

shutil.unpack_archive('example.zip', 'unzipped_directory', 'zip')