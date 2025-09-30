import cv2 as cv 
import numpy as np


img=cv.imread("photo/bmw.jpg")
# cv.imshow("Original",img)

blank=np.zeros(img.shape,dtype='uint8')
# cv.imshow("Blank",blank)


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# cv.imshow("Gray",gray)

blur=cv.blur(img,(3,3),cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)
canny=cv.Canny(blur,125,125)
cv.imshow("Canny",canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} countoutrs found')



cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow("Countours Drawn",blank)




cv.waitKey(0)