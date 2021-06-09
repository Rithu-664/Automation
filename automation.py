import os
import shutil

inputPath = input('Enter path name')
length = os.listdir(inputPath)

if os.path.exists(inputPath):
    listOfDirectories = os.listdir(inputPath)
    if len(listOfDirectories) != length:
        for files in listOfDirectories:
            name,ext = os.path.splitext(files)
            ext = ext[1:]
            if ext == "":
                continue
            if os.path.exists(inputPath+'/'+ext):
                shutil.move(inputPath+'/'+files,inputPath+'/'+ext+'/'+files)
            else:
                os.mkdir(inputPath+'/'+ext)
                shutil.move(inputPath+'/'+files,inputPath+'/'+ext+'/'+files)

else:
    print('Directory could not be found') 