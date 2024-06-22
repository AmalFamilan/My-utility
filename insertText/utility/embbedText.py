import cv2 
import os


def embbed_roll_number(image,org_roll,roll_num):
    text_format = generate_text_format(cv2.FONT_HERSHEY_SIMPLEX,4,9,(0,0,0))
    image = insert_element_in_image(image,org_roll,roll_num,text_format)
    return image

def embbed_text(image,org_name,org_sec,name,sec):
        
    text_format = generate_text_format(cv2.FONT_HERSHEY_TRIPLEX,2.5,4,(0,0,0))
    image = insert_element_in_image(image,org_name,name,text_format)
    image = insert_element_in_image(image,org_sec,sec,text_format)
    
    return image

def insert_element_in_image(image, origin_pixel_coordinate, value, text_format):
    image = cv2.putText(image, str(value), origin_pixel_coordinate, text_format['font_name'],text_format['fontScale_name'],text_format['colour'], text_format['thickness_name'], cv2.LINE_AA)
    return image
    
def generate_text_format(fontName, font_scale, font_thickness, colour):
     text_format = {
        'font_name' : fontName,
        'fontScale_name' : font_scale,
        'colour' : colour,
        'thickness_name' : font_thickness
    }
     return text_format


    