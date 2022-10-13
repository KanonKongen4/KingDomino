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
    for row in range(1, 6):
        divide_row(input_image, row)

def divide_row(input_image, rowNum):
    h, w, channels = input_image.shape
    fifth = w // 5
    multiplierStart = 0
    multiplier = 1

    for x in range(5):
        print(f"x is{x}")
        firstPart = input_image[100 * (rowNum-1) :100 * rowNum, fifth * multiplierStart:fifth * multiplier]
        cv.imshow(f"rowNum: {rowNum}, part{multiplier}", firstPart)
        multiplier += 1
        multiplierStart += 1


divide_image_into_equal_parts(img)

key = cv.waitKey(0)
