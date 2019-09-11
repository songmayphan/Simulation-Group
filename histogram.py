# Laura Celis
# Problem 3: Data
# CMS 380, Fall 2019

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import numpy as np

# read data values from text
f = np.loadtxt('data.txt', unpack='False')

# create figure
plt.figure()

# Histogram of the data
plt.hist(f, histtype ='bar', bins = 'auto')

# calculate the mean
mean = np.mean(f)
print('Mean: ', mean)

# calculate the variance
sum_ = 0
for i in range(len(f)):
    sum_ += (float(f[i]) - mean) ** 2 # Sum of squared distances
variance = sum_/(len(f)-1)
print('Variance: ', variance)

# Title and axis labels
plt.title('Histogram')
plt.xlabel('Data Values')
plt.ylabel('Freqency/Count')

# Save figure to a file 
plt.savefig('1_histogram.pdf', bbox_inches='tight')