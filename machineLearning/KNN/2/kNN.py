from numpy import *
import operator
import os 

# classify using kNN  
def kNNClassify(newInput, dataSet, labels, k):  
    numSamples = dataSet.shape[0] # shape[0] stands for the num of row  
  
    ## step 1: calculate Euclidean distance  
    # tile(A, reps): Construct an array by repeating A reps times  
    # the following copy numSamples rows for dataSet  
    diff = tile(newInput, (numSamples, 1)) - dataSet # Subtract element-wise  
    squaredDiff = diff ** 2 # squared for the subtract  
    squaredDist = sum(squaredDiff, axis = 1) # sum is performed by row  
    distance = squaredDist ** 0.5  
  
    ## step 2: sort the distance  
    # argsort() returns the indices that would sort an array in a ascending order  
    sortedDistIndices = argsort(distance)  
  
    classCount = {} # define a dictionary (can be append element)  
    for i in xrange(k):  
        ## step 3: choose the min k distance  
        voteLabel = labels[sortedDistIndices[i]]  
  
        ## step 4: count the times labels occur  
        # when the key voteLabel is not in dictionary classCount, get()  
        # will return 0  
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1  
  
    ## step 5: the max voted class will return  
    maxCount = 0  
    for key, value in classCount.items():  
        if value > maxCount:  
            maxCount = value  
            maxIndex = key  
  
    return maxIndex   

# convert image to vector
def img2vector(filename):
	rows = 32
	cols = 32
	imgVector = zeros((1,rows*cols))
	fileIn = open(filename)
	for row in xrange(rows):
		lineStr = fileIn.readline()
		for col in xrange(cols):
			imgVector[0,row*32 +col] = int(lineStr[col])

	return imgVector

#load dataSet
def loadDataSet():
	print "----Getting training set-----"
	dataSetDir = 'digits'
	trainingFileList = os.listdir(dataSetDir+'trainingDigits')
	numSamples = len(trainingFileList)

	train_x = zeros((numSamples,1024))
	train_y = []

	for i in xrange(numSamples):
		filename = trainingFileList[i]

		#get train_X
		train_x[i, : ]= img2vector(dataSetDir+'trainingDigits/%s' %filename)

		#get label from filen name such as '1_18.txt'
		label = int(filename.split('_')[0])
		train_y.append(label)

	print"----Getting testing set....."
	testingFilelist = os.listdir(dataSetDir+'testDigits')
	numSamples = len(testingFilelist)
	test_x = zeros(numSamples,1024)
	test_y = []
	for i in xrange(numSamples):
		filename = testingFilelist[i]

		#get train_x
		test_x[i,:] = img2vector(dataSetDir+'testDigits/%s'%filename)

		#get label from file name such as '1_18.txt'
		label =  int(filename.split('_')[0])
		test_y.append(label)

	return train_x,train_y,test_x,test_y

#test hand writing class
def testHandWritingClass():
	#step1:load data
	print 'step1 : load data ....'
	train_x,train_y,test_x,test_y = loadDataSet

	#step2:training....
	print "step2 : training...."
	pass

	#step3: testing
	numTestSamples = test_x.shape[0]
	matchCount = 0
	for i in xrange(numTestSamples):
		predict = kNNClassify(test_x[i],train_x,train_y,3)
		if predict == test_y[i]:
			matchCount+=1

	accuracy = float(matchCount)/numTestSamples

	# step4 :show the result
	print "step4:show the result...."
	print 'The classify accuracy is :%.2f%%'%(accurcy*100)

testHandWritingClass()

