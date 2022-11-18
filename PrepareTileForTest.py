import cv2
import numpy as np

def return_list_of_blurred_images(listOfImages):
    list= []
    for img in listOfImages:
        list.append(blur_image(img))
    return list

def blur_image(img):
    return cv2.medianBlur(img,7)