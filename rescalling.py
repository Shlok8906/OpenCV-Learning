import cv2 as cv

def rescaling(height, width):
    # only works for live video (Camera)
    capture.set(3, width)   # property id 3 -> width
    capture.set(4, height)  # property id 4 -> height

capture = cv.VideoCapture(0)

rescaling(1920,1200)  # resolution set karna (height, width)

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        print("Failed to capture frame")
        break

    cv.imshow("Livevideo", frame)

    # 'c' dabao to band hoga
    if cv.waitKey(20) & 0xFF == ord('c'):
        break

capture.release()
cv.destroyAllWindows()
