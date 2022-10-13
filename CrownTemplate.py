import cv2 as cv
import numpy

imgtemp = cv.imread("crown.jpg")
imgtemp2 = imgtemp.copy()
template = cv.imread("20.jpg")