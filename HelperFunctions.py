<<<<<<< Updated upstream
=======
import cv2 as cv
import numpy as np


>>>>>>> Stashed changes
def get_tile_size_of_img(input_image):
    height = input_image.shape[0]
    # length = input_image.shape[1]
    size_of_tile = height / 5
<<<<<<< Updated upstream
    return size_of_tile
=======
    return size_of_tile


def show_images_in_list(listToShow):
    for i in range(len(listToShow)):
        cv.imshow(f"tile[{i}]", listToShow[i])


def create_image_with_colour(color, num):
    testImg = np.zeros((300, 300, 3), np.uint8)
    # Fill image with red color(set each pixel to red)
    testImg[:] = color
    cv.imshow("test" + str(num), testImg)
    return testImg


def create_empty_string_array():
    strs = [["" for x in range(5)] for y in range(5)]
    return strs



>>>>>>> Stashed changes
