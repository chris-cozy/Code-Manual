# Python Debugger
Python comes with a built-in debugger tool.
It allows you to interactively explore variables within mid-operation of your Python code.
To use the Python debugger, use this statement at the top of your file:
*import pdb*

A trace will pause operations mid-script and allow you to mess with variables to understand what is going on. Similar to a break in gdb. Set your trace before the line with an error. To set a trace:
*pdb.set_trace()*

Once the trace is open, you can call variables to report/view their values. You can also perform operations on variables within the input box (e.g x + 2, 2 + 2)

To quit the debugger, type this in the input window:
*q*

For more information on general debugging techniques and more methods, check out the official documentation:
https://docs.python.org/3/library/pdb.html