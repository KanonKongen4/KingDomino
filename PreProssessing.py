import cv2 as cv
import numpy as np

img = cv.imread("20.jpg")
img_grayscale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
template = cv.imread('crown_upscaled_180_Rotation.png', 0)
#template_grayscale = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
w, h = template.shape[::-1]

res = cv.matchTemplate(img_grayscale, template, cv.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)


cv.imshow("Start", img)

def get_tile_size_of_img(input_image):
    height = input_image.shape[0]
    length = input_image.shape[1]
    print(f"height is {height}, length is {length}")

    size_of_tile = height/5
    print(f"tileSize is {size_of_tile}")
    return size_of_tile

def divide_image_into_equal_parts(input_image):
    h, w, channels = input_image.shape
    fifth = w//5

    firstPart = input_image[:fifth, :fifth]
    cv.imshow('Left part', firstPart)
    #print(f"input_image[pointx,pointy is {input_image[pointx,pointy]}")


#def GetSmallerArrayFromArray(tileSize, Startingpoint)2
    #arrayOf2DArrays = numpy.array()

get_tile_size_of_img(img)

divide_image_into_equal_parts(img)

key = cv.waitKey(0)