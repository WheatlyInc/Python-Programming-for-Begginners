#Tuples, unlike Lists, cannot be changed once defined (immutable)

def example():
    return 15,19

a,b = example()

#You can define tuples like this: 3,4,5,6   or even this with brackets: (3,4,5,6)

print a
print b

#Lists
#There really isn't any such thing of arrays in Python, just lists

x = [6,2,3,6,8,9,4,3]
print(x)
print x[5]

x.append(12)
print(x)

x.insert(5, 7)
print x

x.remove(7)
#If you have multiple elements of the same ^value, it removes the first element in the list
print x

#Can find the first instance of the element in a list
print(x.index(12))

print(x.count(3))

x.sort()

print(x)

x = ['Spot', 'Cam', 'Jan', 'Dave', 'Zack']
print(x)

x.sort()
print x

x.reverse()
print x
