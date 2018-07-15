# dupFinder.py - a functionalized version of code found at https://www.pythoncentral.io/finding-duplicate-files-with-python/
# by Andres Torres (removed system prints and converted __main__ to a defintion)
import os, sys
import hashlib

def findDup(sParentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(sParentFolder):
        # print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
def buildResults(dict1):
    lRepeatImageNamesFlattened = []
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        results = sorted(results, key=len, reverse=True) # sort entire found list by the length of the sublists
        totalCount = 0
        lRepeatImageNames = []
        for result in results:
            totalCount = totalCount + len(result)
            lRepeatImageNames.append(result)
        for lSubList in lRepeatImageNames:
            for sItem in lSubList:
                lRepeatImageNamesFlattened.append(sItem)
        return lRepeatImageNamesFlattened
    else:
        return []
 
def buildDuplicatesList(sFolder):
    dups = {}
    # process the folder passed
    if os.path.exists(sFolder):
        # Find the duplicated files and append them to the dups
        joinDicts(dups, findDup(sFolder))
    else:
        print('%s is not a valid path, please verify' % i)
        sys.exit()
    lRepeatImageNames = buildResults(dups)
    return lRepeatImageNames
        
        
        
        