import shutil 
import os

folder_path = "D:/sample"
destination = "D:/sample move"
folder_list = os.listdir("D:/sample2")

for folder in folder_list:
    shutil.move(f"{folder_path}/{folder}",f"{destination}/{folder}")