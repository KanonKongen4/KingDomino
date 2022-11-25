
def get_dominant_colour_new(img):

    rSum=0
    gSum=0
    bSum=0

    for x in range(len(img[0])):
        for y in range(len(img[1])):
            if x < 25 or x > 75 or y<25 or y>75:

                rSum += img[x,y][0]
                gSum += img[x, y][1]
                bSum += img[x, y][2]


    rAverage = rSum/7500
    gAverage = gSum / 7500
    bAverage = bSum / 7500


    colValues = [rAverage,gAverage,bAverage]
    color = tuple(colValues)


    return color

def get_list_of_dominant_colours(tile_list):
    colors = []
    for tile in tile_list:
        colors.append(get_dominant_colour_new(tile))

    return colors