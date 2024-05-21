     
import os
path = "./text_data"                
files = os.listdir(path)
for file in files:
    file_path = os.path.join(path,file)
    file_name = os.path.splitext(os.path.basename(file_path))[0] 
    json_path = os.path.join(path,f"{file_name}.json")
    if not os.path.exists(json_path):
        os.remove(file_path)
        print(f"{file_name} removed")                

                
                
                
                
import os
import shutil


path = r"/home/ubuntu/mount/math_obj_data/text_data"
json_files = [i for i in os.listdir(path) if i.endswith(".json")]
batch_size = 500
folders=r"/home/ubuntu/mount/math_obj_data/batch"
batch_json_files = [json_files[i:i+batch_size] for i in range(0, len(json_files), batch_size)]
for i, batch in enumerate(batch_json_files):
    for json_file in batch:
        save_dir = os.path.join(folders, f"Batch_{str(i)}")
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
        shutil.copy(os.path.join(path, json_file), os.path.join(save_dir, json_file))
        png_path = json_file.replace('.json','.png')
        shutil.copy(os.path.join(path, png_path), os.path.join(save_dir, png_path))
            
            
            
            
            

