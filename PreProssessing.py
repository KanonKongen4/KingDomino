import cv2 as cv
import DominantColourFinder
import HelperFunctions
import DivideimageIntoParts
import PrepareTileForTest
import TerritoryName

img = cv.imread("20.jpg")#Read the test image
blurred = PrepareTileForTest.blur_image(img) # blur the input image
cv.imshow("blurred", blurred)# show the input image

listOfTiles = DivideimageIntoParts.divide_image(blurred) #Divide the image into 25 tiles
#HelperFunctions.show_images_in_list(listOfTiles) # Show the divided tiles!


colours = DominantColourFinder.get_list_of_dominant_colours(listOfTiles) # colours of the tiles

one_colour_images = []
i = 0
for colour in colours:
    one_colour_images.append(HelperFunctions.create_image_with_colour(colour, i))
    i += 1

stringArray = HelperFunctions.create_empty_string_array()

list_2D_territory_code_strings = [[]]

i = 0
for image in one_colour_images:
    territoryString = TerritoryName.get_territory_name(image,i)
    i += 1



key = cv.waitKey(0)
