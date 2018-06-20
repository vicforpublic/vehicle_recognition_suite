# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:43:25 2018

@author: f202897
"""

import numpy as np
import cv2

cap = cv2.VideoCapture('dia.mp4')

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorGMG()

while(1):
     ret, frame = cap.read()
 
     fgmask = fgbg.apply(frame)
     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
 
     cv2.imshow('frame',fgmask)
     k = cv2.waitKey(30) & 0xff
     if k == 27:
         break
 
cap.release()
cv2.destroyAllWindows()