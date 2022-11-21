import cv2 as cv
import colorsys

import numpy


def get_territory_name_from_colour(color, id):

    (h, s, v) = colorsys.rgb_to_hsv(color[2], color[1], color[0])
    values = [h*180,s,v]
    hsv = tuple(values)

    range = 7

    # TODO: get the average colours for each tile by getting the average of a number of differently lighted images.

    col_water = (100, 0, 180)
    col_forest = (39, 0, 60)
    col_meadow = (39, 0, 150)
    col_desert = (23, 0, 105)
    col_coal = (23, 0, 50)
    col_corn = (26, 0, 198)

    string = "empty"

    if (check_conditions(hsv, col_water, 6, 70)):
        string = "water"
    elif (check_conditions(hsv, col_forest, 6, 70)):
        string = "forest"
    elif (check_conditions(hsv, col_meadow, 6, 70)):
        string = "meadow"
    elif (check_conditions(hsv, col_desert, 6, 25)):
        string = "desert"
    elif (check_conditions(hsv, col_coal, 6, 25)):
        string = "coal"
    elif (check_conditions(hsv, col_corn, 6, 40)):
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




def check_conditions(input_color, color_to_find, range_hue, range_value):
    hue = input_color[0]

    value = input_color[2]

    if hue > color_to_find[0] - range_hue and hue < color_to_find[0] + range_hue:
        if value > color_to_find[2] - range_value and value < color_to_find[2] + range_value:
            return True