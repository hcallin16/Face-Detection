#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Detects and blurs faces in video files.
@author Henry Callin
@Date 12/8/21
"""
# Imports
import tkinter as tk
import tkinter.filedialog as fd
import cv2
import os
import sys
# Create gui to browse for file.
root = tk.Tk()
root.withdraw()
currdir = os.getcwd()
file = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select image file')
# Import face detection file from CV2.
face_cascade = cv2.CascadeClassifier('Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# Capture chosen video file.
video = cv2.VideoCapture(file)
# Step through each frame of the video, detecting face and blurring it.
while True:
    # Read the current frame, and convert to grayscale for face detection.
    _, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detects any faces in the frame.
    faces = face_cascade.detectMultiScale(gray, 1.3, 3)
    # Steps through each detected face, isolates each face region,
    # applies a blur to the region, and splices it back onto original frame.
    for (x, y, w, h) in faces:
        roi = img[y:y + h, x:x + w]
        kernel = (15,15)
        blurred = cv2.blur(roi, kernel)
        img[y:y + h, x:x + w] = blurred
    # Display the altered frame.
    cv2.imshow('Output', img)
    # Exits code if esc is pressed twice.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# End of program.
video.release()
cv2.waitKey()
# Exit.
exit()