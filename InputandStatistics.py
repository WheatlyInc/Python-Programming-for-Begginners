#Doesn't like anything written without quotes???
name = input('What is your name?: ')
print('Hello', name)



#Below is not available in Python 2.7, only 3 and above
import statistics

exList = [5,3,2,9,7,4,3,1,8,9]

x = statistics.mean(exList)
print(x)

x = statistics.median(exList)

x = statistics.mode(exList)

x = statistics.stdev(exList)

x = statistics.variance(exList)