example = [
    ['corn1', 'desert1', 'corn2', 'coal1', 'desert2'],
    ['coal2', 'desert1', 'corn2', 'corn2', 'forest'],
    ['coal2', 'desert1', 'empty', 'corn2', 'corn2'],
    ['coal2', 'coal2', 'meadow1', 'meadow1', 'corn2'],
    ['corn3', 'corn3', 'desert3', 'desert3', 'meadow2']]

exampleCrowns = [
    [0, 0, 0, 2, 0],
    [1, 1, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [2, 3, 0, 0, 1],
    [0, 0, 0, 0, 0]]


def GetDifferentTerritoryNames(inputMatrix):
    listOfDifferentNames = []
    for y in inputMatrix:  # For each row
        for string in y:  # ... for each string in the row
            if string not in listOfDifferentNames:  # if the string is NOT found in list of different names, Append it
                listOfDifferentNames.append(string)
    return listOfDifferentNames # A list of the different names is returned


def FindNumberOfTilesWithID(matrixToSearch, tileName: str):
    connectedTilesCount = 0
    for y in matrixToSearch: # for each row
        for string in y: #... for each string in the row
            if tileName in string: # if the tilename is in the string
                connectedTilesCount += 1 # ... add 1 to the counter int
    print(tileName + " - " + str(connectedTilesCount))
    return connectedTilesCount

def GetListOfConnectedTilesCount(matrixToSearch, namesList):
    listToReturn = []
    for name in namesList:
        listToReturn.append(FindNumberOfTilesWithID(matrixToSearch,name))

    return listToReturn


def GetCrownsForEachTerritory(differentNamesList):
    listOfCrownValues = []
    for name in differentNamesList:
        crownCount = 0
        for i, y in enumerate(example):
            for j, x in enumerate(y):
                if x == name:
                    if(exampleCrowns[i][j] != 0):
                        crownCount += exampleCrowns[i][j]

        listOfCrownValues.append(crownCount)
    return listOfCrownValues

territoryNames = GetDifferentTerritoryNames(example)

tilesCount = GetListOfConnectedTilesCount(example,territoryNames)
print("tilesCount is: " ,tilesCount)

crownCount =GetCrownsForEachTerritory(territoryNames)
print("crownCount is: " ,crownCount)

def AddTilesAndCrownTogether():
    points = 0
    for i, entry in enumerate(tilesCount):
        points+= tilesCount[i] * crownCount[i]
    return points

points = AddTilesAndCrownTogether()
print("points", points)

# for name in GetDifferentTerritoryNames(example):
#     points += FindNumberOfTilesWithID(example, name)
#
# print("points is: ", points)

