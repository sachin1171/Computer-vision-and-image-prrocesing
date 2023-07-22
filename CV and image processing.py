# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 17:15:53 2021

@author: usach
"""
#importing required libraries
import cv2

# Creating body classifier using haarcascade_fullbody.xml
body_classifier = cv2.CascadeClassifier('C:/Users/usach/Desktop/AI assignments/Module 8/haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('C:/Users/usach/Desktop/AI assignments/Module 8/180301_06_B_CityRoam_01.mp4')

# Loop once video is successfully loaded
while cap.isOpened():
    
    # Read first frame
    ret, frame = cap.read()
    
    #converting video into Gray, where as RGB is time consuming
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Pass frame to our body classifier
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extract bounding boxes for any bodies identified
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Pedestrians', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
