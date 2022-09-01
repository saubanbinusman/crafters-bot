import os
import textract



file_names = os.listdir("data")

text = textract.process('data/book1.pdf', method='tesseract')

print(text)

# pdfFileObj = open('data/book1.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF3.PdfFileReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(pdfReader.numPages)
#
# # creating a page object
# pageObj = pdfReader.getPage(100)
#
# # extracting text from page
# okay = pageObj.extractText()
# escaped = re.escape(okay)
# print(okay)
#
# # closing the pdf file object
# pdfFileObj.close()