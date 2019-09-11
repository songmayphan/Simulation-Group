import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def main():
    #read data from file
	dataset = [line.rstrip('\n') for line in open('data.txt')]
	new_dataset = []
	
	#Change to float type
	for i in dataset:
		new_dataset.append(float(i))
		
	#Convert to array
	new_dataset = np.array(new_dataset)
	#Calculate variance and mean
	print("Variance: ", np.var(new_dataset))
	print("Mean:  ", np.mean(new_dataset))
	print("TEST")
	print("Standard Variation: ", np.std(new_dataset))
	#Change to list 
	list_dataset = list(new_dataset)

	# Histogram
	plt.hist(list_dataset, bins='auto', histtype='bar', rwidth=0.9)
	
    # Title and labels
	plt.xlabel('Data')
	plt.ylabel('Frequency')
	plt.title('Histogram of Data')

	# save as pdf
	print("PDF is saving... ")
	plt.savefig('histogram_data.png', bbox_inches='tight')
	print("PDF saved.")


if __name__ == '__main__':
	main()
