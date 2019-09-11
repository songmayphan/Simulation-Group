import matplotlib.pyplot as plot
#import numpy as np


file = open("data.txt", "r")
if file.mode == "r":
    f1 = file.readlines()

list = []

totalSum = 0;
numLines = 0;
for x in f1:
    totalSum += float(x)
    numLines += 1
    list.append(float(x))
    
#list.pop(0)

average = totalSum/numLines
print("The mean is: " + str(average))

variance = 0

#Calculate Variance
for x in f1:
   variance += (float(x) - average)**2

variance /= (numLines - 1)
print("The Variance is: " + str(variance))


#Print the results to a histogram and save it
plot.xlabel('Values')
plot.ylabel('Ocurrences')

plot.hist(list, bins = 50, rwidth = 0.5)

#plot.style.use('ggplot')

plot.savefig("histogram.png")

#Maplotlib