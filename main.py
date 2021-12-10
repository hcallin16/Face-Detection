#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Henry Callin
@Date 12/8/21
"""

import tkinter as tk
import tkinter.filedialog as fd
import cv2
import os
import sys

root = tk.Tk()
root.withdraw()

currdir = os.getcwd()
file = fd.askopenfilename(parent=root, initialdir=currdir, title='Please select image file')

face_cascade = cv2.CascadeClassifier('Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(file)

while True:
    _, img = video.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 3)

    for (x, y, w, h) in faces:
        roi = img[y:y + h, x:x + w]
        kernel = (10,10)
        blurred = cv2.blur(roi, kernel)
        img[y:y + h, x:x + w] = blurred

    cv2.imshow('Output', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break


video.release()
cv2.waitKey()

# Exit
exit()