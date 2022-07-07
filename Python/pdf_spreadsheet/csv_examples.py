# import csv - Importing the built-in library
# open() - Opening a csv file
    # A common error is that default encoding may fail due to special characters present in the file
    # To sove this, add an encoding argument when opening the file. You can search online for the different encodings
# csv.reader() - Read the data in csv format
    # You can specify the delimiter according to the file's syntax
# list() - Transfer the data into a python list. This will create a list of lists.
    # Each sublist is a data row/entry. Very first row will be column names.
import csv
raw_file = open("pdf_spreadsheet\examples\example.csv", encoding = "utf-8")
csv_data = csv.reader(raw_file)
data_lines = list(csv_data)


# Accessing a specific row
# Accessing a specific value
print(data_lines[10])
print(data_lines[10][3])

# Example - Extracting a column (all emails)
    # Starting at index 1 to avoid the column name
all_emails = []
for line in data_lines[1:15]:
    all_emails.append(line[3])
print(all_emails)

# Example - Extracting and manipulating multiple columns to get desired data (Combining first and last names to get full)
full_names = []
for line in data_lines[1:15]:
    full_names.append(line[1] + " " + line[2])
print(full_names)


# Writing to .csv file
    # Specify the mode and that newline is empty string
        # 'w' to overwrite the file
        # 'a' to add to the file
# csv.writer ()
    # ',' as delimeter
# With the writer, you can either write a single row or multiple rows
    # writerow()
        # Takes in a list
    # writerows()
        # Takes in a list of lists
output_file = open("pdf_spreadsheet\\examples\\test_output.csv", mode = 'w', newline = '')
writer = csv.writer(output_file, delimiter= ',')
output_file.close()