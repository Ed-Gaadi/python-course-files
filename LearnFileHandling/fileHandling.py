myFile=open("myFolder\myFolder2\insideFolder.txt")

content=myFile.read()
print(content)

contentSplit=content.split("\n")
print(contentSplit)