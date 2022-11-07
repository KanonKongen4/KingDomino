def divide_image(input_image):
    h, w, channels = input_image.shape
    tileSize = w // 5
    listOfTiles = []
    for y in range(1, 6):
        for x in range(5):
            tile = input_image[tileSize * (y-1) :tileSize * y, tileSize * x:tileSize * (x + 1)]
            listOfTiles.append(tile)


    return listOfTiles


