import PyPDF2

def split_pdf(pdf_path, output_folder):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for page_number in range(num_pages):
            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_number])
            
            output_path = f"{output_folder}/page_{page_number + 1}.pdf"
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

pdf_path = "D:/rotation_dataset/maps/LMMS_6F_SS_2402.pdf"  # Path to your PDF file
output_folder = "D:/rotation_dataset/maps/New folder"  # Folder where you want to save the split PDF pages

split_pdf(pdf_path, output_folder)
