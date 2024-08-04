import PyPDF2

def remove_pages(input_pdf_path, output_pdf_path, pages_to_remove):
    with open(input_pdf_path, 'rb') as input_file:
        reader = PyPDF2.PdfReader(input_file)
        writer = PyPDF2.PdfWriter()

        num_pages = len(reader.pages)

        for page_number in range(num_pages):
            if page_number not in pages_to_remove:
                writer.add_page(reader.pages[page_number])

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

# Example usage:
input_pdf_path = "D:/rotation_dataset/graph/pages_1_91.pdf" # Path to your input PDF file
output_pdf_path = 'D:/rotation_dataset/graph/graph-2.pdf'  # Path for the output PDF file
pages_to_remove = [0]  # List of page numbers to remove (0-indexed)

remove_pages(input_pdf_path, output_pdf_path, pages_to_remove)