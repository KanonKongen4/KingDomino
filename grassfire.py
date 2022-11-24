from collections import deque
import numpy as np
import cv2 as cv

img = cv.imread("shapes.png", cv.IMREAD_GRAYSCALE)


'''img = np.array([[0, 0, 0, 255, 255, 255],
               [0, 0, 0, 0, 255, 0],
               [0, 0, 0, 0, 255, 0],
               [0, 0, 255, 255, 0, 0],
               [0, 0, 255, 255, 0, 0],
               [0, 0, 255, 255, 0, 0]], dtype=np.uint8)'''


def ignite_pixel(stringMatrix, coordinate, id, tileTypeString):
    y, x = coordinate
    burn_queue = deque()

    if stringMatrix[y, x] == tileTypeString:
        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if stringMatrix[y, x] == tileTypeString:
            stringMatrix[y, x] = id

            if x + 1 < stringMatrix.shape[1] and stringMatrix[y, x + 1] == tileTypeString:
                burn_queue.append((y, x + 1))
            if y + 1 < stringMatrix.shape[0] and stringMatrix[y + 1, x] == tileTypeString:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and stringMatrix[y, x - 1] == tileTypeString:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and stringMatrix[y - 1, x] == tileTypeString:
                burn_queue.append((y - 1, x))

        #print(stringMatrix)
        #print(burn_queue)
        #input()

        if len(burn_queue) == 0:
            return id + 1

    return id


def grassfire(image):
    next_id = 1
    for y, row in enumerate(image):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(image, (y, x), next_id)




grassfire(img)

#print(img)
cv.imshow("Output", img)
cv.waitKey()