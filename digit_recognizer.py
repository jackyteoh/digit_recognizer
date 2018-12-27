#Digit Recognizer 
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

# add this to btoi file so you get a usable text output
fprintf(fp2, "%4d", 0); # pads a zero
while ((c = getc(fp1)) != EOF){
	for (i = 1; i <= y; i++){
		for(j = 1; j <= x; j++){
			c = getc(fp1);
			fprintf(fp2, "%4d", c);
		}
	}
}