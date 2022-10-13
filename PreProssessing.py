import cv2 as cv
import numpy

img = cv.imread("20.jpg")
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


#def GetSmallerArrayFromArray(tileSize, Startingpoint)
    #arrayOf2DArrays = numpy.array()

get_tile_size_of_img(img)

divide_image_into_equal_parts(img)

key = cv.waitKey(0)