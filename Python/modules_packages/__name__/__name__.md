# __name__ and __main__

At the bottom of large scripts there may often be a mysterious code line:
if __name__ == "__main__":
    - block of code

Sometimes when importing from a module you would like to know whether a module's function is being used as an import, or if it is the original .py file that is being run.

## __name__
__name__ is a built in variable that gets assigned a string depending on how the script is being run. If the script is being run directly, from the command line, __name__ will have a value of '__main__'

If the script is an import to another file that is being run directly, __name__ will have another value.