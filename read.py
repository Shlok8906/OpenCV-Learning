import cv2 as cv
#reading imagingess
# img=cv.imread("photo/bmw_m340i_xdrive_50_jahre_m_edition_2022_4k_5k_hd_cars-3840x2160.jpg")
# cv.imshow('car',img)
#reading videos
import cv2 as cv

#reading videos 
capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('c'):  # 'c' dabao to band hoga
        break
capture.release()
cv.destroyAllWindows()

