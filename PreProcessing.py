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

img = cv.imread("20.jpg")  # Read the test image
blurred = PrepareTileForTest.blur_image(img)  # blur the input image
cv.imshow("start", img)  # show the input image
cv.imshow("blurred", blurred)  # show the blurred input image

listOfTiles = DivideimageIntoParts.divide_image(blurred)  # Divide the image into 25 tiles

colours = DominantColourFinder.get_list_of_dominant_colours(listOfTiles)  # Getting the dominant colour of the tiles

# print("colours", colours)
merged = MergeDominantColourImages.MergeImages(colours)  # Merge the dominant colours into an image
cv.imshow("tes", merged)
print("hello")
territories2DMatrix = TerritoryName.get_territory_name_from_colour_list(colours)
print(territories2DMatrix)

territoriesSegmented = grassfire.GetNewMatrixWithID(territories2DMatrix)


print("territoriesSegmented", territoriesSegmented)

allCrownPositions = CrownTemplate.GetAllCrowns(img)
print("allCrownPositions", allCrownPositions)

crownPositions = NonMaximaSuppression.non_max_suppression(allCrownPositions)
print("positions", crownPositions)

xs, ys = CrownTemplate.GetXsYsFromBoxes(crownPositions)

print("xs, ys", xs, ys)
crownMatrixFinished = CrownTemplate.Make_Crown_Matrix(ys,xs)
print("crownMatrixFinished", crownMatrixFinished)

points = PointsCounter.GetPointsFromTerritoriesMultipliedByCrowns(territoriesSegmented,crownMatrixFinished)

print("points", points)
cv.waitKey(0)
