from collections import deque


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
            #print(stringMatrix[y, x])
            if x + 1 < stringMatrix.shape[1] and stringMatrix[y, x + 1] == tileTypeString:
                burn_queue.append((y, x + 1))
            if y + 1 < stringMatrix.shape[0] and stringMatrix[y + 1, x] == tileTypeString:
                burn_queue.append((y + 1, x))
            if x - 1 >= 0 and stringMatrix[y, x - 1] == tileTypeString:
                burn_queue.append((y, x - 1))
            if y - 1 >= 0 and stringMatrix[y - 1, x] == tileTypeString:
                burn_queue.append((y - 1, x))



        if len(burn_queue) == 0:
            return id + 1

    return id


def grassfire(tileStringMatrix, territoryName):
    next_id = 1
    for y, row in enumerate(tileStringMatrix):
        for x, pixel in enumerate(row):
            next_id = ignite_pixel(tileStringMatrix, (y, x), next_id, territoryName)
    return tileStringMatrix


def GetNewMatrixWithID(oldMatrix):
    newMatrix = oldMatrix

    newMatrix = grassfire(oldMatrix, "corn")
    newMatrix = grassfire(oldMatrix, "coal")
    newMatrix = grassfire(oldMatrix, "forest")

    newMatrix = grassfire(oldMatrix, "meadow")
    newMatrix = grassfire(oldMatrix, "desert")
    newMatrix = grassfire(oldMatrix, "water")

    return newMatrix
