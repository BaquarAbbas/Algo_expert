'''
  Write a function that takes in a sorted array of distinct integers and returns
  the first index in the array that is equal to the value at that index. In
  other words, your function should return the minimum index where index == array[index].
  
  If there is no such index, your function should return -1.
 '''
 #Solution1 
 def indexEqualsValue(array):
    for i in range(len(array)):
		if i == array[i]:
			return i 
	return -1 
 
 #Solution2
 def indexEqualsValue(array):
    leftIdx = 0 
	rightIdx = len(array) - 1
	while leftIdx <= rightIdx:
		middleIdx = leftIdx + (rightIdx - leftIdx)//2 
		middleValue = array[middleIdx] 
		
		if middleValue < middleIdx:
			leftIdx = middleIdx + 1 
		elif middleIdx == middleValue and middleIdx == 0:
			return middleIdx 
		elif middleIdx == middleValue and array[middleIdx - 1] < middleIdx - 1:
			return middleIdx 
		else:
			rightIdx = middleIdx - 1 
	return -1
  
'''array = [-5, -3, 0, 3, 4, 5, 9]'''
