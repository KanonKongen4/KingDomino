import cv2
import numpy as np

# def get_dominant_colour(img):
#     data = np.reshape(img, (-1, 3))
#     data = np.float32(data)
#
#     criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#     flags = cv2.KMEANS_RANDOM_CENTERS
#     compactness, labels, centers = cv2.kmeans(data, 1, None, criteria, 10, flags)
#
#     color = centers[0].astype(np.int32)
#     #print('Dominant color is: bgr({})'.format(color))
#
#     return color

def get_dominant_colour_new(img):

    rSum=0
    gSum=0
    bSum=0

    for x in range(len(img[0])):
        for y in range(len(img[1])):
            if x < 25 or x > 75 or y<25 or y>75:

                rSum += img[x,y][0]
                gSum += img[x, y][1]
                bSum += img[x, y][2]


    rAverage = rSum/7500
    gAverage = gSum / 7500
    bAverage = bSum / 7500

    # for x in range(len(img[0])):
    #     for y in range(len(img[1])):
    #
    #         rSum += img[x,y][0]
    #         gSum += img[x, y][1]
    #         bSum += img[x, y][2]
    #
    #
    # rAverage = rSum/10000
    # gAverage = gSum / 10000
    # bAverage = bSum / 10000


    colValues = [rAverage,gAverage,bAverage]
    color = tuple(colValues)


    return color

def get_list_of_dominant_colours(tile_list):
    colors = []
    for tile in tile_list:
        colors.append(get_dominant_colour_new(tile))

    return colors