#PythonTest
# condition = condition + 1
'''
multiple
lines
can go
here
'''
print('hello', "there")
print('5'+'I am')
print('I\'m 5')
print(4**2)


condition = 1

while condition < 10:
    print(condition)
    condition += 1

print("I ended it")

exampleList = [1,6,7,3,6,9,0]

for thing in exampleList:
    print(thing)
for x in range(1, 11):
    print(x)
for x in xrange(1, 11):
    print(x)

x = 2
y = 7
z= 10
if x > y:
    print(x, 'is greater than', y)
if x < y:
    print(x, 'is less than', y)
if  x == y:
    print(x, 'is the same as', y)

if x == '2':
    print(x, 'equals the string 2')
if x < '2':
    print(x, 'is less than 2')
    #This IF statement may result in an error since x is not the correct datatype

