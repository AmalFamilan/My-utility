import cv2
import os
import uuid

def rotate_image(image_path):
    
    for img in image_path:
        
        tem = "D:/extra data/270/rot/"+img
   
        image = cv2.imread(tem)
        
        # Rotate the image by 270 degrees clockwise
        rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
        output_image_path = f"D:/extra data/270/output_{uuid.uuid4()}.jpg"
        cv2.imwrite(output_image_path, rotated_image)
    


# Example usage:
input_image_path = os.listdir("D:/extra data/270/rot")
# output_image_path = f"D:/rotation_automation/train/90/output_{uuid.uuid4()}.jpg"  # Ensure this includes a valid file extension
rotation_angle = 90  # Change this value to rotate by a different angle

rotated_image = rotate_image(input_image_path)

