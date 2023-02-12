import cv2
import numpy as np

# Read the image
img = cv2.imread('image.jpg')

# Convert to grayscale 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
  
# Apply Gaussian Blur 
blur = cv2.GaussianBlur(gray,(5,5),0) 
  
# Apply Canny Edge Detection 
canny = cv2.Canny(blur,50,150) 

 # Dilate the edges to make them thicker 
dilated = cv2.dilate(canny, np.ones((3,3), np.uint8))