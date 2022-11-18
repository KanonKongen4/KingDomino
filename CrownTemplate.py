import cv2 as cv
import numpy

crown_left = cv.imread('crownLeft.jpg', 0)
imgsearch_left_crowns = cv.imread('20.jpg')
img_gray_left = cv.cvtColor(imgsearch_left_crowns, cv.COLOR_BGRA2GRAY)
w, h = crown_left.shape[::-1]

crown_right = cv.imread('crownRight.jpg', 0)
imgsearch_right_crowns = cv.imread('20.jpg')
img_gray_right = cv.cvtColor(imgsearch_right_crowns, cv.COLOR_BGRA2GRAY)
w, h = crown_right.shape[::-1]

crown_down = cv.imread('CrownDown.jpg', 0)
imgsearch_down_crowns = cv.imread('20.jpg')
img_gray_down = cv.cvtColor(imgsearch_down_crowns, cv.COLOR_BGRA2GRAY)
w, h = crown_down.shape[::-1]

res_left = cv.matchTemplate(img_gray_left, crown_left, cv.TM_CCOEFF_NORMED)
threshold = 0.5
loc = numpy.where(res_left >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(imgsearch_left_crowns, pt, (pt[0] + w, pt[1] + h), (0, 0, 225), 2)

res_right = cv.matchTemplate(img_gray_right, crown_right, cv.TM_CCOEFF_NORMED)
threshold = 0.90
loc = numpy.where(res_right >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(imgsearch_right_crowns, pt, (pt[0] + w, pt[1] + h), (0, 0, 225), 2)

res_down = cv.matchTemplate(img_gray_down, crown_down, cv.TM_CCOEFF_NORMED)
threshold = 0.7
loc = numpy.where(res_down >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(imgsearch_down_crowns, pt, (pt[0] + w, pt[1] + h), (0, 0, 225), 2)

cv.imwrite('res_left.png', imgsearch_left_crowns)
cv.imshow('leftCrowns', imgsearch_left_crowns)

cv.imwrite('res_right.png', imgsearch_right_crowns)
cv.imshow('rightCrowns', imgsearch_right_crowns)

cv.imwrite('res_down.png', imgsearch_down_crowns)
cv.imshow('downCrowns', imgsearch_down_crowns)

cv.waitKey(0)
