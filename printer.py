import math
from duplicates import buildDuplicatesList # refactored duplicate function
from PIL import Image

iSquareRadius = 8 # square radius of 16x16 tiles is 8

# given int, returns array representing x, y coordinates
def getStartingCoordinatesOfRing(iRingNumber, iSquareRadius):
    return [2*iRingNumber*iSquareRadius, iRingNumber*iSquareRadius]

def printHex(sTownName):
    # initialize vars
    
    lDirectionVectors = [(0,-2*iSquareRadius),(-2*iSquareRadius,-1*iSquareRadius),(-2*iSquareRadius,1*iSquareRadius),(0,2*iSquareRadius),(2*iSquareRadius,1*iSquareRadius),(2*iSquareRadius,-1*iSquareRadius)] # down, SSW, NNW, up, NNE, SSE... and no, SSW is not southby -_-
    iNumRings = 23
    lRepeatImageNames = buildDuplicatesList(sTownName)
    iImageWidth = 2*iNumRings*2*iSquareRadius
    iImageHeight = 2*iNumRings*2*iSquareRadius
    oImage = Image.new('RGBA', (iImageWidth, iImageHeight)) # initialize our image we will build # TODO: add padding?
    
    # initialize vars for loop - start pattern off with tile in the center (exact centered around 0 will be minus a radius in x and plus a radius in y)
    iImageIndex = 0
    iDirectionVectorsIndex = 0
    sFileName = lRepeatImageNames[iImageIndex] # first tile image will be the tile that is repeated most - and will continue for the number of times
    oTileImage = Image.open(sFileName)
    lCurrentDirectionVector = lDirectionVectors[iDirectionVectorsIndex] # initial direction for each ring (down)
    oImage.paste(oTileImage, (iImageWidth / 2 - iSquareRadius,iImageHeight / 2 - iSquareRadius)) # tile in center of image
    iImageIndex = iImageIndex + 1 # increment image index
    
    for i in range(1,iNumRings): # loop through desired ring numbers
        iNumTiles = i*6 # ring 1 has 
        iDirectionRepeatAmount = i # the number of times to repeat a direction before changing it also happens to be the ring number
        lCurrentTileCenterCoordinates = getStartingCoordinatesOfRing(i, iSquareRadius) # starting coordinate of this ring
        iSameDirectionTimes = 0 # initialize times
        iDirectionVectorsIndex = 0 # initialize direction index
        lCurrentDirectionVector = lDirectionVectors[ iDirectionVectorsIndex % len(lDirectionVectors) ]
        print "RING " + str(i) + "------------------------------"
        for j in range(0,iNumTiles): # print tiles for this ring
            if iSameDirectionTimes == iDirectionRepeatAmount: # first determine direction for this
                iSameDirectionTimes = 0 # reset direction count
                iDirectionVectorsIndex = iDirectionVectorsIndex + 1 # increment to new direction ( we walk around the rings clockwise as we 'paint' )
                lCurrentDirectionVector = lDirectionVectors[ iDirectionVectorsIndex % len(lDirectionVectors) ] # modulo gives us the proper index such that lDirectionVectors acts as a cirular list
            if iImageIndex == len(lRepeatImageNames): # we've exhausted all our tiles
                print "No more tiles :( headin on out..."
                oImage.save("results/" + sTownName + '.png') # save the finished image in the folder with its tiles
                return # done processing
            sFileName = lRepeatImageNames[iImageIndex] # first tile image will be the tile that is repeated most - and will continue for the number of times
            oTileImage = Image.open(sFileName) # open the image that corresponds to the duplicate data
            print "Current tile coord: (" + str(lCurrentTileCenterCoordinates[0]) + ", "+ str(lCurrentTileCenterCoordinates[1]) + ")"
            oImage.paste(oTileImage, (iImageWidth / 2 - iSquareRadius + lCurrentTileCenterCoordinates[0],iImageHeight / 2 - iSquareRadius + lCurrentTileCenterCoordinates[1])) # paste this tile at these coordinates into the image!
            print "Now moving " + str(lCurrentDirectionVector[0]) + " in X"
            print "and " + str(lCurrentDirectionVector[1]) + " in Y"
            lCurrentTileCenterCoordinates[0] = lCurrentTileCenterCoordinates[0] + lCurrentDirectionVector[0] # x direction to go from vector
            lCurrentTileCenterCoordinates[1] = lCurrentTileCenterCoordinates[1] + lCurrentDirectionVector[1] # y direction to go from vector
            iImageIndex = iImageIndex + 1 # increment image index
            iSameDirectionTimes = iSameDirectionTimes + 1 # also increase direction 'times'
            
def printSnowflake(sTownName):
    print "cool function, bro"

# recursive fractal function called by def printBinaryTree
def drawTree(x1, y1, angle, depth, oImage, iImageIndex, lRepeatImageNames):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        # pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
        sFileName = lRepeatImageNames[iImageIndex] # first tile image will be the tile that is repeated most - and will continue for the number of times
        oTileImage = Image.open(sFileName)
        oTileImage = oTileImage.resize((oTileImage.size[0]*depth, oTileImage.size[1]*depth), Image.ANTIALIAS)
        oImage.paste(oTileImage, (x2, y2)) # paste the currently indexed image at the current tree coordintes
        iImageIndex = iImageIndex + 10 # next image
        print iImageIndex
        drawTree(x2, y2, angle - 45, depth - 1, oImage, iImageIndex, lRepeatImageNames)
        drawTree(x2, y2, angle + 45, depth - 1, oImage, iImageIndex, lRepeatImageNames)

def printBinaryTree(sTownName):
    # initialize vars
    iImageIndex = 0
    iNumLevels = 9
    lRepeatImageNames = buildDuplicatesList(sTownName)
    iImageWidth = 15*iNumLevels*2*iSquareRadius
    iImageHeight = 15*iNumLevels*2*iSquareRadius
    oImage = Image.new('RGBA', (iImageWidth, iImageHeight)) # initialize our image we will build # TODO: add padding?
    drawTree(300, 550, -90, iNumLevels, oImage, iImageIndex, lRepeatImageNames)
    oImage.save(sTownName + "/" + sTownName + '_binary_tree.png') # save the finished image in the folder with its tiles

