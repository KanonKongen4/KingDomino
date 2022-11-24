from collections import deque
import numpy as np
import cv2 as cv
import PreProcessing

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
            stringMatrix[y, x] = stringMatrix[y, x] + id
            print(stringMatrix[y, x])
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


def grassfire(tileStringMatrix):
    next_id = 1
    for y, row in enumerate(tileStringMatrix):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, tileTypeString="water")
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, tileTypeString="forest")
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, tileTypeString="meadow")
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, tileTypeString="desert")
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, tileTypeString="coal")
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, tileTypeString="corn")




newTileStringMatrix = grassfire(tileStringMatrix=PreProcessing.territories2DMatrix)

#print(img)
#print(newTileStringMatrix)
#cv.imshow("Output", img)
cv.waitKey()