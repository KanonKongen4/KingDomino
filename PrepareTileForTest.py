import cv2
import numpy as np

def return_list_of_blurred_images(listOfImages):
    list= []
    for img in listOfImages:
        list.append(blur_image(img))
    return list


def blur_image(img):
    return cv2.medianBlur(img,7)

def get_dominant_colour(img):
    data = np.reshape(img, (-1, 3))
    print(data.shape)
    data = np.float32(data)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data, 1, None, criteria, 10, flags)

    color = centers[0].astype(np.int32)
    print('Dominant color is: bgr({})'.format(color))

    return color


def get_list_of_dominant_colours(tile_list):
    colors = []
    for tile in tile_list:
        colors.append(get_dominant_colour(tile))

    return colors