import os
import shutil


def main(args):
    files = os.listdir()
    folderNumber = int(len(files) / args)
    folderGenerator(folderNumber)
    fileMover(args, files)


def folderGenerator(folders):
    for x in range(folders + 1):
        os.makedirs(str(x))


def fileMover(filesPerFolder, filesList):
    localLoopCounter = 0
    folderCounter = 0

    for x in range(len(filesList)):
        if localLoopCounter == filesPerFolder:
            folderCounter = folderCounter + 1
            localLoopCounter = 0
        currentFile = str(filesList[x])
        shutil.copy(currentFile, str(folderCounter))
        localLoopCounter = localLoopCounter + 1


main(4)
