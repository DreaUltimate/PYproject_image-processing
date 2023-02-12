#importing the necessary libraries
import numpy as np
import cv2

cap = cv2.VideoCapture(0) 
ret, frame = cap.read()  
gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
blur = cv2.GaussianBlur(gray_image, (5, 5), 0) 
canny = cv2.Canny(blur, 10, 70) 
contours, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
cv2.drawContours(frame, contours, -1, (0, 255, 0), 2) 

cv2.imshow('Contours', frame)
