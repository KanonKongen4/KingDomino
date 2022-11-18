import cv2 as cv
import DominantColourFinder
import HelperFunctions
import DivideimageIntoParts
import MergeDominantColourImages
import PrepareTileForTest
import TerritoryName

img = cv.imread("20.jpg")#Read the test image
blurred = PrepareTileForTest.blur_image(img) # blur the input image
cv.imshow("blurred", blurred)# show the input image

listOfTiles = DivideimageIntoParts.divide_image(blurred) #Divide the image into 25 tiles
#HelperFunctions.show_images_in_list(listOfTiles) # Show the divided tiles!


colours = DominantColourFinder.get_list_of_dominant_colours(listOfTiles) # colours of the tiles




merged = MergeDominantColourImages.MergeImages(colours)
cv.imshow("tes", merged)

stringArray = HelperFunctions.create_empty_string_array()

list_2D_territory_code_strings = [[]]

territories2DMatrix = TerritoryName.get_territory_name_from_colour_list(colours)
print(territories2DMatrix)



key = cv.waitKey(0)
