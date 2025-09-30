import cv2 as cv 
import numpy as np


img=cv.imread("photo/bmw.jpg")
cv.imshow("Original",img)

#laplocion
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow("Laplacian",lap)

#sabel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('Sobel X',sobelx)
cv.imshow("Sobel y",sobely)

merged=cv.bitwise_or(sobelx,sobely)
cv.imshow("Merged sobel",merged)

canny=cv.Canny(gray,150,175)
cv.imshow("Canny",canny)


cv.waitKey(0)