import cv2 as cv
import colorsys

def get_territory_name(img, id):
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    color_hsv = hsv[0][0]

    range = 7

    # TODO: get the average colours for each tile by getting the average of a number of differently lighted images.

    col_water = (100, 0, 180)
    col_forest = (39, 0, 66)
    col_meadow = (39, 0, 160)
    col_desert = (23, 0, 116)
    col_coal = (23, 0, 70)
    col_corn = (26, 0, 198)

    string = "empty"

    if (check_conditions(color_hsv, col_water, 6, 70)):
        string = "water"
    elif (check_conditions(color_hsv, col_forest, 6, 70)):
        string = "forest"
    elif (check_conditions(color_hsv, col_meadow, 6, 70)):
        string = "meadow"
    elif (check_conditions(color_hsv, col_desert, 6, 25)):
                    string = "desert"
    elif (check_conditions(color_hsv, col_coal, 6, 25)):
        string = "coal"
    elif (check_conditions(color_hsv, col_corn, 6, 40)):
        string = "corn"

    print(str(string) + "  " + str(id) +"  hsv: " + str(hsv[0][0])  )

    return string

def get_territory_name_from_colour(color, id):
    hsv = colorsys.rgb_to_hsv(color)

    range = 7

    # TODO: get the average colours for each tile by getting the average of a number of differently lighted images.

    col_water = (100, 0, 180)
    col_forest = (39, 0, 66)
    col_meadow = (39, 0, 160)
    col_desert = (23, 0, 116)
    col_coal = (23, 0, 70)
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

    print(str(string) + "  " + str(id) +"  hsv: " + str(hsv[0][0])  )

    return string

def check_conditions(input_color, color_to_find, range_hue, range_value):
    hue = input_color[0]

    value = input_color[2]

    if hue > color_to_find[0] - range_hue and hue < color_to_find[0] + range_hue:
        if value > color_to_find[2] - range_value and value < color_to_find[2] + range_value:
            return True