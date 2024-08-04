import pypdfium2 as pdfium
import cv2

def extractPDFtoImages(path,pdf_image_destination):
    pdf = pdfium.PdfDocument(path)
    for i in range(len(pdf)):
        page = pdf[i]
        image = page.render(scale=6).to_pil()
        # page = cv2.imread(image)
        # img_path = r"D:\roll-num\New folder\G2_MAT_TVSM_for review_page-0001.jpg"
        # sample_img = cv2.imread(img_path)
        # h,w = sample_img.shape[:2]
        # image = cv2.resize(page, (int(w), int(h)))
        # cv2.imwrite(f"{pdf_image_destination}/output_{i+0}.jpg",image)
        image.save(f"{pdf_image_destination}/output_{i+0}.jpg")
    print(f"-----{path} pdf image extration completed to {pdf_image_destination}----")   
      