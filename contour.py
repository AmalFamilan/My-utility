import cv2
import numpy as np
import pypdfium2 as pdfium

# Load a document
pdf = pdfium.PdfDocument("D:/rotation_dataset/contour/merged-1.pdf")

# Loop over pages and render
for i in range(len(pdf)):
    page = pdf[i]
    image = page.render(scale=4).to_pil()
    image.save(f"Extracted-image/output_{i:03d}.jpg")
    
    image = cv2.imread(f"Extracted-image/output_{i:03d}.jpg")

# Preprocess the Image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    edges =cv2.Canny(gray, threshold1=200, threshold2=150)  # Adjust threshold values as needed

    # Find Contours
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw Contours
    contour_image = np.zeros_like(image)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

    # Saving Contours
    
    cv2.imwrite(f"D:/rotation_dataset/contour/sample/contuor-image-{i:03d}.png", contour_image)
    # cv2.imwrite("D:/rotation_dataset/contour/image.png", image)