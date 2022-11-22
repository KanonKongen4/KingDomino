from pathlib import Path

import cv2 as cv
import numpy


#Importing the different crown template images.
input_dir_up = Path.cwd() / "crownImages/up"  # Path.cwd finds current working directory(where this file is run) and a folder name
input_dir_right = Path.cwd() / "crownImages/right"
input_dir_down = Path.cwd() / "crownImages/down"
input_dir_left = Path.cwd() / "crownImages/left"

#Add the images to lists
ex_images_up = list(input_dir_up.glob('*.jpg'))  # Finds all images in folder  .png extension and adds them to an array
ex_images_right = list(input_dir_right.glob('*.jpg'))
ex_images_down = list(input_dir_up.glob('*.jpg'))
ex_images_left = list(input_dir_left.glob('*.jpg'))

for crown_image in ex_images_left:
    print(crown_image)

#Image To Search for crowns in
imgsearch = cv.imread('20.jpg')
#To grayscale
img_gray = cv.cvtColor(imgsearch, cv.COLOR_BGRA2GRAY)
#width and height of image

DEFAULT_THRESHOLD = 0.5
detections = []
def Find_Crowns_in_Image(gray_image, listOfExampleCrowns):
    for crown_image in listOfExampleCrowns: # Loop over every image in the list
        w, h = crown_image.shape[::-1] # finding the width and height of the image ??
        res_left = cv.matchTemplate(gray_image, crown_image, cv.TM_CCOEFF_NORMED)
        loc = numpy.where(res_left >= DEFAULT_THRESHOLD)
        for pt in zip(*loc[::-1]):
            cv.rectangle(gray_image, pt, (pt[0] + w, pt[1] + h), (0, 0, 225), 2)
            detections.append(pt)
    return  gray_image

image = Find_Crowns_in_Image(img_gray,ex_images_up)
cv.imshow("image", image)
print(detections)

cv.waitKey(0)
