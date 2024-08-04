import cv2
import os
import shutil

def find_and_save_similar_images(template_path, images_dir, output_dir):
    # Read the template
    
    
    # Iterate through all images in the directory
    for filename in os.listdir(images_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png')):  # Adjust file extensions as needed
            image_path = os.path.join(images_dir, filename)
            
            # Read the image
            img = cv2.imread(image_path, 0)
            # Apply template matching
            for tem in template_path: 
                template = cv2.imread(tem, 0)
                result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            
            # Threshold for considering a match
                threshold = 0.5
                if max_val >= threshold:
                    # Get the coordinates of the matched region
                    
                    top_left = max_loc
                    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
                    
                    # Extract the matched region
                    matched_region = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
                    
                    # Save the matched region to the output directory
                    output_path = os.path.join(output_dir, filename)
                    cv2.imwrite(output_path, matched_region)
                    shutil.copy(image_path, f"D:/rotation_dataset/contour/output/{filename}")
                    print(f"Matched region saved to: {output_path}")

# Example usage
template_path = ["D:/rotation_dataset/contour/state.jpg","D:/rotation_dataset/contour/outline.jpg"]
images_dir = "D:/rotation_dataset/contour/pdf-image"
output_directory = "D:/rotation_dataset/contour/nochang"

find_and_save_similar_images(template_path, images_dir, output_directory)




