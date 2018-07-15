from printer import printHex
from printer import printBinaryTree
from tiles import createTiles

# all towns and cities from johto and kanto
lTownNames = ["azalea", "blackthorn", "celadon", "cerulean", "cherrygrove", "cianwood", "cinnabar", "ecruteak", "fuchsia", 
"goldenrod", "lavender", "mahogany", "newbark", "olivine", "pallet", "pewter", "saffron", "vermilion", "violet", "viridian"]

for sTownName in lTownNames:
    # 1. break town map to tiles
    print "Generating tileset for '" + sTownName + "'..."
    createTiles(sTownName)

    # 2. print hex map based on statistics of tiles
    print "Printing hex pattern for '" + sTownName + "'..."
    printHex(sTownName)
    # printBinaryTree(sTownName)

    print "Done."