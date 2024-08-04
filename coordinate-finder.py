# from PIL import Image

# def get_image_coordinates(image_path):
#     image = Image.open(image_path)
#     width, height = image.size
#     coordinates = (0, 0, width, height)  # Assuming the whole image as the region of interest
#     return coordinates

# image_path = r"D:\roll-num\G2_MAT_TVSM_for review_page-0001.jpg"  # Replace "example.jpg" with the path to your image
# coordinates = get_image_coordinates(image_path)
# print("Image coordinates:", coordinates)

# import the required library
import cv2

# define a function to display the coordinates of

# of the points clicked on the image
def click_event(event, x, y, flags, params):
   if event == cv2.EVENT_LBUTTONDOWN:
      print(f'({x},{y})')
      
      # put coordinates as text on the image
      cv2.putText(img, f'({x},{y})',(x,y),
      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
      
      # draw point on the image
      cv2.circle(img, (x,y), 3, (0,255,255), -1)
 
# read the input image
img = cv2.imread(r"D:\roll-num\G2_MAT_TVSM_for review_page-0001.jpg")

# create a window
cv2.namedWindow('Point Coordinates')

# bind the callback function to window
cv2.setMouseCallback('Point Coordinates', click_event)

# display the image
while True:
   cv2.imshow('Point Coordinates',img)
   k = cv2.waitKey(1) & 0xFF
   if k == 27:
      break
cv2.destroyAllWindows()