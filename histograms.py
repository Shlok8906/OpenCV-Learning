import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("photo/icecream.jpg")
cv.imshow("Original",img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)

# gray_hist=cv.calcHist([gray],[0],None,[256],[0,256])

# plt.figure()
# plt.title("Grayscale histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#color histogram
plt.figure()
plt.title("colour histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)