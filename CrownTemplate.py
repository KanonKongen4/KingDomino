from pathlib import Path
import math
import cv2 as cv
import numpy
import NonMaximaSuppression

#Importing the different crown template images.
input_dir_up = Path.cwd() / "crownImages/up"  # Path.cwd finds current working directory(where this file is run) and a folder name
input_dir_right = Path.cwd() / "crownImages/right"
input_dir_down = Path.cwd() / "crownImages/down"
input_dir_left = Path.cwd() / "crownImages/left"

#Add the images to lists
ex_images_up = list(input_dir_up.glob('*.jpg'))  # Finds all images in folder  .png extension and adds them to an array
ex_images_right = list(input_dir_right.glob('*.jpg'))
ex_images_down = list(input_dir_down.glob('*.jpg'))
ex_images_left = list(input_dir_left.glob('*.jpg'))


#Image To Search for crowns in
imgsearch = cv.imread('20.jpg')
#To grayscale
img_gray = cv.cvtColor(imgsearch, cv.COLOR_BGRA2GRAY)
#width and height of image

DEFAULT_THRESHOLD = 0.8
boxes = list()
def Find_Crowns_in_Image(gray_image, listOfExampleCrowns):
    for crown_image in listOfExampleCrowns: # Loop over every image in the list
        img = cv.imread(str(crown_image))[:, :, :] # Read the image
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert crown example image to grayscale
        w, h  = gray.shape # get width and height of example image
        result = cv.matchTemplate(gray_image, gray, cv.TM_CCOEFF_NORMED) #??
        loc = numpy.where(result >= DEFAULT_THRESHOLD) # numpy.where loops over the image and checks if result > threshold
        for point in zip(*loc[::-1]): #??
            cv.rectangle(imgsearch, point, (point[0] + w, point[1] + h), (0, 0, 225), 2) # Draw rectangle at top-left point of match

            x1 = point[0]
            y1 = point[1]
            x2 = point[0] + w
            y2 = point[1] + h

            boxes.append((x1, y1, x2, y2))
    return  imgsearch

image = Find_Crowns_in_Image(img_gray,ex_images_up)
image = Find_Crowns_in_Image(img_gray,ex_images_right)
image = Find_Crowns_in_Image(img_gray,ex_images_down)
image = Find_Crowns_in_Image(img_gray,ex_images_left)

cv.imshow("image", image)

NonMaximaSuppression.NMS(boxes,0.4)
cv.waitKey(0)