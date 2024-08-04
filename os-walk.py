import os
import shutil

def collect_pdf_files(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def extract_and_save_pdf(pdf_files, destination_dir):
    for pdf_file in pdf_files:
        # Extract the file name from the full path
        file_name = os.path.basename(pdf_file)
        # Create the destination path
        destination_path = os.path.join(destination_dir, file_name)
        # Copy the PDF file to the destination directory
        shutil.copy(pdf_file, destination_path)
        # print(f"Extracted and saved: {destination_path}")

# Specify the source directory containing PDF files
source_directory_path = "D:/rotation_dataset/contour/schls"
# Specify the destination directory to save the extracted PDF files
destination_directory_path = "D:/rotation_dataset/contour/schl-pdf"

pdf_files = collect_pdf_files(source_directory_path)
extract_and_save_pdf(pdf_files, destination_directory_path)
