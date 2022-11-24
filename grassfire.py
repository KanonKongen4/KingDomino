from collections import deque

import numpy
import numpy as np
import cv2 as cv
import PreProcessing


def ignite_pixel(stringMatrix, coordinate, id, tileTypeString):
    y, x = coordinate
    burn_queue = deque()

    if stringMatrix[y, x] == tileTypeString:
        burn_queue.append((y, x))

    while len(burn_queue) > 0:
        current_coordinate = burn_queue.pop()
        y, x = current_coordinate
        if stringMatrix[y, x] == tileTypeString:
            stringMatrix[y, x] = stringMatrix[y, x] + str(id)
            print(stringMatrix[y, x])
            if x + 1 < stringMatrix.shape[1] and stringMatrix[y, x + 1] == tileTypeString:
                burn_queue.append((y, x + 1))
            if y + 1 < stringMatrix.shape[0] and stringMatrix[y + 1, x] == tileTypeString:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and stringMatrix[y, x - 1] == tileTypeString:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and stringMatrix[y - 1, x] == tileTypeString:
                burn_queue.append((y - 1, x))
        else: print("fuuuck!")

        # print(stringMatrix)
        # print(burn_queue)
        # input()

        if len(burn_queue) == 0:
            return id + 1

    return id


def grassfire(tileStringMatrix, territoryName):
    next_id = 1
    for y, row in enumerate(tileStringMatrix):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, territoryName)
    return tileStringMatrix

newMatrix = PreProcessing.territories2DMatrix
# print("newMatrix", newMatrix)

newMatrix = grassfire(PreProcessing.territories2DMatrix, "corn")
newMatrix = grassfire(PreProcessing.territories2DMatrix, "coal")
newMatrix = grassfire(PreProcessing.territories2DMatrix, "tree")

newMatrix = grassfire(PreProcessing.territories2DMatrix, "mead")
newMatrix = grassfire(PreProcessing.territories2DMatrix, "desert")
newMatrix = grassfire(PreProcessing.territories2DMatrix, "water")

print("newTafdf", newMatrix)
# print(img)
# print(newTileStringMatrix)
# cv.imshow("Output", img)
cv.waitKey()
