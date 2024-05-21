import os 
import shutil

    
tenent_path = r"D:/science/science-2"
file_list = os.listdir(tenent_path)
split_range = len(file_list)//2
for i in range(split_range+1):
    file_path = f'{tenent_path}/{file_list[i]}'
    os.makedirs(f'D:/science/science-3',exist_ok=True)
    shutil.move(file_path,'D:/science/science-3')
    
    



    