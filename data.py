import matplotlib
import numpy as np
matplotlib.use('Agg')
from matplotlib import pyplot as plt


file = open("data.txt","r")
data = file.readlines()
data_conv = np.array(data).astype(np.float)
mean = sum(data_conv)/len(data) 

sum_ = 0
for i in range(len(data)):
    sum_ += (float(data[i]) - mean) ** 2 # Sum of squared distances

variance = sum_/(len(data)-1)
std_dev = variance ** .5

print("Sum of squared distances: " + str(sum_))
print("Mean:" + str(mean))
print("Variance: " + str(variance))
print("Standard Deviation: " + str(std_dev))
print("Data Sample Size: " + str(len(data)))

data_hist = [variance]

plt.figure()
plt.hist(data_conv, int(len(data)* 0.1))
plt.title('Histogram - Problem 3')
plt.xlabel('Data value')
plt.ylabel('Frequency')
plt.savefig('Data_histogram.png', bbox_inches='tight')
