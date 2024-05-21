import os 

dir_path = r"D:\detectron2 data\Full data"
path = os.listdir(dir_path)

for file in path:
    if file.endswith('Copy.jpg'):
        file_path = os.path.join(dir_path,file)
        # print(file_path)
        os.remove(file_path)