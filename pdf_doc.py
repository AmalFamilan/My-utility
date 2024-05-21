import PyPDF2
from docx import Document
import os
def pdf_to_text(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfFileReader(f)
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
    return text

def text_to_doc(text, output_file):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(output_file)

def pdf_to_doc(pdf_file, output_file):
    text = pdf_to_text(pdf_file)
    text_to_doc(text, output_file)

# Example usage:
pdf_list = "D:/Renuga report/final year report  (1).pdf"



output_file = "D:/Renuga report/final year report  (1).docx"
pdf_to_doc(pdf_list, output_file)
