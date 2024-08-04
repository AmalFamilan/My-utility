import cv2
import matplotlib.pyplot as plt
import numpy as np
import uuid
import os
from tqdm import tqdm
import time


def padding(file):
    original_image = cv2.imread(file)
    OUTPUT_WIDTH, OUTPUT_HEIGHT = 640, 640
    height, width, _ = original_image.shape
    scale_factor = min(OUTPUT_WIDTH / width, OUTPUT_HEIGHT / height)
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    offset_x = (OUTPUT_WIDTH - new_width) // 2
    offset_y = (OUTPUT_HEIGHT - new_height) // 2
    blank_image = np.full((OUTPUT_HEIGHT, OUTPUT_WIDTH, 3), 255, dtype=np.uint8)
    resized_original_image = cv2.resize(original_image, (new_width, new_height))
    resized_original_image = cv2.cvtColor(resized_original_image, cv2.COLOR_BGR2RGB)
    blank_image[offset_y:offset_y+new_height, offset_x:offset_x+new_width] = resized_original_image
    return blank_image
 
   
for root, _, files in (os.walk(r"D:\VGG16\data")):
    for filename in tqdm(files,desc="Processing : "):
        if filename.endswith(".jpg"):
            image_path = os.path.join(root, filename)
            result = padding(image_path)
            if root == r"D:\VGG16\data\train\0":
                plt.imsave(f"D:/VGG16/pad data/train/0/image-{uuid.uuid4()}.jpg", result) 
            elif root == r"D:\VGG16\data\train\90" :
                plt.imsave(f"D:/VGG16/pad data/train/90/image-{uuid.uuid4()}.jpg", result) 
            elif root == r"D:\VGG16\data\train\180":
                plt.imsave(f"D:/VGG16/pad data/train/180/image-{uuid.uuid4()}.jpg", result)
            elif root == r"D:\VGG16\data\train\270":
                plt.imsave(f"D:/VGG16/pad data/train/270/image-{uuid.uuid4()}.jpg", result) 
            elif root == r"D:\VGG16\data\train\NOT":
                plt.imsave(f"D:/VGG16/pad data/train/NOT/image-{uuid.uuid4()}.jpg", result)
            elif root == r"D:\VGG16\data\test\0":
                plt.imsave(f"D:/VGG16/pad data/test/0/image-{uuid.uuid4()}.jpg", result)
            elif root == r"D:\VGG16\data\test\90":
                plt.imsave(f"D:/VGG16/pad data/test/90/image-{uuid.uuid4()}.jpg", result)
            elif root == r"D:\VGG16\data\test\180":
                plt.imsave(f"D:/VGG16/pad data/test/180/image-{uuid.uuid4()}.jpg", result)
            elif root == r"D:\VGG16\data\test\270":
                plt.imsave(f"D:/VGG16/pad data/test/270/image-{uuid.uuid4()}.jpg", result)
            elif root == r"D:\VGG16\data\test\NOT":
                plt.imsave(f"D:/VGG16/pad data/test/NOT/image-{uuid.uuid4()}.jpg", result)
     
# path = r"D:\Extra data\0\output_2fe7f76c-a9cf-4b59-9eb1-b5d113756c4b.jpg"
# s = time.time()
# result = padding(path)
# e = time.time()
# plt.imsave(f"D:/Extra data/image.jpg", result)   
# print(e - s)