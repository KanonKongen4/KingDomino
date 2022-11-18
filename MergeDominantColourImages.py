import DominantColourFinder
import cv2 as cv
from PIL import Image

img = Image.open("20.jpg")

def MergeImages(image, tile_list):
    new_image = Image.new('RGB', (image.size[0], image.size[1]), (250,250,250))
    for tile in tile_list:
        new_image.paste(tile_list[tile], tile_list)

    return new_image