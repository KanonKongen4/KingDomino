import random
from pathlib import Path
import numpy as np
import cv2 as cv

input_dir_coal = Path.cwd() / "averageColourExampleImages/coal"  # Path.cwd finds current working directory(where this file is run) and a folder name
input_dir_corn = Path.cwd() / "averageColourExampleImages/corn"
input_dir_desert = Path.cwd() / "averageColourExampleImages/desert"
input_dir_forest = Path.cwd() / "averageColourExampleImages/forest"
input_dir_meadow = Path.cwd() / "averageColourExampleImages/meadow"
input_dir_water = Path.cwd() / "averageColourExampleImages/water"

# is added

images_coal = list(input_dir_coal.glob('*.jpg'))  # Finds all images with .jpg extension and adds them to an array
images_corn = list(input_dir_corn.glob('*.jpg'))
images_desert = list(input_dir_desert.glob('*.jpg'))
images_forest = list(input_dir_forest.glob('*.jpg'))
images_meadow = list(input_dir_meadow.glob('*.jpg'))
images_water = list(input_dir_water.glob('*.jpg'))


def get_average_colour(list_of_images):
    list_average_colours = []
    for img in list_of_images:
        img = cv.imread(str(img))[:, :, :]
        img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        average = img_hsv.mean(axis=0).mean(axis=0)
        #print(average , "  avg" ,str (list_of_images))

        list_average_colours.append(average)

    return combine_colours(list_average_colours)


def combine_colours(list_of_colours):
    sum_h = 0
    sum_s = 0
    sum_v = 0
    for color in list_of_colours:
        sum_h += color[0]
        sum_s += color[1]
        sum_v += color[2]

    average_h = sum_h / len(list_of_colours)
    average_s = sum_s / len(list_of_colours)
    average_v = sum_v / len(list_of_colours)

    color = (average_h, average_s, average_v)
    create_image_with_colour(color, random.Random(10000))
    return color


def create_image_with_colour(color, num):
    testImg = np.zeros((300, 300, 3), np.uint8)
    # Fill image with red color(set each pixel to red)
    testImg[:] = color
    cv.imshow("test" + str(num), testImg)
    return testImg

def create_image_with_colour_HSV2BGR(color, num):
    testImg = np.zeros((300, 300, 3), np.uint8)
    # Fill image with red color(set each pixel to red)
    testImg[:] = color
    img_bgr = cv.cvtColor(testImg, cv.COLOR_HSV2BGR)

    cv.imshow("test" + str(num), img_bgr)
    return img_bgr
