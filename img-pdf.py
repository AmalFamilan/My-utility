from PIL import Image  
import os 

# def imgTopdf(path,pdf_path):
#     images = [] 
#     for file in os.listdir(path): 
#         # file = "output_9abbacf5-62d6-4bed-b6ea-988ea72cf8a4_000.jpg"
#         images.append(Image.open(os.path.join(path, file)))
#     images[0].save(
#         pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
#     )

def convert_images_to_pdf(input_dir, output_pdf):
    images = [file for file in os.listdir(input_dir) if file.endswith(('png', 'jpg', 'jpeg', 'gif', 'bmp'))]
    if not images:
        print("No images found in the directory.")
        return
    
    images.sort()  # Sort images by filename

    first_image = Image.open(os.path.join(input_dir, images[0]))
    pdf_path = os.path.join(input_dir, output_pdf)
    first_image.save(pdf_path, save_all=True, append_images=[Image.open(os.path.join(input_dir, img)) for img in images[1:]])

    print(f"PDF created successfully at {pdf_path}")

# Example usage:
input_directory = r"D:\extracted_img\2"
output_pdf_name = r"D:\extracted_img\TTS-II-H-MAT-PDF2.pdf"
convert_images_to_pdf(input_directory, output_pdf_name)
