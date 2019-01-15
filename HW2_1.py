# Clay Oshiro-Leavitt
# coshiroleavitt@wpi.edu
# Algorithms HW2 Question 1

from numpy import ndarray
import random
from numpy import median


def arrayinit(numArray):
	for i in range(0,100):
		# assign a random integer from [1,1000] to ith element of array numArray
		numArray[i] = random.randint(1, 1000)
#		print numArray[i]

def pivotcalc(numArray, start, end):
	# numArray: array (or subarray) being sorted
	# start: starting index
	# end: end index

	# calculate pivot using: first value, last value, median value
	# this limits worst case performance possibilities
	global tempPos
	criticalvalues = [numArray[start], numArray[end], numArray[(end + start)/2]]
	pivot = median(criticalvalues)

	# store the position of the pivot value
	if pivot == numArray[start]:
		tempPos = start
	if pivot == numArray[end]:
		tempPos = end
	if pivot == numArray[(end + start)/2]:
		tempPos = ((end + start)/2)
	return pivot
	# new pivot will be put in RHS position

def partition(numArray, start, end): 
	# numArray: array (or subarray) being sorted
	# start: starting index
	# end: end index
    i = (start - 1)         # smallest element index 

    # determine the pivot value
    pivot = pivotcalc(numArray, start, end)

    # put pivot in RHS position
    numArray[end], numArray[tempPos] = numArray[tempPos], numArray[end]

  
    for j in range(start , end): 
        if   numArray[j] <= pivot: 
          # element is less than or equal to pivot, switch
          # j element with ith element
          # increment index of smaller element 
            i = i + 1 
            numArray[i], numArray[j] = numArray[j], numArray[i] 
  
  	# element i + 1 is larger than last element in current set, perform switch
    numArray[i + 1], numArray[end] = numArray[end], numArray[i + 1] 
    
    # write out to file "output.txt"
    output = open("output.txt", "a")
    for k in range(100):
    	output.write(str(numArray[k]))
       	output.write(", ")
    output.write("\n\n\n")
    return (i + 1)
  
def quickSort(numArray,start,end): 

	# numArray: array (or subarray) being sorted
	# start: starting index
	# end: end index
    if start < end: 
  
        # partIndex: partitioning index 
        partIndex = partition(numArray,start,end) 
  
        # recursively sort elements before, after partition
        quickSort(numArray, start, partIndex - 1) 
        quickSort(numArray, partIndex + 1, end) 

#create an unitialized array of 100 integers
numArray = ndarray((100,), int)
global pivot
global tempPos
pivot = 0
tempPos = 0
arrayinit(numArray)
quickSort(numArray, 0, 99)