import numpy as np


# def isWithinRange(area1, area2, range):
#     if area1>area2-range and area1< area2 + range:
#         return True
#     else:
#         return False

def coord_is_within_range(coord1, coordList):
    range = 6

    i = 0
    for each_coord in coordList:

        x1 = coord1[0]
        y1 = coord1[1]
        x2 = each_coord[0]
        y2 = each_coord[1]

        # print("x1:",x1 ,"  y1:",y1, "  x2:",x2, "  y2:",y2)
        i+= 1
        print(i)
        if x1 > x2 - range and x1 < x2 + range and y1 > y2 - range and y1 < y2 + range:
            print("REMOVED")
            return True
        print("KEPT")
        return False

        # if x1 == x2 and y1>=


def NMS(boxes, overlapThresh):  # TODO: started writing own NMS but its kinda hard to do:-O!!!

<<<<<<< Updated upstream
    # outputMatrix = numpy.zeros((5, 5), dtype=int)
    # print(outputMatrix)
=======
    outputMatrix = np.zeros((5, 5), dtype=int)
    print(outputMatrix)
>>>>>>> Stashed changes

    boundingBoxesCoords = []

    for box in boxes:
        values = [box[0], box[1], box[2], box[3]]
        boundingBoxesCoords.append(values)

    print(boundingBoxesCoords)

    newList = boundingBoxesCoords


    # check if insde range and remove if it is
    for coord in boundingBoxesCoords:
        if coord_is_within_range(coord, boundingBoxesCoords):
            newList.remove(coord)

    print(newList)
<<<<<<< Updated upstream
    return topLeftCoordinates
=======
    return boxes

def non_max_suppression(boxes, probs=None, overlapThresh=0.3):
    # if there are no boxes, return an empty list
    boxesNp = np.array(boxes)

    if len(boxesNp) == 0:
        return []

    # if the bounding boxesNp are integers, convert them to floats -- this
    # is important since we'll be doing a bunch of divisions
    if boxesNp.dtype.kind == "i":
        boxes = boxesNp.astype("float")

    # initialize the list of picked indexes
    pick = []

    # grab the coordinates of the bounding boxes
    x1 = boxesNp[:, 0]
    y1 = boxesNp[:, 1]
    x2 = boxesNp[:, 2]
    y2 = boxesNp[:, 3]

    # compute the area of the bounding boxes and grab the indexes to sort
    # (in the case that no probabilities are provided, simply sort on the
    # bottom-left y-coordinate)
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = y2

    # if probabilities are provided, sort on them instead
    if probs is not None:
        idxs = probs

    # sort the indexes
    idxs = np.argsort(idxs)

    # keep looping while some indexes still remain in the indexes list
    while len(idxs) > 0:
        # grab the last index in the indexes list and add the index value
        # to the list of picked indexes
        last = len(idxs) - 1
        i = idxs[last]
        pick.append(i)

        # find the largest (x, y) coordinates for the start of the bounding
        # box and the smallest (x, y) coordinates for the end of the bounding
        # box
        xx1 = np.maximum(x1[i], x1[idxs[:last]])
        yy1 = np.maximum(y1[i], y1[idxs[:last]])
        xx2 = np.minimum(x2[i], x2[idxs[:last]])
        yy2 = np.minimum(y2[i], y2[idxs[:last]])

        # compute the width and height of the bounding box
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        # compute the ratio of overlap
        overlap = (w * h) / area[idxs[:last]]

        # delete all indexes from the index list that have overlap greater
        # than the provided overlap threshold
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    # return only the bounding boxes that were picked
    return boxes[pick].astype("int")
>>>>>>> Stashed changes
