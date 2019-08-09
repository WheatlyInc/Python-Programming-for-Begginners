#Reading, writing, appending

#Reading from exampleFile

readMe = open('exampleFile.txt', 'r').read()
print(readMe)

splitMe = readMe.split('\n')    #Splits by a new line

print(splitMe)

print

print(splitMe[1])

print

readMe2 = open('exampleFile.txt', 'r').readlines()
print(readMe2)