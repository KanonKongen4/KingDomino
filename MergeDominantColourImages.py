import numpy as np

from PIL import Image

img = Image.open("20.jpg")


def MergeImages(color):

    new_matrix2D = np.zeros((5,5,3), dtype=np.uint8)
    colors2D = np.reshape(color,(5,5,3))

    for y in range(0, len(colors2D[0])):
        for x in range(0, len(colors2D[1])):
            new_matrix2D[y, x] = colors2D[y,x]

    return new_matrix2D
