import cv2 as cv
import numpy

template = cv.imread('crownblack.jpg', 0)
imgsearch = cv.imread('20.jpg')
img_gray = cv.cvtColor(imgsearch, cv.COLOR_BGRA2GRAY)
w, h = template.shape[::-1]

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
threshold = 0.90
loc = numpy.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(imgsearch, pt, (pt[0] + w, pt[1] + h), (0, 0, 225), 2)

cv.imwrite('res.png', imgsearch)
cv.imshow('plsvirk', imgsearch)

cv.waitKey(0)
