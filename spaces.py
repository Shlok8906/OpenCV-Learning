import cv2 as cv
import matplotlib.pyplot as plt
img=cv.imread("photo/bmw.jpg")
cv.imshow("Original",img)

# plt.imshow(img)
# plt.show()

# #bgr to hsv
# hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)

#bgr to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RGB",rgb)

plt.imshow(rgb)
plt.show()



cv.waitKey(0)
