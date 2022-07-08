# PDF
PDF stands for Portable Document Format. It was developed by Adobe in the 1990s. 

## PDFs in Python
Many PDFs are not machine readable through python, because they mainly encapsulate and display a fixed-layout flat document. This is unlike CSV files. It means that a pdf that was simply scanned is unlikely to be readable in python.
Additions to pdfs such as images, tables, etc can also render a pdf unreadable by python.
The *PyPDF2* library is an open-source, free library that can be used to read pdfs with python. Not all pdfs will be readable by the library.
There are also other libraries that can read PDFs.
It is only possible to read from PDFs, writing to them will often generate errors.
- You can add pages though
### Installing Libraries
*pip install PyPDF2*