
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

def GetListOfConnectedTilesCount(matrixToSearch, namesList):            #Returns a list of the count of each tile group, like "meadow1", "desert1", "desert2", "water3" and so on
    listToReturn = []
    for name in namesList:
        listToReturn.append(FindNumberOfTilesWithID(matrixToSearch,name))

    return listToReturn


def GetCrownsForEachTerritory(differentNamesList, territoryMatrix, crownMatrix):
    listOfCrownValues = []
    for name in differentNamesList:
        crownCount = 0
        for i, y in enumerate(territoryMatrix):
            for j, x in enumerate(y):
                if x == name:
                    if(crownMatrix[i][j] != 0):
                        crownCount += crownMatrix[i][j]

        listOfCrownValues.append(crownCount)
    return listOfCrownValues


def GetPointsFromTerritoriesMultipliedByCrowns(inputTerritoryMatrix, crownMatrix):

    territoryNames = GetDifferentTerritoryNames(inputTerritoryMatrix)

    tilesCount = GetListOfConnectedTilesCount(inputTerritoryMatrix, territoryNames)

    crownCount = GetCrownsForEachTerritory(territoryNames, inputTerritoryMatrix, crownMatrix)
    print("crownCount",crownCount)
    points = 0
    for i, entry in enumerate(tilesCount):
        points += tilesCount[i] * crownCount[i]

    return points


