import os 
import shutil

    
tenent_path = "D:/text_obj_dect/Wrksheet"
destination = "D:/text_obj_dect/train_data"
for root, dirs, files in os.walk(tenent_path):
        for file in files:
            if file.endswith(".png"):
                move_path = os.path.join(destination,file)
                png_path = os.path.join(root,file)
                shutil.copy(png_path,move_path)
                
            if file.endswith(".json"):
                move_path = os.path.join(destination,file)
                json_path = os.path.join(root,file)
                shutil.copy(json_path,move_path)
        print(f"done for {root}")        
            