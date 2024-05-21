import PyPDF2
import os

def merge_pdfs(pdf_list, output_path):
    merger = PyPDF2.PdfMerger()

    for pdf_file in pdf_list:
        merger.append(pdf_file)

    merger.write(output_path)
    merger.close()
    
# Example usage:
# pdf_list = []
# dir_path = r"D:\Projects\Quantum ML of BDS using randamize mesurements\familan changes"
# pdf = os.listdir(dir_path)
# for pdf in pdf_list:
#     pdf_path = os.path.join(dir_path,pdf)
#     pdf_list.append(pdf_path)

pdf_list = [ r"D:\Projects\Quantum ML of BDS using randamize mesurements\Final report Familan.pdf",r"D:\Projects\Quantum ML of BDS using randamize mesurements\Quantum machine learning of big dataset using randomized measurement paper .pdf",r"D:\Projects\Quantum ML of BDS using randamize mesurements\familan cirtificate.pdf"
] # List of PDF files to merge
output_path = r"D:\Projects\Quantum ML of BDS using randamize mesurements\familan .pdf"  # Path for the output merged PDF file

merge_pdfs(pdf_list, output_path)