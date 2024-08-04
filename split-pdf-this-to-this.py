import PyPDF2

def split_pdf(pdf_path, output_folder, page_ranges):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        for start, end in page_ranges:
            # if start < 0 or start >= num_pages or end < start or end >= num_pages:
            #     print(f"Invalid page range: {start}-{end}. Skipping.")
            #     continue

            writer = PyPDF2.PdfWriter()
            for page_number in range(start-1, end):
                writer.add_page(reader.pages[page_number])

            output_path = f"{output_folder}/pages_{start}_{end}.pdf"
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)

# Example usage:
pdf_path = r"D:\object_detection_collection\maths\TEY251 - IX - G9_MATHS_ANNUAL EXAMINATION _B - 4.pdf"  # Path to your PDF file
output_folder = r"D:\object_detection_collection\maths"  # Folder where you want to save the split PDF pages
page_ranges = [(87, 282)]  # Specify the ranges of pages you want to split

split_pdf(pdf_path, output_folder, page_ranges)
