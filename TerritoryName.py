import cv2 as cv
import colorsys

import numpy

import GetAverageColourOfTiles


def get_territory_name_from_colour(color, id):

    (h, s, v) = colorsys.rgb_to_hsv(color[2], color[1], color[0])
    values = [h*180,s*255,v]
    hsv = tuple(values)

    #range = 7

    col_water = GetAverageColourOfTiles.get_average_colour(GetAverageColourOfTiles.images_water)
    col_forest = GetAverageColourOfTiles.get_average_colour(GetAverageColourOfTiles.images_forest)
    col_meadow = GetAverageColourOfTiles.get_average_colour(GetAverageColourOfTiles.images_meadow)
    col_desert = GetAverageColourOfTiles.get_average_colour(GetAverageColourOfTiles.images_desert)
    col_coal = GetAverageColourOfTiles.get_average_colour(GetAverageColourOfTiles.images_coal)
    col_corn = GetAverageColourOfTiles.get_average_colour(GetAverageColourOfTiles.images_corn)

    GetAverageColourOfTiles.create_image_with_colour_HSV2BGR(col_water,4)
    GetAverageColourOfTiles.create_image_with_colour(color, 5)
    print("water check:", "colwater: ", col_water, "    -hsv: " , hsv)
    string = "empty"

    if (check_conditions(hsv, col_water, 10, 80, 70)):
        string = "water"
    elif (check_conditions(hsv, col_forest, 6, 50, 70)):
        string = "forest"
    elif (check_conditions(hsv, col_meadow, 6, 50, 70)):
        string = "meadow"
    elif (check_conditions(hsv, col_desert, 6, 50, 40)):
        string = "desert"
    elif (check_conditions(hsv, col_coal, 30, 50, 80)):
        string = "coal"
    elif (check_conditions(hsv, col_corn, 6, 50, 40)):
        string = "corn"

   # print(str(string) + "  " + str(id) +"  hsv: " + str(hsv)  )

    return string

def get_territory_name_from_colour_list(listOfColours):
    i = 0
    strings = []
    for col in listOfColours:
        strings.append(get_territory_name_from_colour(col, i))
        i += 1

    new2DMatrix = numpy.reshape(strings,(5,5))

    return new2DMatrix


def check_conditions(input_color, color_to_find, range_hue, range_saturation, range_value):
    hue = input_color[0]
    sat = input_color[1]
    value = input_color[2]

    if hue > color_to_find[0] - range_hue and hue < color_to_find[0] + range_hue:
        if sat > color_to_find[1] - range_saturation and sat < color_to_find[1] + range_saturation:
            if value > color_to_find[2] - range_value and value < color_to_find[2] + range_value:
                return True