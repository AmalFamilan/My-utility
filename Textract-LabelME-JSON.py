from PIL import Image
import json
import base64
import os
import argparse

def convert_textract_to_labelme(image_path, textract_json_path, output_folder):
    img = Image.open(image_path)

    width = img.width
    height = img.height

    with open(textract_json_path, 'r') as f:
        tJson = json.load(f)

    with open(image_path, 'rb') as image_file:
        data = image_file.read()

    image_data = base64.b64encode(data).decode('utf-8')

    labelme_data = {
        "version": "5.4.1",
        "flags": {},
        "shapes": [],
        "imagePath": f"{os.path.basename(image_path)}",  
        "imageData": image_data,
        "imageHeight": height,
        "imageWidth": width
    }

    for i in tJson['annotations']:
        if i["BlockType"] == "WORD":
            for j in i['Geometry']['Polygon']:
                j['X'] = j['X'] * width
                j['Y'] = j['Y'] * height

    for i in tJson['annotations']:
        if i["BlockType"] == "WORD":
            label = "text"
            points = []
            for j in i['Geometry']['Polygon']:
                points.append([j['X'], j['Y']])

            shape_data = {
                "label": label,
                "points": points,
                "group_id": None,
                "description": "",
                "shape_type": "polygon",
                "flags": {},
                "mask": None
            }
            labelme_data["shapes"].append(shape_data)

    
    image_filename = os.path.splitext(os.path.basename(image_path))[0]
    os.makedirs(output_folder, exist_ok=True)
    output_json_path = os.path.join(output_folder, f"{image_filename}.json")
    labelme_json = json.dumps(labelme_data, indent=2)
    with open(output_json_path, "w") as json_file:
        json_file.write(labelme_json)

    print(f"LabelMe JSON for {image_filename} created")

    


parser = argparse.ArgumentParser(description='Run the excel generation')
parser.add_argument('-t','--textract',help = "path of textract json folder ", required=True)
parser.add_argument('-l','--labelme',help="path to save labelme json folder",required=True)
args = vars(parser.parse_args())


input_folder = args.get("textract")
output_folder = args.get("labelme")

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg','.png')):
        image_path = os.path.join(input_folder, filename)
        textract_json_path = os.path.join(input_folder, f"{os.path.splitext(filename)[0]}.json")

        convert_textract_to_labelme(image_path, textract_json_path, output_folder)
