# Testing
There are several testing tools for python:

## Pylint
A library that looks at your code and reports back possible issues

Install using:
    pip install pylint

Within the pylint repo is a file named bad_script.py, which is written with a purposeful mistake. This file can be used with pylint as an example. Another file is also included, named good_script.py. These are to serve as contrasting examples.

To use pylint, use the command:
    pylint *script_name*
To view a report, use the command:
    pylint *script_name* -r y

After running the command, you will recieve a list of notes. The notes preceded with an E, such as E0602, are errors.
The report will contain a list of statistics for your code, and at the end, a grade for your code.


## Unittest
A built-in library that allows you to test your own programs and check if you are getting desired outputs

In the Unittest repo, there is a script named script.py, which contains a basic function. There is another script named test_script.py. This script serves as the tester.

To use unittest, create a separate script for testing. Import the unittest library, as well as the script to be tested. Create a testing class, then define your functions within. As shown in the example, the functions will be testing the script.

When writing test functions, it is best to go from simple to complex, as each function will be run in order.

Run the testing script to start the tests.

