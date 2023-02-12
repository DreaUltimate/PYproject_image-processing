#importing the necessary libraries
import numpy as np
import cv2

#reading the image from the webcam
cap = cv2.VideoCapture(0) 
ret, frame = cap.read() 
  
#converting the image to grayscale 
gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  
#applying gaussian blur on the image 
blur = cv2.GaussianBlur(gray_image, (5, 5), 0) 
  
#applying canny edge detection on the blurred image 
canny = cv2.Canny(blur, 10, 70) 

 #finding contours in the edged image and keeping only the largest ones 
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 

 #drawing contours on the original image 
cv2.drawContours(frame, contours, -1, (0, 255, 0), 2) 

 #displaying the resulting frame with contours drawn on it  
cv2.imshow('Contours', frame)
