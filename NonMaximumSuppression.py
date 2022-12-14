import numpy as np

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
    # bottom-right y-coordinate)
    area = (x2 - x1 + 1) * (y2 - y1 + 1)
    idxs = y2

    # if probabilities for match templates are provided, sort on them instead
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

        # compute the width and height of the bounding box and makes sure no bounding boxes are deleted if they dont overlap,
        # since if for an example xx2 - xx1 + 1 results in a negative number, then the next line where bounding boxes overlap
        # is calculated will equal 0, since 0 will be picked by the np.maximum() method, and 0 times or divided by anything
        # will always equal zero, making sure that the calculated overlap will not be greater than the set overlapTresh (overlap threshold)
        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        # compute the ratio of overlap
        overlap = (w * h) / area[idxs[:last]]

        # delete all indexes from the index list that have overlap greater
        # than the provided overlap threshold
        idxs = np.delete(idxs, np.concatenate(([last], np.where(overlap > overlapThresh)[0])))

    # return only the bounding boxes that were picked
    return boxes[pick].astype("int")
