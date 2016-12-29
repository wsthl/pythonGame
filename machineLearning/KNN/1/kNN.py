from numpy import *
import operator

# create a dataSet which contains 4 Samples
def createDataSet():
	group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
	labels = ['A','A','B','B']
	return group,labels

def kNNClassify(newInput,dataSet,labels,k):
	numSamples = dataSet.shape[0]

	#step1 : caculate the distance
	diff = tile(newInput,(numSamples,1)) - dataSet
	squaredDiff = diff ** 2
	squaredDist = sum(squaredDiff,axis = 1)
	distance = squaredDist ** 0.5

	#step2 : sort the distance
	sortedDistIndices = argsort(distance)

	#step3 : choose the min k distance
	classCount = {}
	for i in xrange(k):
		voteLabel = labels[sortedDistIndices[i]]

	#step4: count the times labels occur
		classCount[voteLabel] = classCount.get(voteLabel,0)+1

	#step5: the max voted class will return 
	maxCount = 0
	for key ,value in classCount.items():
		if value > maxCount :
			maxCount = value
			maxIndex = key

	return maxIndex



