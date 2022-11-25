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
ex_images_down = list(input_dir_down.glob('*.jpg'))
ex_images_left = list(input_dir_left.glob('*.jpg'))


DEFAULT_THRESHOLD = 0.8
boxes = list()
def Find_Crowns_in_Image(inputImage, listOfExampleCrowns):
    gray_image = cv.cvtColor(inputImage, cv.COLOR_BGR2GRAY) #
    for crown_image in listOfExampleCrowns: # Loop over every image in the list
        img = cv.imread(str(crown_image))[:, :, :] # Read the image
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # convert crown example image to grayscale
        w, h  = gray.shape # get width and height of example image
        result = cv.matchTemplate(gray_image, gray, cv.TM_CCOEFF_NORMED) #??
        loc = numpy.where(result >= DEFAULT_THRESHOLD) # numpy.where loops over the image and checks if result > threshold
        for point in zip(*loc[::-1]): #??
            #cv.rectangle(imgsearch, point, (point[0] + w, point[1] + h), (0, 0, 225), 2) # Draw rectangle at top-left point of match

            x1 = point[0]
            y1 = point[1]
            x2 = point[0] + w
            y2 = point[1] + h
            boxes.append((x1, y1, x2, y2))

    return boxes

def Make_Crown_Matrix(template_positionsX,template_positionY):
    crown_amount_matrix = numpy.zeros((5, 5))
    for i in range(len(template_positionsX)):
        #Hvor mange gange går X positionen op i 100, hvis 0 gange, så er column = 0, 1 gang = column 1 osv
        column = template_positionsX[i] / 100
        column = int(column) #Converter til int for at skærer decimalet væk
        row = template_positionY[i] / 100
        row = int(row)
        crown_amount_matrix[row,column] += 1
    return crown_amount_matrix

def get_approx_box_center(boxes):
    newBoxes = numpy.zeros(boxes.shape)

    for i in range(len(boxes)):
        newBoxes[i,0] = boxes[i,2] - 15 # 30 er cirka template width, så ved at minus med halvdelen får vi centret
        newBoxes[i,1] = boxes[i,3] - 15 # 30 er cirka også template height, så her minuser vi også med halvdelen

    #Slicer så vi kun har 2 columns - 1 for x og 1 for y
    newBoxes = newBoxes[:,:2]
    #print(newBoxes)


    #newBoxes[i, 0] = np.maximum(boxes[i, 0], boxes[i, 2])
    #newBoxes[i, 2] = np.minimum(boxes[i, 0], boxes[i, 2])
    #newBoxes[i, 0] = newBoxes[i, 0] - newBoxes[i, 2]
    return newBoxes

def draw_box_coordinates(img,boxes):
    newImage = numpy.zeros(img.shape)
    #print(boxes.shape)

    for x in boxes:
        #print(f"x:{x}")
        newImage[int(x[1]),int(x[0])] = 1


    #cv2.imshow("newImage",newImage)
    #cv2.waitKey(0)
    return newImage

def GetXsYsFromBoxes(boxes):

    xs = []
    ys = []
    for x in boxes:
        #print(f"x:{x}")
        xs.append(int(x[1]))
        ys.append(int(x[0]))

    return xs,ys

def GetAllCrowns(inputImage):

    image = Find_Crowns_in_Image(inputImage,ex_images_up)
    image = Find_Crowns_in_Image(inputImage,ex_images_right)
    image = Find_Crowns_in_Image(inputImage,ex_images_down)
    image = Find_Crowns_in_Image(inputImage,ex_images_left)
    return boxes



