import cv2.cv as cv
import time

cv.NamedWindow("camera", 1)

capture = cv.CaptureFromCAM(0)

i = 0
while True:
    img = cv.QueryFrame(capture)
    cv.ShowImage("camera", img)
    cv.SaveImage('pic{:>}.jpg'.format(i), img)
    if cv.WaitKey(62) == 27:
        break
    i += 1