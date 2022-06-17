import numpy as np 
import cv2

gray_img = np.empty((240, 320), dtype=np.uint8)
gray_img2 = np.ones((240, 320), dtype=np.uint8) * 255
color_img = np.zeros((240, 320, 3), dtype=np.uint8)
color_img2 = np.ones((240, 320, 3), dtype=np.uint8) * 255

cv2.imshow('gray_img', gray_img) 
cv2.imshow('gray_img2', gray_img2) 
cv2.imshow('color_img', color_img) 
cv2.imshow('color_img2', color_img2) 

cv2.waitKey() 
cv2.destroyAllWindows()

