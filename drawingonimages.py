import cv2 as cv 
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow("Blank",blank)
# #paint image with certain color
# blank[:]=0,165,255
#          #B #G #R
# cv.imshow("Orange",blank)

# 2.Draw Rectangle
cv.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=cv.FILLED)
cv.imshow("Rectangle",blank)

#3. Circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),70,(0,165,255),thickness=-1)
cv.imshow("Circle",blank)
cv.waitKey(0)
