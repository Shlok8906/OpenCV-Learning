import cv2 as cv 
import numpy as np

img=cv.imread("photo/bmw.jpg")
# cv.imshow("Original",img)

blank=np.zeros((400,400),dtype='uint8') 
#rectangle

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow("Rectangle",rectangle)
cv.imshow("Circle",circle)

#AND operator
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow("AND",bitwise_and)

#or operator
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow("or",bitwise_or)

#XOR operator
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow("XOR",bitwise_xor)

#NOT operator
bitwise_not=cv.bitwise_not(circle)
cv.imshow("NOT CIRCLE",bitwise_not)



cv.waitKey(0)