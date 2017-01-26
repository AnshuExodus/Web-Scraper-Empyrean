import os
import shutil
import pathlib

# myMovieHomeDirectory = "E:\Temp"
myMovieHomeDirectory = "E:\Movies"
slashType = "\\" # Use the other slash for Linux-based systems.


def createFolderForFile(fileStr):
    newFilePath = str(fileStr[:(fileStr.rfind("."))])+slashType
    if(os.path.isdir(newFilePath) == False):
        os.makedirs(newFilePath)
    return shutil.move(fileStr, newFilePath)

def extractFolderNameFromDirectoryName(fileStr, isFile):
    if(isFile):
        directoryName = str(fileStr[:(fileStr.rfind(slashType))])
    else:
        directoryName = fileStr
    folderName = directoryName[directoryName.rfind(slashType) + 1:]
    return folderName

def cleanMovieName_leftSide(movieStr):
    movieStr = movieStr.lstrip()
    if(movieStr[0] == '['):
        movieStr = movieStr[movieStr.find(']') + 1:]
        movieStr = cleanMovieName_leftSide(movieStr)
    if(movieStr[0] == '('):
        movieStr = movieStr[movieStr.find(')') + 1:]
        movieStr = cleanMovieName_leftSide(movieStr)
    if(movieStr[0] == '-'):
        movieStr = movieStr[movieStr.find('-') + 1:]
        movieStr = cleanMovieName_leftSide(movieStr)
    return movieStr

def cleanMovieName_rightSide(movieStr):
    if(movieStr.find('(') != -1):
        movieStr = movieStr[:movieStr.find('(')].rstrip()
        movieStr = cleanMovieName_rightSide(movieStr)
    if(movieStr.find('[') != -1):
        movieStr = movieStr[:movieStr.find(']')].rstrip()
        movieStr = cleanMovieName_rightSide(movieStr)
    return movieStr

def cleanMovieName(movieStr):
    return cleanMovieName_rightSide(cleanMovieName_leftSide(movieStr))

for p in pathlib.Path(myMovieHomeDirectory).iterdir():
    isFile = False
    finalPath = str(p)
    if p.is_file():
        finalPath = createFolderForFile(str(p))
        isFile = True
    rawMovieName = extractFolderNameFromDirectoryName(finalPath, isFile)
    print(rawMovieName)
    print(cleanMovieName(rawMovieName))
