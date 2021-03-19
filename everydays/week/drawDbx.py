# coding: utf-8
"""
    @author: zhangjk
    @file: drawDbx.py
    @date: 2020-02-07
    说明：xxxx
"""
import cv2
import numpy as np

img = range(1,255)

img = np.zeros((365,500,3),np.uint8)

cv2.line(img,(20,60),(200,100),(255,0,0),3)
cv2.rectangle(img,(60,20),(100,200),(255,0,255),6)
cv2.rectangle(img,(260,80),(300,120),(222,0,255),6)
cv2.circle(img,(360,300),60,(255,0,255),10)
cv2.ellipse(img,(256,256),(150,100),0,0,360,(255,0,255),2)

cv2.imshow("Image",img)

cv2.waitKey(0)
