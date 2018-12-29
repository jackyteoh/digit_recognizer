#Jacky Teoh
#Handwritten Digit Recognizer

#50 hidden nodes
#then 100, then 300 once the initial 50 are working
#5 output nodes (0 1 2 3 4)
#train raw and train labels go together
#test raw and test labels go together
#each image in the raw corresponds to each label 
# 28x28 pixels = 784 pixels total
# read in images one by one, until 28038 images
# 28038 train files, 2561 images in test file
# trainlabels file there are 28038 rows of numbers 
# in testlabels > 2561 rows
# calculate mean squared error
# input all images, back propogate, check mean squared, 
# when you train, keep the resulting weights and biases you've used to train on those again (in an array?)

import numpy as np 

# The Sigmoid function, used for activation
def sigmoid (x, deriv=False):
	if deriv:
		return x * (1-x)
	return 1 / (1 + np.exp(-x))

# Function for the mean squared error
#def mean_squared_error ():

test_labels_arr = []
train_labels_arr = []
bias = 0.1
weight = 0
number_of_times_trained = 0
output_layer = [0, 0, 0, 0, 0]

# Reading in the test and train labels and putting them into arrays
test_labels = open("test_labels.txt", "r")
train_labels = open("train_labels.txt", "r")
test_initial = test_labels.readlines()
train_initial = train_labels.readlines()
for x in test_initial:
	test_labels_arr.append(x.strip())
for y in train_initial:
	train_labels_arr.append(y.strip())

# Finds the max value in the output layer (which is most likely the number)
def find_max (output_layer):
	for x in output_layer:
		highest = output_layer[0]
		if (x > highest):
			highest = x
	return highest

# Finds the position of the max in the output layer
def find_position (output_layer):
	position = 0
	for x in output_layer:
		if (x != find_max(output_layer)):
			position += 1
		else:
			return position

# Based on the position, returns what the number is (since its the highest, most probably is that number)
def the_number (output_layer):
	number = find_position(output_layer)
	if (number == 0):
		print ("This number is a 0")
	else if (number == 1):
		print ("This number is a 1")
	else if (number == 2):
		print ("This number is a 2")
	else if (number == 3):
		print ("This number is a 3")
	else if (number == 4):
		print ("This number is a 4")


test_labels.close()
train_labels.close()