'''
  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.
'''
#Solution1
def sortedSquaredArray(array):
	res = [] 
	for ele in array:
		item = ele * ele 
		res.append(item) 
	res.sort() 
	return res 
#Solution2
def sortedSquaredArray(array):
    # Write your code here.
	res = [0 for _ in array]
	small = 0 
	largest = len(array)-1 
	for idx in reversed(range(len(array))):
		smallerValue = array[small] 
		largerValue = array[largest] 
		
		if abs(smallerValue) > abs(largerValue):
			res[idx] = smallerValue * smallerValue 
			small += 1 
		else:
			res[idx] = largerValue*largerValue
			largest -= 1 
	return res
'''array = [1,2,3,4,5,6,7,8,9]''' 
