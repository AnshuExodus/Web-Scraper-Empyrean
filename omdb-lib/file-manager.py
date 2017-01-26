import os
import re
import shutil
import pathlib
import Master_Movie_Genre

# myMovieHomeDirectory = "E:\Temp"
myMovieHomeDirectory = "F:\Movies"
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
    if(movieStr[0] == '{'):
        movieStr = movieStr[movieStr.find('}') + 1:]
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
    if(movieStr.find('{') != -1):
        movieStr = movieStr[:movieStr.find('}')].rstrip()
        movieStr = cleanMovieName_rightSide(movieStr)
    return movieStr

def cleanMovieName(movieStr):
    return cleanMovieName_rightSide(cleanMovieName_leftSide(movieStr))

def lookForYearFromRawMovieName(movieStr):
    movieStr = movieStr.replace('(','[')
    movieStr = movieStr.replace(')',']')
    movieStr = movieStr.replace('{','[')
    movieStr = movieStr.replace('}',']')
    possibilities = (re.findall(r"[^[]*\[([^]]*)\]{0,}", movieStr))
    myList = []
    for chance in possibilities:
        if len(chance) == 4 and chance.isdigit():
            myList.append(chance)
    if len(myList) == 1:
        return myList[0]
    else:
        return None

# print("Performing preliminary calculations...")
# totalCount = 0.0
# for p in pathlib.Path(myMovieHomeDirectory).iterdir():
#     totalCount = totalCount + 1
# currentCount = 0.0

print("Starting database updates!")
for p in pathlib.Path(myMovieHomeDirectory).iterdir():
    percent = round((currentCount/totalCount)*100, 2)
    print("before")
    print(str(percent), end="")
    print("after")

    isFile = False
    finalPath = str(p)
    if p.is_file():
        finalPath = createFolderForFile(str(p))
        isFile = True
    rawMovieName = extractFolderNameFromDirectoryName(finalPath, isFile)
    # try:
    #     Master_Movie_Genre.master(cleanMovieName(rawMovieName), lookForYearFromRawMovieName(rawMovieName))
    # except:
    #     print("Looks like there was a networking error.")
    
    # print(rawMovieName)
    print(cleanMovieName(rawMovieName))
    currentCount = currentCount + 1
    # print(lookForYearFromRawMovieName(rawMovieName))
    # print("\n")
