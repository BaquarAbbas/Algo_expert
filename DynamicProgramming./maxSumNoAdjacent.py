'''
  Write a function that takes in an array of positive integers and returns the
  maximum sum of non-adjacent elements in the array.
  If the input array is empty, the function should return 0.
'''
#Solution1 
def maxSubsetSumNoAdjacent(array):
    if not len(array):
		return 0
	if len(array) == 1:
		return array[0] 
	maxsums = array[:] 
	maxsums[1] = max(array[0],array[1]) 
	for i in range(2,len(array)):
		maxsums[i] = max(maxsums[i -1],maxsums[i - 2] + array[i])
	return maxsums[-1]
  
  #Solution2 
  def maxSubsetSumNoAdjacent(array):
    if not len(array):
		return 0
	if len(array) == 1:
		return array[0] 
	second = array[0]
	first = max(array[0],array[1])
	for i in range(2,len(array)):
		current = max(first,second + array[i]) 
		second = first 
		first = current 
	return first 
