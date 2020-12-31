'''Given an array of integers between 1 and n inclusively,where n is the length of the array, write a function
   that returns the first integer that appears more than once (when the array is read from left to right).
   if no integer appears morethan once your function should return -1.
'''
#solution1
def firstDuplicateValue(array):
	my_dict = dict()
	for item in array:
		if item in my_dict:
			return item 
		elif item not in my_dict:
			my_dict[item] = 1
	return -1
  
#solution2
def firstDuplicateValue(array):
	minimumSecondIndex = len(array)
	for i in range(len(array)):
		value = array[i]
		for j in range(i + 1,len(array)):
			valueToCompare = array[j] 
			if value == valueToCompare:
				minimumSecondIndex = min(minimumSecondIndex,j) 
	if minimumSecondIndex == len(array):
		return -1
	return array[minimumSecondIndex]
  
  '''array = [2, 1, 5, 2, 3, 3, 4]'''
