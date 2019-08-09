#Reading, writing, appending

#Append: Adding to the end of the file

appendMe = ' even more Some more text'

saveFile = open('exampleFile.txt', 'a')
saveFile.write('\n')
saveFile.write(appendMe)
saveFile.close()