import cv2 as cv
import numpy

img = cv.imread("20.jpg")
cv.imshow("Start", img)


def get_tile_size_of_img(input_image):
    height = input_image.shape[0]
    # length = input_image.shape[1]
    size_of_tile = height / 5
    return size_of_tile


def divide_image_into_equal_parts(input_image):
    h, w, channels = input_image.shape
    fifth = w // 5
    firstPart = input_image[0:100, 0:100 ]
    cv.imshow(f"Left part{0}", firstPart)
    firstPart = input_image[100:200, 0:100]
    cv.imshow(f"Left part{2}", firstPart)


divide_image_into_equal_parts(img)

key = cv.waitKey(0)
