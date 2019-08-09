x = 6
#x is a global variable


def example3():
    global x
    x += 1
    print(x)


def example():
    z = 5   #local variable, but global to this function
    print(z)


def example2():
    z = 7
    print(z)

    #x += 1  #we cannot modify x, but we can read from it
    #print(x)

    y = x + 1
    print(y)
    return y


example()
x = example2()
print(x)

example3()