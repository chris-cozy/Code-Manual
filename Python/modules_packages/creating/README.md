# Creating your own Modules and Packages
Modules are just .py scripts that you call in another .py script.

Packages are a collection of modules.

## Creating a module
In the files included in this repo, there is a module file and a program file. The module file is simply a python file containing a function we want to use in our program file.

To use a module/another python file in the same repo, use the line:
from *module_filename* import *func_name*

## Creating a package
There is also a package folder in this repository. There is also a subpackage folder within that folder.
To register these folders as directory, create this file within each:
__init__.py