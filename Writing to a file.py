#Reading, writing, appending

writeMe = 'Example text'

saveFile = open('exampleWrite.txt', 'w')    #We open this file with the intention of writing, we would have cleared this file completely
saveFile.write(writeMe)
saveFile.close()    #Very important: Indicates we are done writing