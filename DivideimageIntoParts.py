import cv2 as cv

def divide_image(input_image):
    listOfTiles =[]
    h, w, channels = input_image.shape
    tileSize = w // 5
    for y in range(1, 6):
        for x in range(5):
            tile = input_image[tileSize * (y-1) :tileSize * y, tileSize * x:tileSize * (x + 1)]
            # cv.imshow(f"rowNum: {y}, part{x}", tile)
            listOfTiles.append(tile)
    return listOfTiles