'''
  You're given an array of arrays where each subarray holds two integer values
  and represents an item; the first integer is the item's value, and the second
  integer is the item's weight. You're also given an integer representing the
  maximum capacity of a knapsack that you have.
  Write a function that returns the maximized combined value of the items that
  you should pick as well as an array of the indices of each item picked.
'''
#Solution1 
def knapsackProblem(items, capacity):
    knapSackValues = [[0 for x in range(0,capacity+1)]for y in range(0,len(items) + 1)]
	for i in range(1,len(items) + 1):
		currentWeight = items[i-1][1] 
		currentValue = items[i-1][0] 
		for c in range(0,capacity+1):
			if currentWeight > c:
				knapSackValues[i][c] = knapSackValues[i-1][c] 
			else:
				knapSackValues[i][c] = max(knapSackValues[i-1][c],knapSackValues[i-1][c - currentWeight] + currentValue)
				
	return [knapSackValues[-1][-1],getKnapSackItems(knapSackValues,items)] 
  
def getKnapSackItems(knapSackValues,items):
	sequence = [] 
	i = len(knapSackValues) - 1 
	c = len(knapSackValues[0]) - 1 
	while i > 0:
		if knapSackValues[i][c] == knapSackValues[i-1][c]:
			i -= 1 
		else:
			sequence.append(i-1) 
			c -= items[i-1][1]
			i -= 1
		if c == 0:
			break 
	return list(reversed(sequence))
  
  '''items = [[1, 2], [4, 3], [5, 6], [6, 7]]
     capacity = 10
  '''
