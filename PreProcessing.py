import random
import cv2 as cv

import CrownTemplate
import DominantColourFinder
import DivideimageIntoParts
import MergeDominantColourImages
import NonMaximaSuppression
import PointsCounter
import PrepareTileForTest
import TerritoryName
import grassfire
import GetAverageColourOfTiles

img = cv.imread("TestImages\example (8).jpg")  # Read the test image
blurred = PrepareTileForTest.blur_image(img)  # blur the input image

listOfTiles = DivideimageIntoParts.divide_image(blurred)  # Divide the image into 25 tiles

colours = DominantColourFinder.get_list_of_dominant_colours(listOfTiles)  # Getting the dominant colour of the tiles

for col in colours:
    GetAverageColourOfTiles.create_image_with_colour(col, random.Random(10000))

# print("colours", colours)
merged = MergeDominantColourImages.MergeImages(colours)  # Merge the dominant colours into an image
cv.imshow("tes", merged)

territories2DMatrix = TerritoryName.get_territory_name_from_colour_list(colours)

territoriesSegmented = grassfire.GetNewMatrixWithID(territories2DMatrix)


print("territoriesSegmented \n", territoriesSegmented)

allCrownPositions = CrownTemplate.GetAllCrowns(img)

crownPositions = NonMaximaSuppression.non_max_suppression(allCrownPositions)

xs, ys = CrownTemplate.GetXsYsFromBoxes(crownPositions)

crownMatrixFinished = CrownTemplate.Make_Crown_Matrix(ys,xs)
print("crownMatrixFinished \n", crownMatrixFinished)

points = PointsCounter.GetPointsFromTerritoriesMultipliedByCrowns(territoriesSegmented,crownMatrixFinished)

print("points", points)

cv.imshow("start", img)  # show the input image

cv.waitKey(0)
