def NMS(boxes, overlapThresh):

    areas = []
    for box in boxes:

        x1 = boxes[0]
        y1 = boxes[1]
        x2 = boxes[3]
        y2 = boxes[4]

        width = x2-x1
        height = y2-y1
        print(box)

        areas.append()

    return boxes