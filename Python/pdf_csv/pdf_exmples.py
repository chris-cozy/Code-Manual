# Import library
# open() - Open pdf file
    # Mode will be 'rb'
# PyPDF2.PdfFileReader() - Convert into a PyPDF2 object
    # numPages - attribute
    # getPage() - get page at index
        # Returns a page object, so set equal to a variable
        # extractText() - Returns the text on the page as a Python string
            # If an empty string is returned, the pdf file is not compatible with PyPDF2
# Opening and reading a pdf
import PyPDF2
file = open("pdf_csv\examples\Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(file)

print(pdf_reader.numPages)

page1 = pdf_reader.getPage(0)
page1_text = page1.extractText()

print(page1_text)

file.close()

# Adding page to pdf
# PdfFileWriter() - create a writer object
    # addPage() - Adds a page to the write queue. Has to be a pdf page object
    # write() - Writes the queue to the output file entered as argument.
# open() - Open the file to write to
    # Mode = 'wb'
file = open("pdf_csv\examples\Working_Business_Proposal.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(file)
page1 = pdf_reader.getPage(0)

pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page1)

out_file = open("pdf_csv\examples\New_File.pdf", 'wb')
pdf_writer.write(out_file)

file.close()
out_file.close()


