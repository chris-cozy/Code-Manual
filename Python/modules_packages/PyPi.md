
There are many other libraries available that people have open-sourced and shared on PyPi. PyPi is a repository for open-source third-party Python packages. It's similar to RubyGems for Ruby, or NPM for Node.js.

We use 'pip install' at the command line to install third-party packages from PyPi.

There are packages available for almost any use case you can think of! You can google search to find package documentation, or a link to its PyPi page.

### What are packages?
Modules are just .py scripts that you call in another .py script.

Packages are a collection of modules.

### How to download and install external packages
Windows Users: Command Prompt
MacOS/Linux Users: Terminal

Your firewall may block pip from accessing the internet

On the command line:
pip install *package_name*

### To access packages from command line - example with the colorama package
run python with the command:
python

Once in the python env:
from colorama import init
init()
from colorama import Fore
print(Fore.RED + "some red text")

### Correctly google searching for packages
It's always best to start with a simple google search
'python package for ---'
Generally the first few results have recommended packages