import pypdfium2 as pdfium
import PIL.Image
import os
from tqdm import tqdm
import uuid


def name_converter(pdf):
    array = pdf.split('/')
    root_ext = os.path.splitext(array[5])
    return root_ext[0]

# for multiple pdf in  single dir
def for_multiple_pdf(Pdf_dir,out_dir):
    pdf_array=os.listdir(Pdf_dir)
    for pdf in tqdm(pdf_array,desc="Processing : "):
        if pdf.endswith('.pdf'):
            print(pdf)
            pdf_path = f"{Pdf_dir}/{pdf}"
            pdf = pdfium.PdfDocument(pdf_path) 
            # pdf_name = name_converter(pdf_path)
            pdf_name = uuid.uuid4()
            for i in range(len(pdf)):
                page = pdf[i]
                image = page.render(scale=4).to_pil()
                image.save(f"{out_dir}/{pdf_name}-page-{i+1}.png")
                print(f'--{i+1}--')
    
# for single pdf 
def for_single_pdf(Pdf_path,out_dir):
    pdf = pdfium.PdfDocument(Pdf_path)
    # pdf_name = name_converter(Pdf_path)
    pdf_name = uuid.uuid4()
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=6).to_pil()
        image.save(f"{out_dir}/{pdf_name}-page-{i+1}.png")
        print(f"--{i+1}--")
    
        

Pdf_path = r"d:\object_detection_collection\scoi"
out_put_dir = r"D:/object_detection_collection/inference_data"
for_multiple_pdf(Pdf_path,out_put_dir)
