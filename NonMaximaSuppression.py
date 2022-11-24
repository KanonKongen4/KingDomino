import numpy


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

    outputMatrix = numpy.zeros((5, 5), dtype=int)
    print(outputMatrix)

    topLeftCoordinates = []

    for box in boxes:
        values = [box[0], box[1]]
        topLeftCoordinates.append(values)

    print(topLeftCoordinates)

    newList = topLeftCoordinates


    # check if insde range and remove if it is
    for coord in topLeftCoordinates:
        if coord_is_within_range(coord, topLeftCoordinates):
            newList.remove(coord)

    print(newList)
    return boxes
