import cv2 as cv 
img=cv.imread("photo/1st.jpg")
cv.imshow("original",img)
#making B&W
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",gray)

# #Blur
blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
# # cv.imshow("blur",blur)

# #Edge Cascades (Intrestingg)
canny=cv.Canny(blur,125,175)
cv.imshow("canny",canny)

#di;ating the image
dilated=cv.dilate(canny,(11,11),iterations=3)
cv.imshow("Dilated",dilated)

#eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

cv.waitKey(0)
