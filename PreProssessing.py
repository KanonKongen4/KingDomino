import cv2 as cv
import numpy
import HelperFunctions
import DivideimageIntoParts

img = cv.imread("20.jpg")
cv.imshow("Start", img)

DivideimageIntoParts.divide_image(img)

key = cv.waitKey(0)
