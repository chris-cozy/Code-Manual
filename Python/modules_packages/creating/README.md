# Creating your own Modules and Packages
Modules are just .py scripts that you call in another .py script.

Packages are a collection of modules.

## Creating a module
In the files included in this repo, there is a module file and a program file. The module file is simply a python file containing a function we want to use in our program file.

To use a module/another python file in the same repo, use the line:
from *module_filename* import *func_name*

## Creating a package
There is a package repo in this repository, and a subpackage repo within that repo.
To register these repos as packages, create this file within each:
__init__.py

Within each repo, mypackage and subpackage, there is a python script containing the functions we want to use in the program. As long as the repos contain the __init__.py file they can be treated as packages.

To use a package in the same repo, use the line:
from *package_name* import *script_name*
from *package_name*.*subpackage_name* import *script_name*

To call functions from these scripts:
*script_name*.*function_name*