import cv2 as cv
import numpy as np
img=cv.imread("photo/bmw.jpg")
cv.imshow("Original",img)
def translate(img,x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transmat,dimensions)
# -x -> left
# +x -> right
# -y ->up
# # +y -> down
# translated=translate(img,-60,-100)
# cv.imshow('Translated',translated)

# #Rotation
# def rotate(img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]
#     if rotPoint is None:
#         rotPoint=(width//2,height//2)
#     rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
#     dimensions=(width,height)
#     return cv.warpAffine(img,rotPoint,dimensions)
# rotated=rotate(img,90)
# cv.imshow("Rotaed",rotated)

#Fliping
fliped=cv.flip(img,1) #0 for upside down and 1 for left to right
cv.imshow("Flip",fliped)
cv.waitKey(0)
