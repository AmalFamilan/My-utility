import cv2
import os
import uuid
from tqdm import tqdm

def rotate_image_90(image_path):
    
    for img in tqdm(image_path):
        
        tem = "D:/Extra data/90-Dup/"+img
   
        image = cv2.imread(tem)
        
        # Rotate the image by 270 degrees clockwise
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        output_image_path = f"D:/Extra data/90/output_{uuid.uuid4()}.jpg"
        cv2.imwrite(output_image_path, rotated_image)
        

def rotate_image_180(image_path):
    
    for img in tqdm(image_path):
        
        tem = "D:/Extra data/180-Dup/"+img
   
        image = cv2.imread(tem)
        
        # Rotate the image by 270 degrees clockwise
        rotated_image = cv2.rotate(image, cv2.ROTATE_180)
        output_image_path = f"D:/Extra data/180/output_{uuid.uuid4()}.jpg"
        cv2.imwrite(output_image_path, rotated_image)
        
def rotate_image_270(image_path):
    
    for img in tqdm(image_path):
        
        tem = "D:/extra data/270-Dup/"+img
   
        image = cv2.imread(tem)
        
        # Rotate the image by 270 degrees clockwise
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        output_image_path = f"D:/Extra data/270/output_{uuid.uuid4()}.jpg"
        cv2.imwrite(output_image_path, rotated_image)
        
        
path = os.listdir("D:/extra data/90-Dup")
rotate_image_90(path)

path = os.listdir("D:/extra data/180-Dup")
rotate_image_180(path)

path = os.listdir("D:/extra data/270-Dup")
rotate_image_270(path)