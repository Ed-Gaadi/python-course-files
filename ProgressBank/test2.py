def getNumberOfUsers():
    usersFile=open("users.txt")
    fileContent=usersFile.read()
    print("Initial String",fileContent)
    fileContentSplit=fileContent.split("\n")
    print(fileContentSplit)
    numberOfUsers=len(fileContentSplit)
    return numberOfUsers

numberOfUsers=getNumberOfUsers()
print(numberOfUsers)