import cv2 as cv
# img=cv.imread('photo/bmw_m340i_xdrive_50_jahre_m_edition_2022_4k_5k_hd_cars-3840x2160.jpg')
# cv.imshow('car',img)
#rescalling
def rescaleframe(frame,scale=0.25):
    #works for images, Videos and live videos(Camera)
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
img=cv.imread('photo/bmw_m340i_xdrive_50_jahre_m_edition_2022_4k_5k_hd_cars-3840x2160.jpg')
resized_image=rescaleframe(img)
cv.imshow('car_resized',resized_image)
# capture = cv.VideoCapture(0)
# while True:
#     isTrue, frame = capture.read()
#     frame_resized=rescaleframe(frame)
#     if not isTrue:
#         break
#     cv.imshow('Video', frame)
#     cv.imshow('Video Resized',frame_resized)
#     if cv.waitKey(20) & 0xFF == ord('c'):  # 'c' dabao to band hoga
#         break
# capture.release()
cv.waitKey(0)
cv.destroyAllWindows()