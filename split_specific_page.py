import PyPDF2

def split_pdf(pdf_path, output_folder, pages_to_split):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for page_number in pages_to_split:
            # if page_number >= len(reader.pages):
            #     print(f"Page {page_number} does not exist in the PDF.")
            #     continue

            writer = PyPDF2.PdfWriter()
            writer.add_page(reader.pages[page_number - 1])

            output_path = f"{output_folder}/page_{page_number}.pdf"
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

pdf_path = r"D:\object_detection_collection\maths\TEY251 - IX - G9_MATHS_ANNUAL EXAMINATION _B - 4.pdf" # Path to your PDF file
output_folder = r"D:\object_detection_collection\maths"  # Folder where you want to save the split PDF pages
pages_to_split = [87]  # Specify the pages you want to split (0-indexed)

split_pdf(pdf_path, output_folder, pages_to_split)