from PIL import Image
import numpy
import os

# variables
def createTiles(sTownName):
    oImage = Image.open(sTownName + "/" + sTownName + ".png")
    oRGBAImage = oImage.convert('RGBA')
    iWidth = oImage.size[0]
    iHeight = oImage.size[1]

    data = numpy.asarray(oRGBAImage)
    count = 0
    for j in range(16,iHeight,16): # y down
        for k in range(16,iWidth,16): # x across
            row = data[j-16:j]
            tile = []
            for i in range(0,16):
                tile.append(row[i][k-16:k])
            oTile = numpy.asarray(tile)
            im = Image.fromarray(oTile)
            if not os.path.exists(sTownName):
                os.makedirs(sTownName)
            im.save(sTownName + "/" + str(count) + ".png")
            count = count + 1
