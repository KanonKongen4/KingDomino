
# def isWithinRange(area1, area2, range):
#     if area1>area2-range and area1< area2 + range:
#         return True
#     else:
#         return False

def NMS(boxes, overlapThresh): # TODO: started writing own NMS but its kinda hard to do:-O!!!
    #
    # areas = []
    # topLeftPoints = []
    #
    # for box in boxes:
    #
    #     x1 = box[0]
    #     y1 = box[1]
    #     x2 = box[2]
    #     y2 = box[3]
    #
    #     width = x2-x1
    #     height = y2-y1
    #
    #     area = width*height
    #     # print("x1/y1: ", x1,"/",y1,  "    area: ", area)
    #     areas.append(area)
    #
    #     listPoint1 =[x1,y1]
    #     # tup = tuple(x1,y1)
    #     topLeftPoints.append(listPoint1)
    #
    # # for i, area in enumerate(areas):
    # #     if isWithinRange(area)
    # print(areas)
    # print(topLeftPoints)

    return boxes