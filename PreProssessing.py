import cv2 as cv
import HelperFunctions
import DivideimageIntoParts
import PrepareTileForTest

img = cv.imread("20.jpg")

listOfTiles = DivideimageIntoParts.divide_image(img)

listOfTiles = PrepareTileForTest.return_list_of_blurred_images(listOfTiles)

HelperFunctions.show_images_in_list(listOfTiles)

img2 = PrepareTileForTest.blur_image(img)
cv.imshow("name", img2)

colours = PrepareTileForTest.get_list_of_dominant_colours(listOfTiles)

# TODO This is not working!!
i = 0
for colour in colours:
    HelperFunctions.create_image_with_colour(colour, i)
    i += 1

# list_2D_territory_codes = [[]]

key = cv.waitKey(0)
