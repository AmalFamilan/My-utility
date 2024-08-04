import input 
import os
import cv2
from utility import pdf_img,embbedText,extractFromExcel
from tqdm import tqdm

path = input.pdf['path']
excel = input.pdf['excel_path']
org_name = input.pdf['org_name']
org_roll = input.pdf['org_roll']
org_sec = input.pdf['org_sec']
out_path = input.pdf['out_pdf_path']
pdf_image_destination = input.pdf['pdf_image_destination']
pdf_img.extractPDFtoImages(path,pdf_image_destination)

   
student_records = extractFromExcel.parsing_student_data_from_excel(excel) 
for student in tqdm(student_records,desc="Pages processing : ",ascii="░▒█"):
    # print("processing student number : ",student['admission_number'])
    pg_count=0
    for img in os.listdir(pdf_image_destination):
        pg_count += 1   
        image = os.path.join(pdf_image_destination,img)
        
        image = cv2.imread(image)
        if pg_count%2 != 0:
            if pg_count == 1:
                image = embbedText.embbed_roll_number(image,org_roll,student['admission_number'])
                image = embbedText.embbed_text(image,org_name,org_sec,student['student_name'],student['section'])
                cv2.imwrite(f"{out_path}/{student['admission_number']}-{pg_count}.jpg",image)
            else:
                image = embbedText.embbed_roll_number(image,org_roll,student['admission_number'])
                cv2.imwrite(f"{out_path}/{student['admission_number']}-{pg_count}.jpg",image)
        else:
            cv2.imwrite(f"{out_path}/{student['admission_number']}-{pg_count}.jpg",image)
        
    
    
    
        

