'''Write a function that takes in a "special" array and returns its product sum.'''
'''
  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.'''
  
def productSum(array,multiplier = 1):
    Sum = 0
	for ele in array:
		if type(ele) is list:
			Sum += productSum(ele,multiplier+1)
		else:
			Sum += ele
    return Sum * multiplier 
    
'''array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]'''

